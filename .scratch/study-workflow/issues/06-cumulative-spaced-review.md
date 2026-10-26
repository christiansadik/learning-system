# 06: Review Cumulatively and Track Progress

**What to build:** An enrolled learner can invoke `to-review`, complete a cumulative quiz across previously studied topics, inspect per-topic results and concept coverage, and receive an updated review schedule with targeted recommendations.

**Blocked by:** 02 — Practice with Flashcards and Quizzes.

**Status:** done

## Context

Read the [source specification](../spec.md), project glossary, and the shared topic, concept, question, and attempt contracts delivered by tickets 01 and 02. Full-flow enrollment is connected in ticket 07; this ticket must define an explicit standalone enrollment route without pretending that unfinished study is complete.

## Acceptance criteria

- [x] `to-review` operates independently over explicitly enrolled topics and preserves completion, eligibility, and mastery as different states.
- [x] First review is due three days after initial cycle completion. The subsequent default intervals use one week and one month, with exact anchors and adaptive rules documented explicitly.
- [x] Review dates persist across sessions. Weak performance brings a topic back sooner, while stronger performance may permit longer intervals according to the documented policy.
- [x] Default cumulative quizzes contain ten questions, five choices each, with corrections and source-grounded explanations withheld until completion.
- [x] Due and difficult topics receive priority while concept coverage grows over successive quizzes; not every topic must appear in every quiz.
- [x] Each question has one primary specific topic and concept for unambiguous score attribution, with repeat detection and comparable difficulty where practical.
- [x] Limited source material does not lead to unsupported questions or an unqualified promise of unlimited novelty.
- [x] History retains questions, learner answers, evaluations, dates, and concept associations; interrupted attempts remain separate from completed scores.
- [x] Results show correct/evaluated counts and percentages per specific topic, distinguish latest results from historical aggregates, and avoid unweighted averaging of topic percentages.
- [x] Coverage is reported separately against the documented concept inventory, with untested concepts and incomplete inventories visible.
- [x] Correctness strictly below 80% recommends review. Strictly below 50% on a fundamental concept additionally recommends deeper study. Boundary scores and small samples are represented honestly.
- [x] Fundamental status is decided contextually by the agent with a short, revisable rationale, using study objectives and prerequisites rather than stack labels alone.
- [x] No background execution, automatic notification, or proof of durable mastery is implied.
- [x] Document observable acceptance evidence and remaining gaps; do not create automated tests or Git commits without explicit authorization.

## Outcome

Implemented as instructions and a versioned shared-state contract. Checked criteria indicate implementation coverage, not exercised learner sessions. See [evidence and gaps](../verification-06.md). Final Standards and Spec reviews found no residual actionable issues. The user authorized this commit before implementation of ticket 07; no tests or push were authorized.
