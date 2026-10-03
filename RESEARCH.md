# Research notes

Checked on October 3, 2026, Japan time. Public pages can change. All competitor performance figures below are participant-reported unless explicitly stated otherwise.

## Official requirements

Primary references:

- [Authoritative participant guide](https://github.com/band-ai/dark-factory-wearedevs/blob/main/docs/participant-guide.md)
- [Kickoff package](https://github.com/band-ai/dark-factory-wearedevs)
- [Official event page](https://lablab.ai/ai-hackathons/wearedevelopers-hackathon)
- [Official live dashboard](https://lablab.ai/ai-hackathons/wearedevelopers-hackathon/live)
- [BAND API documentation](https://docs.band.ai/api/introduction)
- [BAND SDK setup](https://docs.band.ai/integrations/sdks/tutorials/setup)

The event page says participation is fully online and open worldwide. Japan is therefore within its advertised eligibility. Teams can have one to six people. Participants must complete registration and follow the event's linked rule book and guidelines.

The participant guide gives the close as October 5, 23:59 PDT. This converts to October 6, 15:59 JST. One event search result displayed 06:59 UTC, consistent with that conversion. The explicit authoritative schedule takes precedence over a broken browser countdown.

The two fixed tracks are Tablekeeper, a restaurant reservation service, and Pocketful, a wallet and payments service. Pick one and stay in it. Tablekeeper has four cumulative stages:

1. API behavior, atomic writes, idempotency and state import/export.
2. Browser product, richer resource model, stale-state and lost-response recovery.
3. Effective-dated policies, truthful history, recurring agreements and individual exceptions.
4. Atomic amendments and deterministic closure replanning that preserves history.

The guide requires at least three actual agent seats, generic mandate files naming their harness/model, bidirectional addressed room messages, a whole-room export, a public repository, a presentation and a video of the factory working. Minimum service eligibility is a complete stage 1. Production code must originate from the BAND collaboration. Mandates containing track-specific terms, paths or error codes disqualify the entry.

Factory is 50% of the rubric, app 25%, and autonomous teamwork 25%. The final scored run must proceed after the task dispatch without human steering, debugging hints, approvals or manual reruns. Development runs used to improve the factory are distinct from the run submitted as autonomous evidence.

The service may use any language. Python 3.12+ is needed for the organizer harness. Each completed stage must have its own complete service, Dockerfile and RUN.md. Judging uses isolated containers with no outbound runtime network. The shipped tests cover only part of each stage, so green supplied checks do not establish full correctness.

## Public field and what the numbers mean

The official dashboard reported 3,520 registered participants, 609 teams, and 27 submissions. It also reported 13 Pocketful and 15 Tablekeeper submissions. Those track counts sum to 28, not 27. Preserve that inconsistency rather than silently choosing a denominator.

Registration is not an eligible-entry count. Entries may fail gates, late entries may arrive, and current submissions may change. Community votes do not represent judge scores. Prize places have minimum eligible-entry thresholds, so six advertised places are not automatically six awarded prizes.

## Examined projects

| Project | Public evidence | Relevant limit or gap |
| --- | --- | --- |
| [Cat in Town Tablekeeper](https://github.com/daphneyyy/table-keeper) | Four stage folders, FACTORY.md and room.json. Its [submission](https://lablab.ai/ai-hackathons/wearedevelopers-hackathon/cat-kathon/tablekeeper-an-agent-built-reservation-system) reports around two hours, 158 applicable supplied final-stage tests, and $29.68 estimated model spend. | The README explicitly says manager and recurring-booking screens are absent; advanced operations use APIs. Hidden organizer tests are outside its evidence. |
| [Obsidian Foundry](https://lablab.ai/ai-hackathons/wearedevelopers-hackathon/dora/obsidian-foundry-self-verifying-dark-factory) | Participant describes four Pocketful stages, 260 requirements, 242 API tests, 58 browser tests, independent tester, frozen-commit reviewer and two actual repairs. | These figures are submission claims, not organizer certification. Independent testing alone is already a competitive pattern. |
| [Dark Factory Pocketful](https://github.com/yanerox69/dark-factory-pocketful) | Stage 1, mandates, FACTORY.md, room.json. Reports 147 shipped checks and 3h49m. | Only stage 1 was shown in the reviewed repository. The [submission](https://lablab.ai/ai-hackathons/wearedevelopers-hackathon/revenueflow/dark-factory-the-band-that-refuses-its-own-work) candidly reports defects the owner caught after review. |
| [L'Étoile Noire](https://github.com/ibrahimjatt1313-prog/DarkFactory) | Public repository and [submission](https://lablab.ai/ai-hackathons/wearedevelopers-hackathon/tensorcraft/letoile-noire-executive-tablekeeper) show a restaurant UI with zone and station management. | Community-vote leadership does not prove conformance to the prescribed stage contracts. No independent score was available. |

## Original project decision

Choose Tablekeeper. Build the exact organizer contract first. Then expose its advanced capabilities through a clear manager interface rather than spending time on unrelated restaurant features.

Proposed demo: a manager closes a table, compares an atomic recovery preview with the current reservations, applies the plan, and shows that current seating changed while the original confirmation and policy history remain truthful. Add recurring-booking exceptions and explicit failed-response recovery. Those behaviors connect the advanced backend requirements to visible product value.

Use independent testing derived from the full specification and review a frozen commit. Measure execution cost and time, and preserve genuine rejected evidence. These are planned mechanisms; this repository has not executed them.

## Missing evidence

No verified prior winner for this exact event was found. The event is still underway. Searches on X/Twitter did not return attributable event-specific project or winner posts. Unrelated repositories called "dark factory" do not count as this event's competitors. There is no defensible calibrated 99% win probability.
