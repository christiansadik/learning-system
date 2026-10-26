# Stateful Learning Dialogues

Available from state **1.2.0**. Read [workspace.md](workspace.md) and [state.schema.json](state.schema.json). `to-question` and `socrate` use this contract; later explanation sessions may reuse it. These sessions are separate from quiz attempts and never change quiz percentages or assessed-question indices.

## Session identity and records

Allocate `l001`, `l002`, and so on within the main topic. Store sessions in `learning_records`, selecting unfinished work with the topic checkpoint's `active_session_id`. A record contains activity, topic, source IDs, status, difficulty, ordered turns, observations, pending prompt, start/end times, end reason, and optional summary artifact ID. Use statuses `in_progress`, `completed`, and `abandoned`.

Within each session allocate turn IDs `u001`, `u002`, and so on. A turn has role `learner` or `tutor`, text, timestamp, concept IDs, inspected evidence, optional assessment, and optional `responds_to_turn_id`. Save actual learner text verbatim as an immutable learner turn before creating tutor feedback. Tutor feedback points to the learner turn it discusses. Learner turns never carry an agent-assigned assessment; use the corresponding tutor feedback turn for it. Evidence uses the same source-ID/locator shape as practice.

Observations are append-only records of `gap` or `insight` with a concept ID, description, evidence, learner-turn ID, and actual time. They describe the source-backed interpretation of a real learner contribution, not a fabricated answer or diagnostic percentage. Later improvement adds a new insight/history event rather than deleting a prior gap. If a source is insufficient to assess a contribution, use `not_assessed` and explain the uncertainty.

## Checkpoints and active-work guard

Only one active activity per specific topic is supported: an unfinished practice attempt or a learning session, never both. The checkpoint owns next action/status; an active session's `pending_prompt` owns the exact dialogue prompt, so checkpoint `pending_prompt` is null for an active session. On resume, use the session's prompt and checkpoint's next action. Non-session checkpoints retain their own prompt as before. Do not maintain two editable copies of a dialogue prompt.

Before starting any different activity on the same topic, preserve its active pointer and prompt and ask the learner to resume/finish or explicitly abandon it first. Switching to a different topic preserves the old topic's active work unchanged. Merely displaying an already completed artifact is allowed without altering either checkpoint.

Before yielding, save the session's exact pending prompt and checkpoint action (`formulate_question`, `answer_question`, `respond_to_learner`, or `finish_session`). A pending learner contribution and a pending tutor response are different states. A saved learner turn without feedback resumes at `respond_to_learner`; it must not be requested again. Save source scope and permitted difficulty changes in history so another agent need not infer them from chat.

## Completion, skipping, and artifacts

Continue only with real learner turns and explicit source-grounded feedback. The learner decides when to end; do not infer completion from a turn count or a successful answer. A session with no learner contribution can be abandoned or explicitly skipped, not called completed. An unanswered question at the learner's explicit session end remains an identified unresolved question in the summary; do not fabricate its answer.

Before completing, finish pending feedback on already submitted contributions or explicitly mark it not assessed. Save a new numbered `dialogue-NNNN.md` summary with the activity, session ID, source scope, actual contributions, concept-linked gaps/insights, unresolved questions, and learner's completion choice. Register it as `dialogue_summary` with `question_ids: []` and one topic ID. Only then set the session to completed with its artifact ID/end time, complete that method's step with the same artifact and timestamp, and clear `active_session_id`. Follow the workspace save protocol; recover interrupted finalization idempotently without generating duplicate summaries.

On explicit abandonment, save the reason and end time, preserve all turns, clear the session prompt and pointer, and leave the method unfinished. For an explicit skip or accepted inapplicability, finalize any active session as abandoned with the skip reason and end time, preserve its turns, clear its prompt/pointer, then mark only the method `skipped` with that reason and no completion time. A pause changes neither final status nor completion. Final sessions, turns, and observations remain immutable; factual corrections are appended to history and surfaced when reusing the record.

On completed or skipped methods, offer the next method through the workspace continuation rule. On abandonment ask whether to restart or select another activity, saving that choice as next action. Do not schedule a review, complete the overall cycle, or claim mastery.

## Semantic invariants

- Session IDs are unique; turn IDs are unique within the session. Referenced topics, sources, concepts, observations' learner turns, and feedback targets resolve in their proper scope.
- Session sources belong to the selected topic; evidence cites an inspected source and real locator. Unsupported relationships are labeled unresolved.
- A nonnull active session points to an in-progress record for that topic and matches checkpoint activity. It cannot coexist with an active practice attempt.
- For `socrate`, every pending learner-facing tutor turn contains exactly one question. Persisted difficulty is one of basic/intermediate/advanced; explanations do not automatically demonstrate independent understanding.
- A completed session has at least one learner turn, no unevaluated submitted contribution, a registered dialogue summary, and a valid end time. Abandoned sessions have a reason but no fabricated completed step.
- No dialogue turn or observation creates a practice question, attempt, correctness percentage, or assessed-question reference.
