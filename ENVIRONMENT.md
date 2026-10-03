# Current execution limits and completion path

Checked October 3, 2026. These observations describe this execution environment, not the user's laptop.

| Requirement | Observed here |
| --- | --- |
| Python 3.12+ | Python 3.12.14 available |
| Git | Available; official GitHub fetch succeeded |
| Official kickoff | Fetched separately at revision `803560d2a678ace1414465c098eb0ab5380ffade` |
| BAND Desktop/CLI | Not installed or available as a computer-control app |
| BAND connector | No callable BAND connector found |
| BAND Python SDK | Not installed |
| BAND account credentials | No BAND_API_KEY or BAND_AGENT_ID configured; no credential values read |
| Codex / Claude / OpenCode executable | Not on PATH when checked |
| Docker CLI / standard local daemon sockets | Absent |
| Real room / configured seats / recording | Not established |

A package installation cannot supply account identity, provider authentication or the required genuine room evidence. This environment therefore cannot complete an eligible scored run as configured. The preparation tools do not claim otherwise.

## Vendor-supported options

[BAND Desktop](https://docs.band.ai/band-desktop) bundles its matching CLI and daemon. The guide describes browser sign-in, a fallback account API key and local coding-agent onboarding. The desktop must show actual connected seats, and the final video must record that real collaboration.

The [official Codex SDK adapter](https://docs.band.ai/integrations/sdks/tutorials/codex) can connect headless agents via a signed-in local Codex CLI. It needs a real BAND agent identity and API key. Billing follows the actual Codex login method. Using SDK agents is permitted by the event, but it does not remove the Desktop room/seat and recording obligations. The [official organizer guide](https://github.com/band-ai/dark-factory-wearedevs/blob/main/docs/participant-guide.md) also provides an OpenCode adapter example.

[Codeband](https://github.com/band-ai/codeband) is vendor-owned and supports a headless local mode, but still requires BAND account credentials and provider CLIs. Its default team and approval workflow are not automatically suitable for this event's autonomous recorded-run requirements. Do not treat installing Codeband as a qualifying run.

No provider call, account creation, new paid service or model purchase was performed.

## Execute on a machine with BAND access

1. Install BAND Desktop, sign in, establish the coding runtime and actual provider access, and verify a working Docker daemon.
2. Clone the organizer package separately from the result repository. Set up its Python harness environment exactly as its guide directs. Rehearse the toy in a real room.
3. Resolve mandate headers to the actual harness/model, match filenames to actual seat names and verify at least three real connected identities with bidirectional mentions.
4. Run the read-only readiness checker. Its local checks do not prove account authentication or eligibility.
5. Generate the complete dispatch with the tool below. It embeds all four specifications verbatim, records their SHA-256 values and exact official revision, rejects modified organizer checkouts, and refuses to overwrite existing task inputs.
6. Dispatch it to the authentic BAND Lead. Let the recorded collaboration produce the service. Export the actual room at completion, record the walkthrough, run final gates and submit.

```bash
python tools/preflight.py --kickoff /absolute/dark-factory-wearedevs --runtime codex
python tools/prepare_dispatch.py \
  --kickoff /absolute/dark-factory-wearedevs \
  --result /absolute/band-work/result \
  --out /absolute/band-work/inputs/seatbelt-task.md
```

The input file and manifest must stay outside the final result repository. The generator creates neither an empty stage folder nor a fabricated transcript. No account key belongs in the task input. Keep SDK credential configuration outside the public result and follow the official credential handling guidance.
