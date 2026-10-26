# 03: Explore Questions and Study with Socrates

**What to build:** A learner can formulate their own questions with `to-question` and practice reasoning through an adaptive, one-question-at-a-time dialogue with `socrate`. Either activity can be suspended and resumed.

**Blocked by:** 01 — Start and Resume a Study Topic.

**Status:** done

## Context

Read the [source specification](../spec.md), project glossary, and shared workspace contract. These are two distinct standalone skills within one coherent dialogue slice; neither simulates the learner's contributions.

## Acceptance criteria

- [x] `to-question` helps the learner formulate why-questions, comparisons, and counterfactuals while waiting for the learner's own questions and reasoning.
- [x] Answers and supported connections are grounded in the selected material; authorized additions remain distinguishable.
- [x] `socrate` asks exactly one question at a time and waits for the learner before continuing.
- [x] Errors lead first to simpler guiding questions rather than immediately supplied solutions; successful reasoning allows increasing difficulty.
- [x] Feedback identifies the relevant specific topic and concepts, recording useful gaps and insights without inventing learner responses.
- [x] Persisted activity identifies the pending question or next action so a fresh session can resume accurately.
- [x] Both skills remain independently callable and suitable for subjects beyond programming.
- [x] The learner can explicitly stop or skip; an unfinished dialogue is not silently treated as completed mastery.
- [x] Document observable acceptance evidence and remaining gaps; do not create automated tests or Git commits without explicit authorization.

## Outcome

Implemented as instructions and a versioned state contract. Checked criteria indicate implementation coverage, not exercised learner sessions. See [evidence and gaps](../verification-03.md). The user authorized this ticket's commit as part of the requested sequence; no tests or push were authorized.
