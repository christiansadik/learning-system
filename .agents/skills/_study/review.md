# Cumulative Spaced Review

Available from state **1.5.0**. Read [workspace.md](workspace.md), [state.schema.json](state.schema.json), and [practice.md](practice.md). Question evidence, immutable answers, raw selections, assistance exclusions, correction gating, and attempt finalization reuse the practice contract. This file is authoritative for cumulative selection, enrollment, schedules, metrics, and review-specific completion.

## Enrollment is not mastery or invented completion

Each topic's `review` stores eligibility, basis, actual study-completion time, enrollment time, due date, stage, and append-only history. Initial policy defaults are `interval_days: [3, 7, 30]`, `weak_interval_days: 1`, and `strong_interval_days: 60`; store them in `review_policy`, not agent memory. Values are positive whole UTC-day intervals. Changes require an explicit learner choice and history; existing due dates remain unchanged unless the learner explicitly requests recalculation.

Workflow completion will enroll with basis `cycle_completion`. Independently, a learner may explicitly confirm that a topic was already studied outside this workflow and provide its actual completion time; enroll with basis `learner_attestation`. Preserve unfinished/skipped workflow steps and cycle state instead of inventing prior sessions or calling that cycle completed. If the completion time is uncertain, ask; do not backdate or guess. Future completion times are invalid.

For initial enrollment, set eligible true, stage 0, study-completion time, actual enrollment time, and due time exactly `study_completed_at + interval_days[0]` UTC days. If overdue, display it as overdue rather than moving it forward. Repeated enrollment is idempotent and does not reset history or the first date. Enrollment alone produces no quiz, score, or completed review step. Before its first due date, offer immediate `to-drill` practice instead of treating it as delayed review. Standalone classification uses the explanation contract without requiring a `feynman` session.

## Selection and reservations

One cumulative attempt stays within a main topic. Candidate topics are enrolled and due, plus previously reviewed enrolled topics for interleaving. A newly enrolled topic before its first due time is not a default candidate. If no topic is due, show the next due date and stop; do not start a timer or promise a notification.

Default to ten multiple-choice questions with five options each. Reserve up to two slots for the least-covered eligible concepts/topics and use the remaining slots for oldest-due and weakest topics; for smaller sets reserve at least one coverage slot when there are two or more slots. Round-robin across candidates within these priorities, favor never-assessed concepts, and consult prior question IDs/prompts to avoid claiming repeated questions are new. Limited evidence may require a smaller quiz, intentional reuse, or a missing-source request. Explain the actual selection and limitations in `selection_note`. Coverage opportunities rotate over successive reviews; inaccessible or source-insufficient topics remain explicit gaps, not a promise of guaranteed full coverage.

Keep question difficulty comparable to the latest completed review where practical. New questions may use deeper connections after strong results, but do not compare materially different difficulty as if scores were identical. Every question has exactly one primary topic/concept and inspected source evidence.

Select and reuse questions only for current `in_scope: true` concepts with valid inspected evidence. Retired concept/question associations remain historical, not candidates for new coverage slots. Reactivating a concept requires an explicit scope change recorded in history; do not reactivate it merely to fill a quiz. Superseded or source-inconsistent questions must be inspected and replaced rather than silently reused.

Use the existing `attempts` collection: `purpose: review`, `kind: multiple_choice`, unique selected `topic_ids`, owner in `topic_id`, and the exact ordered questions/responses. Store a question-only artifact of kind `review_questions`, not an immediate practice deck. Reserve all selected topics while that attempt is in progress; only the owner's checkpoint has `active_attempt_id`, activity `to-review`. Reject overlapping active attempts, sessions, or exports on any selected topic. Unrelated topics remain usable.

## Correctness, history, and coverage

Apply the practice contract's real-answer and assistance rules. Revealed, hinted, skipped, invalidated, pending, abandoned, and explicitly disputed evidence do not contribute to unaided completed-review correctness. Never invent a selection to complete a quiz. An all-excluded completed review has no correctness percentage.

For the attempt, each represented topic, and each tested concept, show correct/evaluated counts, excluded counts, sample size, and `100 * correct / evaluated`, or unavailable when evaluated is zero. Compare latest completed review results with historical completed-review totals, summing counts rather than averaging percentages. Clearly separate immediate-practice statistics; do not quietly mix them into spaced-review performance. Topics not tested in this attempt get no new score. Historical corrections/disputes recorded in state history must be surfaced before using affected evidence, not silently overwritten or ignored.

Coverage is assessed in-scope concepts divided by the documented in-scope concept inventory, regardless of whether answers were correct. A concept is assessed only through an unaided evaluated response in a completed practice/review attempt; the question-ID list is a derived index, not a second grading authority. Add review references once at completion. Generating documents, dialogue feedback, assistance, and abandoned attempts do not add coverage.

Concept `in_scope` identifies the current inventory without deleting retired historical IDs. Report assessed/total counts and percentage over known in-scope concepts; when the inventory is incomplete, label it **known-inventory coverage**, not coverage of the whole subject. A zero denominator is unavailable. Set `inventory_complete` true only after checking the declared source scope deliberately and recording the check in `inventory_note` and history; an orientation's ten concepts are insufficient. New concepts or changed source scope reopen inventory completeness unless rechecked. Preserve old question/concept references when retiring a concept.

## Recommendations and scheduling

Use exact ratios before display rounding. Per-topic review correctness strictly below 80% recommends review. For each tested concept with correctness strictly below 50% and current fundamental status true, additionally recommend deeper study; preserve the applicable concept IDs in the schedule outcome. Exactly 80% is not below 80%; exactly 50% is not below 50%. Unknown fundamental status requires contextual classification through the explanation contract before a prerequisite recommendation, not an assumption that null means false. Always show small sample size and untested concepts; these thresholds are study heuristics, not mastery claims.

For each represented enrolled topic, anchor the next interval to the attempt's actual completion time:

- No unaided evaluated answers: preserve stage and due date; record insufficient evidence, not success or postponement.
- Correctness below 80% or any fundamental-concept deeper-study flag: reset stage to 0 and use `min(weak_interval_days, interval_days[0])` days. A strong aggregate must not postpone a fundamental gap.
- Correctness at least 80% with no deeper-study flag: advance stage by one, capped at 2; use the interval at the new stage (normally 7, then 30 days).
- Once already at stage 2, correctness at least 90% with no deeper-study flag permits `strong_interval_days` (normally 60); otherwise remain at the stage-2 interval when no weak/deeper-study rule applies. A strong interval must be at least the configured stage-2 interval.

Record previous/new due date, resulting stage, counts, recommendation, deeper-study concept IDs, attempt ID, and actual outcome time in each topic's review history. Those outcomes are immutable audit snapshots; attempts/responses remain performance authorities. Only topics actually represented are updated. A topic included only through excluded questions retains its due date. Never change schedules from a partial/abandoned attempt or by opening the workspace.

## Finalization and recovery

After all responses are evaluated/excluded, prepare a new private `review-NNNN.md` report with the attempt ID, actual per-topic/concept results, coverage, explanations/source evidence, recommendations, and next due dates. Register it as `review_report` with `question_ids: []`. Store its ID in the attempt's `report_artifact_id` and owner's `to-review` step, complete that step, and mark the attempt completed only as part of the same state replacement that appends schedule outcomes and assessment references. The attempt's original `artifact_id` continues to identify its question-only deck. New in-progress attempts start with `report_artifact_id: null`.

On resume, pending answers and pending correction are different states. An interruption before final state replacement leaves an in-progress attempt; existing report files are reconciled without overwriting. After replacement, check outcome history by attempt ID, restore the report registration, and clear stale active pointers idempotently. At most one outcome per topic/attempt is allowed. Conflicting or partly applied outcomes require explicit reconciliation from snapshots, not a second schedule update. Abandoned attempts retain partial answers but produce no schedule outcomes or completed review step.

After a review, use `choose_next_topic` with an offer to resume study or pause. A standalone review does not automatically complete the initial cycle or launch another method. No background scheduler, future autonomous execution, upload, or notification is implied.
