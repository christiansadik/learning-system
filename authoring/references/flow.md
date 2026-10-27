# Complete Interactive Study Flow

Available from shared state **1.6.0**. Read [workspace.md](workspace.md), [state.schema.json](state.schema.json), and [review.md](review.md). Method instructions remain authoritative for teaching behavior; this contract owns dispatch, lifecycle gates, due-review navigation, and initial-cycle completion.

## Dispatch and independent use

`init-study` is explicit entry into orchestrated mode. The first six methods run in order: `to-map`, `to-drill`, `to-question`, `socrate`, `feynman`, `to-docs`. The seventh, `to-review`, is enrolled and deferred, not run as an immediate final quiz. Each method remains independently callable with its required references and no mandatory predecessor installation.

For each controller turn, first restore any active attempt/session/export or pending source request. Otherwise determine the first unfinished gate from actual step/artifact/session records and `cycle.practice_resolution`; do not blindly restart mapping or trust a stale navigation label. Never regenerate a valid completed output without a revision request or explicit source-scope change.

Activate the selected skill natively with the same workspace and topic IDs, mode `orchestrated`, and accepted scope. Host permissions and consent still apply. After its actions, reread the authoritative state. If learner input is pending, save and yield. If only agent work or a permitted next method remains, continue without an extra generic “shall I continue?” prompt; the learner's request for the full flow authorizes that progression, not fabricated learner contributions or bypassed permissions. Avoid a busy loop: no persisted progress or a repeated blocker means stop with a precise request.

Standalone skill use keeps mode `standalone`, records only that activity, and offers rather than automatically activates its successor. It never automatically closes the overall cycle. Entering the full flow later may reuse valid standalone artifacts and real learning records after their scope is checked; do not invent missing evidence.

## Completion gates for one specific topic

Each gate accepts a completed method with matching real artifacts, or an explicit skip/accepted inapplicability with a recorded reason. Missing tools, denial, interruption, failed writes, and a declined invitation are not implicit skips.

- **Map:** readable registered orientation artifact for the current topic and accepted material scope.
- **Drill:** valid registered question-only deck. In orchestrated mode, generation alone is insufficient: also record `cycle.practice_resolution` as `completed_attempt` referencing a completed practice-purpose attempt for this topic with at least one actual learner answer, or `explicit_skip` with the learner's reason for skipping practice. Hints/exclusions are preserved; success is not required. Never fabricate an attempt for a generation-only request. If the whole method was explicitly skipped, no separate practice resolution is required.
- **Questioning, Socrates, explanation:** each completed step resolves to its own completed learning session, actual learner contribution, source-grounded feedback (including explicit not-assessed uncertainty where appropriate), and registered summary. A paused session or unanswered prompt is not sufficient.
- **Documents:** completed export with two readable registered documents, current topic as owner, and matching step entry artifact. Its default scope is the current topic; an explicitly requested combined export is permitted, but inclusion alone does not complete the other topics' gates.

Preserve original completion times and evidence. If a later failed revision is active, resolve it before continuing rather than treating the old completed artifact as proof the revision succeeded. Skipped steps retain their reasons and null completion times. A full cycle requires no active reservations covering the topic and at least one real learner retrieval/reasoning/explanation contribution in the accepted evidence. An all-skipped or document-only path does not justify automatic studied status; offer explicit standalone prior-study attestation instead, without fabricating a completed cycle.

## Cycle finalization and enrollment

For a newly orchestrated cycle, set `cycle.started_at` once to actual time when the learner enters it. Keep `cycle.completed_at` null until every first-six gate has passed. Progress through those gates even when errors or gaps remain; mastery and threshold scores are not completion prerequisites.

Persist `next_action: finalize_cycle` before finalization if needed. Recheck revisions, source scope, artifacts, skip reasons, practice resolution, and absence of active work. In one safe state replacement set cycle status completed and its actual completion time, then enroll review with basis `cycle_completion` and the review contract's first interval (default +3 UTC days). Record completion/enrollment history together. Enrollment does not complete a quiz: preserve the existing `to-review` step, including any prior completed artifact/timestamp, explicit skip, or installation blocker; an untouched available step remains pending. Never reset a previously completed review merely because the initial cycle finished later.

If already enrolled through standalone attestation, preserve its existing basis, initial completion date, due date, and review history; record the now-completed workflow separately rather than resetting a valid schedule. Reopening an already completed cycle does not create a second enrollment or move its due date. Further practice and revisions preserve that history; substantial new material can be introduced as a new specific topic rather than silently resetting the old one.

On recovery, inspect cycle state and eligibility together. A fully saved completion/enrollment is returned idempotently. A conflicting partly applied state is explicitly reconciled from snapshots/history; do not invent completion time or start another three-day clock. After finalization save `choose_next_topic`, report the due date and unresolved gaps, and wait for the next topic/material or pause. No immediate cumulative quiz, timer, notification, or automatic future session is created.

## Due-review navigation without losing study work

The main-topic `flow` record owns navigation, not teaching: `pending_prompt`, `offered_review_topic_ids`, `selected_review_topic_ids`, `return_topic_id`, `review_owner_topic_id`, and `review_owner_checkpoint`. Initialize prompt/return fields null and both topic-ID arrays empty. Offered candidates and the learner's accepted scope are separate facts.

On explicit startup, inspect saved due dates and offer due reviews before new material. Save the exact offer and eligible topic IDs in `flow`; leave every topic checkpoint/active pointer untouched. Restore this prompt after interruption. Declining clears only the navigation offer, not dates, eligibility, or teaching prompts. A normal answer to an ongoing method does not trigger another startup offer.

If the learner chooses review, apply active-work guards to the actual selected review scope. Topics with conflicting work require its explicit completion/abandonment first; do not auto-skip them or destroy their prompt. Eligible nonconflicting scope may be selected explicitly. The review skill chooses/questions from the enrolled pool through its own contract, not just the newest topic.

Before switching, save the accepted scope in `selected_review_topic_ids` and the original selected topic in `return_topic_id`. Choose the review owner from that selected scope and preserve its exact pre-review checkpoint as the immutable suspended `review_owner_checkpoint`, paired with `review_owner_topic_id`. Clear only the offered-candidate array/prompt after recording this accepted context. Set the review owner's active checkpoint only after saving it; other topics' checkpoints remain authoritative and unchanged. The suspended checkpoint is not a second active teaching state and must not be edited during the excursion.

While an excursion is active, resume `to-review` through that owner and persisted selected scope, including before an attempt exists. Pending answers/correction, source blockers, and incomplete finalization remain in that method until resolved or explicitly canceled. A narrowed/replanned scope requires explicit choice and safe restoration of the old owner context before recording the replacement selection; do not infer it from an empty offer or chat memory. Upon completed/abandoned review or cancellation before an attempt starts, restore the owner's suspended checkpoint without reverting step artifacts, answers, metrics, or updated due dates. Return `current.topic_id` to the saved original topic, clear the excursion fields including selected IDs, and resume its real prompt/gates. If there was no original topic, restore null selection and request the next topic. Do not automatically start a second quiz.

Recover interrupted restoration by checking owner/return IDs and whether review work is still active. Restore only after terminal/canceled review, once; conflicting pointers require explicit reconciliation. The same preservation applies when the review owner equals the original study topic. A completed review must never erase the pending invitation/source request that existed before it.

## Semantic invariants

- Practice resolution references a real completed practice attempt for its topic or an explicit skip reason; it never refers to a review attempt.
- Cycle start/completion times reflect real events and are ordered; imported attestation remains separate from workflow completion.
- A completed cycle's first six gates are evidenced; no active work for that topic is left unfinished. Enrollment alone does not satisfy any gate.
- Flow offered/selected IDs resolve to the main topic's eligible topics. An excursion's owner belongs to its nonempty selected scope; any active review attempt matches that scope. The owner checkpoint snapshot is restored without rolling back current domain records.
- A navigation prompt and a teaching prompt have different owners; neither replaces the other. New study topics preserve the main objective and all earlier topic histories.
