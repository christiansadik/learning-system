# 04: Find Gaps in the Learner's Explanation

**What to build:** A learner invokes `feynman`, explains a topic in their own words, and receives source-grounded feedback on errors, omissions, clarity, and conceptual connections, with learning gaps preserved for subsequent sessions.

**Blocked by:** 01 — Start and Resume a Study Topic.

**Status:** done

## Context

Read the [source specification](../spec.md), project glossary, and shared workspace contract. The learner's explanation is the input to evaluate, not an output for the agent to fabricate.

## Acceptance criteria

- [x] `feynman` supports standalone invocation and identifies the selected specific topic and source material.
- [x] The skill waits for the learner's own explanation before evaluating it; unavailable voice transcription is handled by requesting accessible text.
- [x] Feedback distinguishes factual errors, missing concepts, unclear wording, and supported connections, citing the material at available precision.
- [x] The learner has an opportunity to revise their explanation rather than only receive a finished replacement explanation.
- [x] Persisted records preserve explanation attempts, feedback, concept associations, unresolved gaps, and the next action.
- [x] The agent autonomously identifies fundamental concepts relative to the main topic and study objective, records a brief rationale, and permits later revision.
- [x] Explanation feedback is not silently converted into multiple-choice correctness statistics or proof of mastery.
- [x] Stopping and resuming preserve the distinction between an unfinished explanation activity and an explicitly completed or skipped one.
- [x] Document observable acceptance evidence and remaining gaps; do not create automated tests or Git commits without explicit authorization.

## Outcome

Implemented as instruction-based explanation sessions and a versioned state contract. Checked criteria indicate implementation coverage, not exercised learner sessions. See [evidence and gaps](../verification-04.md). The user authorized this ticket's commit before development of ticket 05; no tests or push were authorized.
