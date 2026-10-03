# Seatbelt

Preparation for a Tablekeeper entry in the WeAreDevelopers × BAND Dark Factory hackathon.

**Status: preparation only. This is not a qualifying submission.** There is no service implementation, BAND run, room export, measured result, or presentation in this repository. Public source: https://github.com/ksmostofa/seatbelt. The local checkout has that repository configured as origin.

Seatbelt's proposed product is a restaurant reservation app with a manager interface for recurring bookings and closure recovery. The proposed factory combines separate backend and frontend owners with independent specification-derived tests and review of a frozen commit.

## Why this project

The event has two fixed tracks. An arbitrary new application would not answer the challenge. Tablekeeper matches the user's restaurant experience and offers a concrete UI opportunity: one strong public competitor implements advanced operations through its API but does not provide manager or recurring-booking screens. That gap informs the proposed interface. It does not establish winning odds.

The organizer weights the factory at 50%, the app at 25%, and autonomous agent teamwork at 25%. Implementation that does not originate from the required BAND collaboration cannot qualify, even if it passes tests. Do not convert work done outside BAND into fictional room evidence.

## Read this repository

| File | Purpose |
| --- | --- |
| [RESEARCH.md](RESEARCH.md) | Official rules, current competition evidence, limits of that evidence |
| [FACTORY.md](FACTORY.md) | Proposed agent roles, handoffs, acceptance and measurement plan |
| [PLAN.md](PLAN.md) | Product scope and delivery priorities |
| [BAND_RUNBOOK.md](BAND_RUNBOOK.md) | How to prepare and record an authentic run |
| [ENVIRONMENT.md](ENVIRONMENT.md) | Verified execution blockers, vendor-supported alternatives and executable preparation tools |
| [EVALUATION.md](EVALUATION.md) | Independent verification areas tied to the official specifications |
| [mandates/](mandates/) | Generic, unexecuted standing-instruction templates |

## Required UI choices

Use shadcn with the exact preset `b1VlJBjs`, requested as Luma, and RareUI components only. Resolve the preset with the official installer and record its generated configuration before creating UI. Verify the official RareUI registry and install selected components from it. Do not claim this preset or any component has been installed: no dependencies or app exist yet.

## Next action

Set up a BAND account and three or more real seats, install the organizer harness, verify Docker and model-provider access, then follow [BAND_RUNBOOK.md](BAND_RUNBOOK.md). Update mandate placeholders to match the actual seat harness and model before running. The eventual service must come from that collaboration.

Two standard-library Python tools are ready: `tools/preflight.py` reports local blockers without reading credentials or starting agents; `tools/prepare_dispatch.py` creates a complete task input from all four pristine official specifications and records their hashes. See ENVIRONMENT.md for commands. Preparation tools are not the stage implementation.

Deadline in the authoritative participant guide: October 5, 2026, 23:59 PDT, which is October 6, 2026, 15:59 JST. Recheck organizer announcements before submission.

No 99% winning claim is supportable. Completion, hidden-test correctness, recorded autonomy and final judging remain unknown.
