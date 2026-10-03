#!/usr/bin/env python3
"""Read-only local readiness checks. Never connects to BAND or reads credential values."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys


def check_environment(kickoff: Path | None, runtime: str, mandates: Path) -> dict:
    checks = []

    def add(name: str, ready: bool, detail: str, required: bool = True) -> None:
        status = "pass" if ready else "blocked" if required else "optional_missing"
        checks.append({"name": name, "status": status, "detail": detail})

    add("python", sys.version_info >= (3, 12), "Python 3.12+ is required by the organizer harness.")
    for command in ("git", "docker", runtime):
        add(command, shutil.which(command) is not None, f"Executable {command!r} must be on PATH.")

    docker = shutil.which("docker")
    if docker:
        try:
            result = subprocess.run(
                [docker, "info", "--format", "{{.ServerVersion}}"],
                capture_output=True, timeout=10, check=False,
            )
            daemon_ready = result.returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            daemon_ready = False
        add("docker_daemon", daemon_ready, "A reachable running Docker daemon is required.")
    else:
        add("docker_daemon", False, "Cannot probe daemon without Docker CLI.")

    cli_ready = shutil.which("band") is not None
    sdk_ready = importlib.util.find_spec("band") is not None
    add("band_cli", cli_ready,
        "Desktop supplies its matching CLI. SDK agents are an alternative runtime, not proof of Desktop readiness.", False)
    add("band_sdk", sdk_ready,
        "Optional vendor SDK path; install the official extra for the chosen runtime if using SDK seats.", False)
    add("band_tooling", cli_ready or sdk_ready,
        "At least one vendor-supported integration must be installed; authentication remains a manual check.")

    if kickoff is None:
        add("kickoff_specs", False, "Pass --kickoff pointing to the official organizer checkout.")
    else:
        required = [kickoff / "tablekeeper" / "spec" / f"stage-{stage}.md" for stage in range(1, 5)]
        add("kickoff_specs", all(path.is_file() for path in required), "All four official specifications must exist.")
        add("kickoff_harness", (kickoff / "harness" / "cli.py").is_file(), "Official harness CLI must exist.")

    files = sorted(mandates.glob("*.md"))
    configured = len(files) >= 3
    for path in files:
        content = path.read_text(encoding="utf-8")
        configured = configured and "UNSELECTED" not in content
        configured = configured and all(
            any(line.startswith(label) and line[len(label):].strip() for line in content.splitlines())
            for label in ("Harness:", "Model:")
        )
    add("mandate_headers", configured, "At least three templates must name actual configured harnesses and models.")

    # These cannot be inferred from a binary, a config file or a self-reported flag.
    manual = [
        "Sign into BAND Desktop; confirm each real seat is connected and provider access works.",
        "Match mandate filenames and actual seat names, identities, harnesses and models.",
        "Confirm bidirectional addressed messages in the real room and rehearse the toy.",
        "Record the real scored run and export its complete room session at completion.",
    ]
    return {
        "purpose": "Local preparation readiness, not submission eligibility",
        "local_blockers": sum(check["status"] == "blocked" for check in checks),
        "checks": checks,
        "manual_verification_required": manual,
        "qualifying_submission_verified": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kickoff", type=Path)
    parser.add_argument("--runtime", choices=("codex", "claude", "opencode"), default="codex")
    parser.add_argument("--mandates", type=Path, default=Path(__file__).resolve().parents[1] / "mandates")
    args = parser.parse_args()
    report = check_environment(args.kickoff, args.runtime, args.mandates)
    print(json.dumps(report, indent=2))
    return 1 if report["local_blockers"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
