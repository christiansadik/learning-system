# Immediate Practice Contract

Applies to shared state **1.1.0**. Read [the workspace contract](workspace.md) and [state.schema.json](state.schema.json) before changing state. This is immediate, single-topic practice, not cumulative spaced review.

## Questions and provenance

Allocate main-topic-scoped question IDs `q001`, `q002`, and so on, and attempt IDs `p001`, `p002`, and so on. Retain IDs permanently. Every question has one primary `topic_id` and `concept_id`, a kind (`flashcard` or `multiple_choice`), prompt, expected answer, rubric, explanation, actual source evidence, difficulty, and creation time. `evidence` records a source ID and a real inspected locator for the answer, not just a link to a generated map.

Use plain-language prompts that assess one intended concept at a time. Flashcards have no options and use an expected-answer rubric. Multiple-choice questions have exactly five distinct options A–E and one correct option, with an explanation supported by the sources. Make distractors plausible without relying on invented facts; use comparable detail and wording and vary the correct position. If material cannot support an unambiguous question, omit it or ask for clarification.

Default to up to ten flashcards or ten quiz questions, fewer when sources are narrow; honor a requested count when evidence supports it. Explain any reduction. Do not promise unlimited unique questions. Reuse a question ID only if its prompt, options, expected answer, rubric, evidence, and difficulty remain unchanged. For revised content, append a new ID with `supersedes_question_id`; preserve the old record and its historical answers. Compare existing questions before generation to avoid accidental duplicates, and identify intentional reuse rather than claiming novelty.

Question records are immutable answer-key authorities. `expected_answer`, `correct_option_id`, rubric, and explanation remain in private state, not in question-only exports or pre-answer chat. This is presentation separation, not access control: a learner with filesystem access can read state and snapshots. Do not claim cryptographic secrecy or tamper resistance.

## Deck artifacts and step completion

Save a numbered `practice-NNNN.md` under the topic's generated area, registered as `practice_questions`. It contains scope, source limitations, question IDs, prompts, and options where applicable; no expected answers, rubric, explanation, or indication of the correct option. This is a derived presentation, not a second question/progress authority.

The artifact record's ordered `question_ids` identifies exactly which immutable questions it presents. Orientation artifact records have `question_ids: []`. Mixed decks may contain both kinds, but each attempt selects one homogeneous kind and explicitly records its own order.

`to-drill` generation is complete once the valid questions, readable deck, provenance, and artifact registration are saved. Set its step artifact and completion timestamp. This describes preparation, not whether practice has finished or been passed. Active practice has its own attempt status and checkpoint even when the deck-generation step is completed. A failed regeneration preserves the previous deck and records the failed activity separately.

After generation without practice consent, save an `awaiting_input` checkpoint with `next_action: offer_practice`, the selected topic, and no active attempt. On explicit refusal or a generation-only request, use the release-boundary checkpoint below. Do not create a fake completed attempt for a declined exercise.

## Attempts and learner answers

Each attempt stores its kind, ordered question IDs, status, actual start and optional completion timestamps, and responses. Only one unfinished active attempt per specific topic is supported. Select it with the topic checkpoint's `active_attempt_id`; this pointer, not narrative history, controls resumption. Switching topics preserves every topic's pointer and pending prompt.

Create all response records with `answer: null`, `selected_option_id: null`, `assistance: none`, `correct: null`, `evaluation_reason: null`, and both timestamps null. Save the attempt and checkpoint before displaying a prompt. `pending_question_id` selects the next unresolved item; it may be null when responses are waiting for correction. Distinguish an absent answer from the learner's explicit skip.

- **Flashcards:** show one front at a time. Wait for the learner's answer or explicit request to reveal. Save their actual answer, then compare against the expected answer and rubric. Accept semantically correct wording, distinguish missing core content from harmless phrasing, and explain feedback using sources. Reveal the explanation only after their response or explicit reveal request. Save before offering the next card.
- **Quizzes:** present the saved ordered question set or the exact unresolved remainder on resume. Save submitted options without exposing correctness; correct only after every question has an unambiguous answer ready for evaluation or a recorded evaluated exclusion (`revealed`, `skipped`, or `invalidated`). Those exclusions satisfy the gate without invented answers. A hinted question still needs a learner answer or explicit exclusion. For early correction, ask whether to abandon the remaining items. If agreed, save abandonment consent in history, evaluate only eligible submitted answers while the attempt remains in progress, then finalize it as abandoned with a reason and end time. Leave unanswered responses untouched; if interrupted during correction, the checkpoint and consent history identify that unfinished finalization. Never fabricate completion or silently replace unanswered items with skips.
- **Hints and reveals:** when explicitly requested, record `assistance: hint` or `revealed` before giving help. A hint can be used for subsequent formative feedback but not an unaided score. A reveal before an answer leaves `answer: null` and sets `assistance: revealed`. Explicit skips set `assistance: skipped`. Assisted/revealed/skipped responses are excluded from unaided correctness counts and from assessed-concept evidence.
- **Uncertain or defective questions:** do not guess the evaluation. Mark a defective item `assistance: invalidated`, explain why, exclude it from counts, and create a corrected question only with a new ID. Preserve the original for history.

Unaided responses receive `correct: true` or `false`, an evidence-based evaluation reason, and `evaluated_at`. For answers awaiting correction, `correct`, evaluation reason, and evaluation time remain null. Excluded responses have `correct: null`, with an exclusion reason and evaluation time. An evaluated hinted response requires an actual learner answer. `responded_at` records the answer time or explicit exclusion time, not the time a hint was offered.

Store submitted text verbatim in `answer`. For multiple choice, separately record the unambiguously selected A–E ID in `selected_option_id` without normalizing away the raw text (for example, retain “I choose B”). If selection is unclear, preserve the raw submission, ask for clarification, and save the clarification in history before filling the selection; do not evaluate or advance meanwhile. Flashcards always leave `selected_option_id` null. A request to change a settled answer is preserved as history and a new attempt, not an overwrite of the original response.

Use `in_progress`, `completed`, or `abandoned` attempt statuses. A completed attempt has every response evaluated or explicitly excluded and an actual `completed_at`. An abandoned attempt records its end time in `completed_at` and a nonempty `end_reason`; it remains excluded from completed-session aggregates. Stop/pause does not abandon or complete an attempt, and partial results do not become final scores. Save each accepted answer and exclusion separately before moving on. Record corrections in a separate save so a session interrupted after answering can resume at `evaluate_answers` without losing that answer.

Completed/abandoned attempts and evaluated responses are immutable. If a later factual correction is needed, append history describing the affected IDs and keep the original record; use a new question/attempt for corrected practice. Later reporting must surface those corrections rather than silently treating disputed evidence as valid. Do not change historical scores by overwriting records.

## Evidence and resumption

At completion report unaided correct/evaluated counts, sample size, correctness percentage, excluded counts, and any pending uncertainty for the attempt and its specific topic. Percentage is `100 * correct / evaluated`, or unavailable when the denominator is zero; display rounding does not change stored evidence. For an abandoned attempt, any displayed partial counts and percentage must be labeled partial and excluded from completed-session aggregates. The records retain denominators and question/concept associations for later metrics; this ticket does not implement cumulative-review selection, historical dashboards, adaptation, or prerequisite recommendations.

For each unaided evaluated response in a completed attempt, add its question ID once to the corresponding concept's `assessed_question_ids`. Record both correct and incorrect assessed answers; assessment coverage is distinct from correctness. Generating, reading, revealing, hinting, skipping, or abandoning practice adds no assessment references. The attempt remains the authoritative performance record; this concept list is a derived index, rebuildable from completed unaided evaluations.

On resume, read the active attempt and restore the same question order and the exact pending prompt. If all responses are answered but not evaluated, resume correction rather than asking the questions again. If an attempt is completed but the checkpoint was not advanced, finish the bookkeeping idempotently; do not duplicate attempts or assessment references. Conflicting checkpoint/attempt references are blockers requiring explicit reconciliation, not a reason to reset progress.

When practice is completed, declined, or explicitly abandoned, clear the active attempt pointer and use `activity: to-question`, `status: blocked`, `next_action: await_next_method`, with a prompt explaining that the next method is unavailable. Keep all later methods unavailable, the overall cycle in progress, and review enrollment and due dates null. Starting another practice set is always an explicit learner choice.

## Semantic checks beyond JSON Schema

- Question IDs, attempt IDs, and responses' question IDs are unique in their scope. `question_ids` contains exactly the response IDs in the same saved order.
- Each question's concept belongs to its specific topic; all evidence sources are registered for that topic and were read for the declared scope.
- Attempt questions have the same topic and question kind as the attempt, and belong to its registered deck. Deck scope, question IDs, and source IDs agree.
- An answer-bearing multiple-choice response with assistance `none` or `hint` must have an offered `selected_option_id` before evaluation, consistent with the preserved raw answer or recorded clarification. Ask on ambiguous input rather than guessing. Revealed, skipped, or invalidated exclusions may have a null selection and no learner answer; record their reason and evaluation time without inventing a selection. Flashcard answers are free text with a null selection.
- Each attempt's `pending_question_id`, if nonnull, names its next unresolved response. It becomes null before final completion or correction when no unanswered response remains.
- Answered items have a response time. Evaluation timestamps do not precede responses; completion does not precede start or included evaluations. Reveals and skips are still recorded with actual times.
- Only an in-progress attempt can be active. A paused session remains in progress. Final attempts cannot receive new responses.
- A completed `to-drill` step references a valid `practice_questions` artifact, not an orientation map. Question and attempt association does not enroll any topic for review.
