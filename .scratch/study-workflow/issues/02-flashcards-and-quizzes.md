# 02: Practice with Flashcards and Quizzes

**What to build:** A learner can invoke `to-drill` for a specific topic, receive source-grounded flashcards and practice quizzes, attempt questions without prematurely exposed solutions, and retain the practice history.

**Blocked by:** 01 — Start and Resume a Study Topic.

**Status:** done

## Context

Read the [source specification](../spec.md), project glossary, and shared workspace contract delivered by ticket 01. Immediate practice is distinct from cumulative spaced review, which ticket 06 delivers.

## Acceptance criteria

- [x] `to-drill` is independently usable with the common workspace and required references.
- [x] Flashcards and practice quizzes are grounded in the selected material and identify their specific topic and relevant concepts.
- [x] Learner-facing presentation separates questions from solutions so retrieval effort remains with the learner.
- [x] Questions have stable identities and record their source basis, concept associations, difficulty, and expected answers in the documented shared format.
- [x] Attempts retain learner answers and evaluations without overwriting previous attempts; partial work is distinguishable from completed results.
- [x] The same associations can be consumed later for per-topic metrics, concept coverage, and repeat-question detection.
- [x] Insufficient or ambiguous material is surfaced rather than padded with unsupported questions or answers.
- [x] Audio and podcast generation are absent from this skill's responsibilities.
- [x] Completion of immediate practice does not silently enroll or complete a cumulative spaced review.
- [x] Document observable acceptance evidence and remaining gaps; do not create automated tests or Git commits without explicit authorization.

## Implementation outcome

Implemented `to-drill`, shared practice instructions, and the versioned question/attempt contract, with consent-based migration from 1.0.0 to 1.1.0 and minimal orientation continuation. Checked boxes indicate instruction/schema implementation coverage, not an exercised learner session.

See [verification evidence and remaining gaps](../verification-02.md). Final independent Standards and Spec reviews reported no remaining actionable findings after corrections. No automated tests or dependency installations were introduced. The user subsequently authorized committing this ticket before implementing ticket 03.
