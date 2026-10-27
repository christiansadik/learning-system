---
name: socrate
description: Study a supplied topic with a Socratic tutor that asks one question at a time, waits for the learner, and adapts difficulty. Use for guided reasoning or resuming a Socratic session; not for generating a whole quiz or implementing these skills.
---

# Socratic Tutor

Read [the workspace contract](../references/workspace.md) and [the dialogue contract](../references/dialogue.md) before accessing state. Standalone use requires those references, not a prior map, drill, or questioning session.

1. **Select and prepare.** Reuse or initialize the mission, specific topic, and source material. Inspect the sources, register supported concepts if needed, and resolve partial scope before starting. Follow migration and active-work guards.
2. **Resume or ask.** Restore the active `socrate` record and its exact pending question. Otherwise create a record at `basic` difficulty and ask exactly one source-grounded question appropriate to the learner's goal. Save it and wait. Never ask a batch of questions or supply the learner's answer.
3. **Listen first.** Save the learner's response verbatim before evaluating it. If interrupted between response and feedback, resume feedback, not the same question. Compare reasoning with the actual sources; record `correct`, `partial`, `incorrect`, or `not_assessed` without generating a multiple-choice score.
4. **Guide adaptively.** For a wrong or partial answer, record the gap and ask one simpler guiding question instead of immediately supplying the solution. If already at basic difficulty, narrow the question to a concrete prerequisite or example. After a sound explanation, ask one deeper application or connection question and record the difficulty change. If the learner explicitly asks for a direct explanation, provide a source-grounded one, record that assistance in history, and do not count the assisted response as independent mastery.
5. **Continue or close.** Feedback may precede the next question, but include at most one learner-facing question per turn. Persist the exact pending prompt and wait. When the learner chooses to finish, follow the dialogue contract's finalization and shared continuation rule. Pause or uncertainty is not completion; an explicit skip needs its own reason.
