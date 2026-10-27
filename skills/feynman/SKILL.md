---
name: feynman
description: Find gaps by evaluating the learner's own explanation of supplied study material, then invite a revision. Use for explain-it-back practice or resuming an explanation session; not for writing the explanation in place of the learner or implementing these skills.
license: MIT
---
<!-- Generated from authoring; run python3 scripts/build_skills.py --write after source changes. -->

# Explain It Yourself

Read [the workspace contract](references/workspace.md), [the dialogue contract](references/dialogue.md), and [the explanation contract](references/explanation.md) before accessing state. Standalone use needs these bundled references, not prior completion of another method.

1. **Select and ground.** Reuse or initialize the main topic, study objective, specific topic, sources, and source-backed concept IDs. Actually inspect readable material and obtain agreement on partial scope. Respect the active-work guard and explicit migration consent. If dictated/audio input is inaccessible, request its transcript rather than claiming to have heard it.
2. **Invite the explanation.** Start or resume a `feynman` learning session. Ask the learner to explain the selected topic in their own words to an unfamiliar peer, optionally focusing on a concept they choose. Persist the exact invitation and wait. Do not preempt them with a model explanation or fabricated transcript.
3. **Listen before judging.** Save each actual explanation or revision as a new immutable learner turn before evaluating it. If feedback was interrupted, resume from that turn instead of requesting it again. Distinguish uncertainty about what they meant from an established factual error; ask for clarification when necessary and preserve both contributions.
4. **Give specific feedback.** Apply the explanation contract's four categories, citing inspected sources and concept IDs. Recognize what is correct, identify gaps without penalizing harmless wording, and offer targeted correction or a revision prompt rather than a complete replacement explanation. Record tutor feedback linked to the learner turn and append observations; earlier gaps and explanations remain intact.
5. **Identify prerequisites.** Classify encountered concepts as fundamental or not relative to the main topic and objective through the explanation contract. Record the rationale and any source/context limitation autonomously; do not require the learner to maintain a manual prerequisite list.
6. **Revise or finish.** Invite another explanation attempt, save the pending prompt, and wait. Follow explicit completion, skip, abandonment, and summary rules in the dialogue contract. The shared continuation rule offers the next method only after the current session is finalized. Never derive a quiz percentage or long-term mastery claim from an explanation.
