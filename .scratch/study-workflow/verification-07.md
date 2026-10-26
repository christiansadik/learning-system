# Ticket 07: Evidence and Limitations

Baseline: ticket 06 commit `1644986`. Scope: complete interactive orchestration, evidenced cycle gates, deferred enrollment, startup due-review navigation, suspended-checkpoint restoration, and migration to state 1.6.0. Agent-specific integrations remain later tickets.

## Observed structural evidence

- The schema parsed as JSON; all 197 local references resolved and patterns compiled.
- All 48 inspected bundled Markdown links resolved; all eight skills retained matching frontmatter names/descriptions.
- No actual full learner flow, migration, due-review excursion, source access, or cross-agent resumption was executed. No automated tests, dependencies, or synthetic learner progress were created. Dedicated JSON Schema meta/instance validation remains unverified.

## Independent review

Standards and Spec reviewers inspected the tracked diff and new flow contract separately. Corrections preserve accepted review scope before an attempt exists and preserve a previously completed review step during later initial-cycle finalization. The controller never resets a legitimate prior review artifact or clock merely because the workflow completes afterward.

Final follow-ups on both axes found no residual actionable findings. Git's tracked-diff whitespace check passed.

## Implementation coverage

`init-study` drives the six immediate methods through native activation and actual persisted progress, stopping for real learner contributions, source decisions, permissions, or pause. Generation-only drills require an actual practice attempt or an explicit practice-skip reason before full-flow progression. Standalone invocation does not inherit authorization to auto-run successors or complete unrelated steps.

Initial-cycle completion checks real artifacts, sessions, learner participation, explicit skips, and absence of active work. It enrolls review in the same safe update with first due time at completion +3 days by default; no immediate cumulative quiz occurs. Existing standalone enrollment is preserved rather than reset.

Startup review offers use a separate persisted navigation prompt. Accepted scope, original selection, and the review owner's suspended checkpoint survive interruption, including before question creation. Terminal/canceled review restores the teaching checkpoint without rolling back answers, reports, or schedules. Progressively supplied topics retain the main objective and previous learning histories.

## Remaining gaps

Actual native activation/consent behavior, learner response routing, evidence-gate enforcement, snapshots and atomic updates, enrollment arithmetic, due-choice restoration, excursion cancellation/replanning, and multi-agent continuation remain unexercised. The controller is an agent-driven instruction loop, not a deterministic runtime or background scheduler. Structural evidence and written acceptance coverage are not end-to-end verification or claims of mastery.
