# Independent evaluation plan

This plan has not run. The Tester must derive exact assertions from the complete official specification in the generated dispatch, rather than treating this overview as the contract. Supplied tests are partial and not a hidden-test certificate.

| Area | Independent probe to design | Source |
| --- | --- | --- |
| Runtime | Clean build, custom PORT, health, no runtime network, resource caps and startup behavior | Stage 1 runtime / delivery |
| Idempotency | Equivalent retry, changed-body key reuse, exact preserved response and state after import | Stage 1 idempotency / export |
| Competition | Simultaneous conflicting writes and retries leave only the permitted reservation state | Stage 1 API |
| Time | Local-time interpretation, invalid or ambiguous DST cases, boundary overlaps | Stage 1 time and DST |
| Atomic moves | Successful cycles, conflicting collective moves, failure leaves every original unchanged | Stage 1 atomic reservation moves |
| Browser race | Search A finishes after search B; every visible result still corresponds to B | Stage 2 competing clients |
| Lost response | Commit followed by response loss preserves uncertain state and retries the same body/key | Stage 2 uncertain outcomes |
| Stale availability | Actual competing booking produces refusal and refreshed availability without false confirmation | Stage 2 competing clients |
| UI contract | Required selectors/routes, readable labels, keyboard focus and 375px overflow | Stage 2 product/browser |
| Combined resources | Single and combined reservations compete for shared resources correctly | Stage 2 combined tables |
| Upgrade | Populate accepted earlier service, export/import into later service, verify existing clients still work | Stage 2 existing clients |
| Historical truth | Accepted terms and past facts remain truthful after newer policies and amendments | Stage 3 policies/history |
| Recurrence | Each occurrence has its own identity and exceptions survive later changes | Stage 3 recurring reservations |
| Collective change | Moves retain prescribed policy/agreement behavior under concurrent writes | Stage 3 collective moves |
| Closure preview | Preview does not mutate state; deterministic specified plan and objective across alternative cases | Stage 4 seating changes |
| Atomic apply | Changed state invalidates stale assumptions as specified; apply succeeds entirely or leaves state unchanged | Stage 4 seating changes |
| Recurring amendment | Allowed targets, exceptions, conflicts and history follow the full specification | Stage 4 recurring amendments |
| User truth | Original receipt remains historical; manager repair changes current seating shown separately | Stage 4 app integration |

Each acceptance record should include the frozen revision, source requirement, input state, exact command, observed output, expected assertion, exit code and untested gaps. Keep a test-setup failure separate from a service defect. Preserve real failures and real repair evidence; do not script a fictional rejection sequence.
