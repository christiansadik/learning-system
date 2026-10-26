# 07: Run and Resume the Complete Study Flow

**What to build:** `init-study` guides the learner through all seven methods for progressively supplied specific topics, waits for real learner input, and enrolls completed topics for future cumulative reviews while preserving the entire workflow across sessions.

**Blocked by:** 01 — Start and Resume a Study Topic; 02 — Practice with Flashcards and Quizzes; 03 — Explore Questions and Study with Socrates; 04 — Find Gaps in the Learner's Explanation; 05 — Export a Concept Map and Explanation; 06 — Review Cumulatively and Track Progress.

**Status:** done

## Context

Read the [source specification](../spec.md), [compatibility findings](../compatibility-notes.md), project glossary, and implemented shared contracts and skills. Reuse each method's authoritative instructions rather than duplicating them inside the orchestrator.

## Acceptance criteria

- [x] The orchestrator coordinates `to-map`, `to-drill`, `to-question`, `socrate`, `feynman`, `to-docs`, and deferred `to-review` through explicit lifecycle transitions.
- [x] A learner retains the main topic and objective while supplying each new specific topic and its materials progressively.
- [x] Source preparation happens before study; inaccessible sources and missing permissions are handled visibly rather than bypassed.
- [x] Questions, Socratic answers, explanations, and other learner-dependent actions pause execution until real input arrives.
- [x] Explicit learner skips or justified inapplicability are recorded separately from completion and interruption.
- [x] Initial cycle completion enrolls the topic even when gaps remain, schedules the first spaced review after three days, and does not launch an immediate cumulative test.
- [x] On startup or resumption, due reviews are shown and offered before new study; the learner chooses whether to take them.
- [x] A fresh agent session can resume the correct topic, pending activity, and next action using shared files without private agent memory.
- [x] Standalone skill use updates shared state consistently without falsely completing unrelated workflow steps or corrupting schedules.
- [x] `to-docs` defaults to the current specific topic while retaining its independent multi-topic capability.
- [x] All seven component skills remain independently callable. The existing `teach` skill is unchanged.
- [x] Document observable acceptance evidence and remaining gaps; do not create automated tests or Git commits without explicit authorization.

## Outcome

Implemented as an interactive agent-driven controller and versioned state contract. Checked criteria indicate authored behavior and structural implementation coverage, not executed learner scenarios. See [evidence and gaps](../verification-07.md). Final independent Standards and Spec reviews found no residual actionable issues. The user authorized this ticket's commit; no tests or push were authorized.
