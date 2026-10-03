#!/usr/bin/env python3
"""Generate a complete task input from official specs. Does not start agents or create service code."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

SOURCE = "https://github.com/band-ai/dark-factory-wearedevs"


def generate(kickoff: Path, result: Path, output: Path) -> dict:
    kickoff = kickoff.resolve()
    result = result.resolve()
    output = output.resolve()
    if result == kickoff or result.is_relative_to(kickoff):
        raise ValueError("Result must be outside the organizer checkout.")
    if output == result or output.is_relative_to(result):
        raise ValueError("Task input must stay outside the eventual result repository.")
    if output.exists() or output.with_suffix(".manifest.json").exists():
        raise ValueError("Refusing to overwrite an existing task or manifest.")
    try:
        revision = subprocess.run(
            ["git", "-C", str(kickoff), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        dirty = subprocess.run(
            ["git", "-C", str(kickoff), "status", "--porcelain"],
            check=True, capture_output=True, text=True, timeout=10,
        ).stdout
    except (OSError, subprocess.SubprocessError) as error:
        raise ValueError("Cannot establish the official checkout revision.") from error
    if dirty:
        raise ValueError("Organizer checkout is modified; restore it before making a dispatch.")
    remote = subprocess.run(
        ["git", "-C", str(kickoff), "remote", "get-url", "origin"],
        check=True, capture_output=True, text=True, timeout=10,
    ).stdout.strip().removesuffix(".git").rstrip("/")
    if remote != SOURCE:
        raise ValueError("Origin must be the official HTTPS organizer repository.")

    specs = []
    manifest = {"official_source": SOURCE, "revision": revision, "specs": []}
    for stage in range(1, 5):
        path = kickoff / "tablekeeper" / "spec" / f"stage-{stage}.md"
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            raise ValueError(f"Official stage {stage} specification is empty.")
        specs.append((stage, content))
        manifest["specs"].append({
            "stage": stage, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "source": f"{SOURCE}/blob/{revision}/tablekeeper/spec/stage-{stage}.md",
        })

    brief = f"""# Seatbelt: complete BAND task dispatch

This is a task input, not an executed run or completed product. Do not dispatch until
actual seats, mandate headers, provider access and permissions are ready.

Build Tablekeeper through all four stages in order using the genuine BAND room.
Read all complete official specifications below, including cumulative requirements.
Official source: {SOURCE}, revision {revision}. The source package uses Apache-2.0.
Organizer checkout: {kickoff}
Result checkout: {result}

Use Lead, Backend, Frontend, Tester and Reviewer roles. Preserve real bidirectional
addressed handoffs. Lead coordinates and does not write production code. Divide
implementation ownership between Backend and Frontend. Tester derives black-box checks
from the full specifications, independently of implementation. Reviewer verifies exact
frozen commits using a clean container, supplied checks and independent probes. Route
actual rejections to the responsible implementer. Never manufacture a failure or log.

Implement complete buildable stage-1/ through stage-4/ folders, each with Dockerfile
and RUN.md. Copy the accepted previous stage before extending it. Preserve cumulative
compatibility and original accepted outputs. No runtime outbound network may be needed.
Use the exact official API, error behavior, browser routes and test selectors.

For UI use shadcn's exact b1VlJBjs preset and RareUI components only. Resolve the preset
through its official installer and verify the official RareUI registry. Record actual
configuration. Do not replace required behavior with simulated UI success.

After core requirements work, expose policy history, recurring agreements and exceptions,
closure recovery preview and atomic application in manager screens. Distinguish original
confirmation details from current seating. These screens must not break required routes,
contracts, cumulative stages or recovery semantics. Prioritize complete required behavior
over optional polish. Keep the hospitality flow clear at 375px and desktop widths.

Build to the specification, never only to supplied tests. Run independent isolation,
concurrency, retry, temporal-history, browser-recovery and migration checks as applicable.
Read the participant guide at {kickoff / 'docs/participant-guide.md'} for exact harness
commands, constraints, stage claims and submission gates. Check output directories must
be new for each harness run. Record exact revision, commands, real outputs, time, usage
and costs where available. Distinguish measured values from estimates and missing data.

All work must continue from this dispatch without human steering, hints or approvals
during the scored run. Stay within configured permissions. If blocked, report the blocker
truthfully rather than inventing completion. Do not create room.json: the owner must
export the complete actual BAND session after work finishes. Final owner-reviewed README
and FACTORY.md must describe the observed run, not this plan.
"""
    for stage, content in specs:
        brief += f"\n\n## Complete official stage {stage} specification\n\n" + content
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(brief, encoding="utf-8")
    output.with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kickoff", required=True, type=Path)
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    try:
        manifest = generate(args.kickoff, args.result, args.out)
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        parser.exit(1, f"Cannot prepare dispatch: {error}\n")
    print(f"Prepared task input: {args.out.resolve()}")
    print(f"Official revision: {manifest['revision']}")
    print("No agents started. No service code, room log or test result created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
