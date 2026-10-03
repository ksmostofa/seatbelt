# Proposed factory

**Unexecuted plan.** This file describes proposed responsibilities, not an observed run. Replace it with a factual account after the run. The owner should write or review the eventual README and FACTORY.md as required by the participant guide.

## Roles

| Seat | Responsibility | Production edits |
| --- | --- | --- |
| Lead | Divide the full task, assign ownership, integrate dependencies, route repairs | No |
| Backend | Implement the service and packaging within assigned ownership | Yes |
| Frontend | Implement the UI and real-service integration within assigned ownership | Yes |
| Tester | Derive independent black-box checks from the full specification | No |
| Reviewer | Review the frozen revision and independently accept or reject it | No |

All harnesses and models are unselected. Mandate templates are not ready for submission until their headers match real configured seats and their filenames match the actual seat names. No seat identities have been created.

## Handoff mechanism

The Lead provides each recipient with the complete applicable requirement text and accessible source paths, assigned file ownership, acceptance criteria and dependencies. Implementers return an exact commit, changed artifacts, executed commands, results and known limitations. The Lead integrates compatible changes and submits a frozen revision to the Reviewer.

The Tester derives a requirement ledger and independent tests from the specification before relying on developer claims. It does not inspect product implementation when designing black-box checks. The Reviewer builds a clean checkout, executes supplied and independent checks, reviews correctness, and accepts or rejects the exact revision. It never repairs production code itself.

On rejection, the Lead routes concrete reproduction steps to the responsible implementer. A repair requires a new commit and independent verification. Preserve the original rejection. Correct first-pass work is valid; do not invent a conflict for appearances.

## Why separate implementation and acceptance

The reviewer cannot treat an implementer's success report as evidence. A shared model can make the same mistake in different roles, so the additional protection comes from different inputs, black-box tests, frozen revisions and reproducible commands. Role separation is not proof that the result is correct.

The frontend and backend can work concurrently inside a stage after agreeing on the exact interface. The stages themselves remain sequential. Copy an accepted stage before extending the next; do not overwrite previous deliverables.

## Measurements to record

- Real dispatch time, final acceptance time and elapsed duration.
- Provider-reported model usage and costs where available; distinguish estimates from measured bills.
- Every accepted and rejected revision with commands, exit codes and output artifacts.
- Specification requirements and independent probes, including gaps not exercised by supplied tests.
- Actual room event IDs demonstrating handoff, review, repair and delivery.
- Known defects, unfinished scope, setup failures and constraints.

| Measurement | Current value |
| --- | --- |
| Execution time | Not measured; no run |
| Model usage / cost | Not measured; no run |
| Completed stages | None |
| Supplied tests | Not executed |
| Independent tests | Not created or executed |
| Accepted revision | None |
| BAND room | Not created |

## Current blockers

This environment has not established a BAND account, configured seats, actual provider access, Docker readiness or a recorded run. The repository deliberately contains no service code or room.json. Follow BAND_RUNBOOK.md before producing a submission.
