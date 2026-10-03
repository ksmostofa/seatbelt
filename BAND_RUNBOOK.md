# Authentic BAND run

This runbook has not been executed. Re-read the [authoritative guide](https://github.com/band-ai/dark-factory-wearedevs/blob/main/docs/participant-guide.md) and announcements before using it. Organizer requirements override this preparation summary.

## Setup before the scored run

1. Register for the event and its required community channels. Create a BAND account and install BAND Desktop using official instructions. Establish actual model-provider access.
2. Clone the official kickoff package separately from this repository. Install the organizer harness with Python 3.12+. Prepare a running Docker daemon and the required browser dependencies.
3. Create the five proposed seats, or at least three distinct real seats. Select the actual harness and model for each. Replace each mandate's UNSELECTED header. Ensure filenames match seat names after ignoring case and punctuation.
4. Give seats access to shared absolute workspace paths, the complete specifications, a separate result checkout, Git identity, and container/browser tools. Keep credentials outside the public repository and room context.
5. Confirm addressed messages and replies work in both directions between the configured seats. Rehearse using the official toy example, then adjust generic process instructions as needed.
6. Resolve human approval prompts and permission configuration before the scored run. Do not bypass account or execution permissions.

## Dispatch and execution

Provide one complete task dispatch with the chosen Tablekeeper track, absolute official spec paths, result path, stage boundaries, generic factory workflow, and required UI choices. Ask seats to read each full specification and delegate complete requirements. Keep domain detail in the task, never in standing mandates.

The scored run must show actual agent collaboration in BAND. Let the seats plan, implement, independently check, reject when warranted and repair. Do not send debugging hints, manually alter production code, approve intermediate decisions or manually rerun until it passes. If the run needs human intervention, record that truthfully and treat it as development rather than falsely claiming autonomy.

Only the code produced through the genuine BAND collaboration belongs in completed stage outputs. This preparation repository cannot supply a substitute room transcript. Do not create a synthetic room.json.

## Verification commands

Run these from the official kickoff package, with `/absolute/result` replaced by the actual result checkout. Agents should perform verification during the recorded run. Confirm current CLI options in the official guide.

```bash
python -m harness run --track tablekeeper --repo /absolute/result --all --mode isolated --out /absolute/checks/final
python -m harness check /absolute/result --track tablekeeper
```

Supplied tests are partial. Require separate probes derived from the full specification and truthful reporting of gaps. A claimed stage in the supplied harness is directional feedback, not hidden-test certification.

## Real submission files

The final result needs README.md, FACTORY.md, mandate files, a full room.json export and each completed stage's buildable source, Dockerfile and RUN.md. Minimum eligibility requires a complete stage 1. Do not add empty stage directories as completion evidence.

In BAND Desktop, open the actual room in the BAND console. Download the **full session**, not a filtered export, after the work completes. Save it as room.json. Preserve the real content. The guide permits replacing exposed credential values with `[REDACTED]` after rotating them; inspect before public publishing and follow that rule precisely.

Record a video showing the real BAND room, an actual handoff and the resulting app. A slide-only explanation is insufficient. Write a factual owner-reviewed FACTORY.md with setup, rationale, actual costs/time, failures and limits. Submit the public GitHub URL, required presentation and video on the event platform.

No account registration, seat creation, run, verification or export has happened in this preparation repository.
