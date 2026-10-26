# Ticket 06: Evidence and Limitations

Baseline: ticket 05 commit `97b92ea`. Scope: cumulative review, explicit standalone enrollment, policy/schedule history, per-topic/concept metrics, coverage, and migration to shared state 1.5.0. Automatic workflow completion/enrollment remains ticket 07.

## Observed structural evidence

- OpenCode advertised `to-review` after creation.
- The schema parsed as JSON; all 183 local references resolved and patterns compiled.
- All 42 inspected bundled links resolved; all eight skills had matching frontmatter names and descriptions.
- No learner quiz, real state migration, schedule update, or cross-agent session was executed. No automated tests or dependencies were created. Full JSON Schema meta/instance validation remains unverified.

## Independent review

Standards and Spec reviewers inspected the tracked diff and scoped new review files independently. Corrections narrowed the practice-only topic invariant, admitted cumulative-review artifact scope, and explicitly excluded retired concepts from new review selection. Scheduling rules explicitly prevent an aggregate success from overriding a fundamental-concept gap.

Final follow-ups on both axes found no residual actionable findings. Git's tracked-diff whitespace check passed.

## Implementation coverage

The contract keeps each question's primary topic/concept separate from the attempt owner. It preserves immutable answers and distinguishes practice/review purposes, partial attempts, exclusions, latest results, historical totals, and known-inventory coverage. Exact 80% and 50% comparisons are performed before display rounding, with sample sizes and missing evidence visible.

Enrollment records a real completion time and explicit basis without fabricating method completion. Default first due time is completion +3 UTC days; later intervals anchor to completed reviews, with weak-result recovery, normal 7/30-day progression, and capped strong-result intervals. No-score outcomes keep due dates unchanged. Reports, schedule outcomes, and assessment indices are finalized once per attempt through the shared save protocol.

## Remaining gaps

Runtime selection fairness, answer/correction timing, threshold arithmetic on actual records, inventory validation, schedule idempotence, interruption/recovery, source access, and multi-agent activation remain unexercised. The implementation is instruction/schema based rather than a deterministic scheduler. Written criteria and structural review are not proof that an agent follows them correctly.
