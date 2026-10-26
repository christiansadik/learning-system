---
name: to-drill
description: Create source-grounded flashcards and practice quizzes for a specific study topic, or resume an unfinished practice attempt. Use independently or after topic orientation; not for cumulative spaced reviews, media generation, or implementing these skills.
---

# Practice Retrieval

Before accessing state, read [the workspace contract](../_study/workspace.md) and [the practice contract](../_study/practice.md). The `_study` bundle is required; `init-study` and `to-map` are not prerequisites for standalone practice.

## Procedure

1. **Select and resume.** Reuse supplied workspace/topic IDs, or initialize through the workspace contract and ask only for missing mission, topic, and material. Follow its active-work guard before changing activities; an unfinished learning dialogue must be resolved through its owning method. Inspect the topic's checkpoint and active attempt. Offer to resume unfinished practice before generating another deck; switch or abandon it only on the learner's explicit choice. Reuse existing sources and IDs. Follow the documented migration consent procedure for older state.
2. **Ground the scope.** Actually inspect relevant readable sources and their recorded scope. Ask whether to proceed when intended material is incomplete; block if no relevant evidence is readable. Register any needed concept IDs with evidence without marking the inventory complete. If a map exists, use its concept IDs where meanings match; a map is not itself a substitute for the underlying sources. External additions require recorded authorization.
3. **Prepare retrieval.** Ask for flashcards, a quiz, or both if the request does not specify. Follow the practice contract for defaults, immutable question records, evidence, answer rubrics, balanced distractors, and presentation. Save all selected questions and the question-only deck artifact before offering practice. An insufficient source supports a smaller set or a request for better material, never fabricated content.
4. **Separate generation from practice.** Offer to start practice unless already requested. Generating a deck does not create learner answers or an attempt, and does not prove learning. Save the deck and its question IDs; a generation-only request can end here. Keep answer keys out of the learner-facing message and question-only deck.
5. **Wait and evaluate.** On practice consent, create and save an attempt with the displayed question order, then present only its pending item(s). Save the exact pending prompt and wait for real learner responses. Use the practice contract's flashcard or quiz feedback timing. Save responses before evaluating, then record evidence-based evaluations. Never fabricate answers, infer correctness from self-confidence, or count revealed answers as unaided retrieval.
6. **Finish or pause.** Complete an attempt only when every response is evaluated or explicitly excluded. Follow the practice contract's result reporting and preserve older attempts. For interruption, persist the active attempt, pending item or correction action, and any unanswered items. End at the release boundary defined in the practice contract: no automatic enrollment, due dates, or cumulative test.

## Boundaries

This skill supplies immediate practice for one specific topic. A new attempt can reuse valid questions, but must not erase earlier answers. Source or question corrections create explicit superseding records. Do not generate audio or podcasts, activate `to-review`, or simulate future review sessions.
