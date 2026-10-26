# Ticket 04: Evidence and Limitations

Baseline: ticket 03 commit `345daa1`. Scope: `feynman`, categorized explanation feedback, contextual fundamental classification, and consent-based upgrade to state 1.3.0.

## Observed structural evidence

- OpenCode advertised `feynman` after creation.
- The schema parsed as JSON; all 138 local references resolved and patterns compiled.
- All 28 inspected bundled Markdown links resolved; six skill frontmatters had matching names and descriptions.
- Independent Standards and Spec reviews reported no actionable findings. Reviews were read-only and structural, not demonstrations of agent behavior.

## Implementation coverage

The method waits for actual learner explanations and preserves each revision as a separate turn. Feedback distinguishes factual errors, missing concepts, unclear wording, and supported connections, with source evidence. Session summaries and unresolved gaps remain separate from explanatory exports and quiz metrics.

The agent can classify prerequisites autonomously relative to the main topic/objective, with nonempty rationale and explicit evidence limitations. Changes preserve previous classifications in history. New maps still initialize new concepts as unclassified; classification does not assess or master a concept.

Shared session rules handle pending feedback, interruption, switching topics, abandonment, skips, and explicit completion. Legacy migration preserves earlier attempts/sessions and does not fabricate learner explanations or classifications.

## Verification gaps

Real explanations, revision/clarification behavior, source reading, contextual classification, migration/recovery, and cross-agent resumption remain unexercised. Dedicated JSON Schema meta-validation and state-instance validation remain unavailable in the inspected environment. No automated tests, dependencies, or synthetic learner progress were generated. Checked ticket criteria indicate implementation coverage, not successful end-to-end learning sessions.
