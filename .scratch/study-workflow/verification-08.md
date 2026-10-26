# Ticket 08: Evidence and Limitations

Baseline: ticket 07 commit `f52a88e`. Deliverables: an explicit bundle/file allowlist, a standard-library installer with preview/apply/check modes, shared installation guidance, and documented OpenCode V2, Codex local, and Copilot CLI routes.

## Observed

- Current primary documentation was retrieved through Context7 and direct official pages.
- Local versions: OpenCode 2.0.32 and Copilot CLI 1.0.90. Codex was not on PATH.
- OpenCode native loading returned the expected `init-study` and `to-map` definitions/base directories.
- Copilot's metadata listing found all eight workflow skills enabled in the original project and a fresh relocated 18-file installation.
- Installer syntax and copied-reference/byte integrity were inspected. No learner state or automated tests were generated.

The public [integration evidence](../../docs/integrations/evidence.md) records the exact assurance boundary without machine-specific paths or unrelated skill metadata.

Independent Standards and Spec reviews found no actionable implementation defects. The Spec review explicitly retained real learner-state handoff as an unverified acceptance gap rather than calling metadata discovery a behavioral pass.

## Gaps

Codex execution and real sequential learner-state handoff are unverified. Neither native definition loading nor Copilot metadata discovery demonstrates teaching, quiz correction, permission decisions, or schema migration. No agent software installation, authentication change, model prompt, push, or public repository creation was performed.
