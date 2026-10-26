# 09: Use the Workflow in Four Additional Agents

**What to build:** A learner can use the shared study workflow in Claude Code, Gemini CLI, Cursor, and Pi through documented installation and invocation routes that preserve common learning state.

**Blocked by:** 07 — Run and Resume the Complete Study Flow.

**Status:** done

## Context

Read the [source specification](../spec.md) and [compatibility findings](../compatibility-notes.md). This ticket can proceed independently of ticket 08 after the full workflow exists. Recheck primary documentation before applying configuration details.

## Acceptance criteria

- [x] Provide minimal installation and invocation routes for Claude Code local terminal, Gemini CLI, Cursor local Agent chat, and the Pi coding agent.
- [x] Reuse the canonical methods and workspace contract; avoid separately maintained copies of the study methodology.
- [x] Claude Code uses a documented discovery route, preserving supporting references if symlinks or other installation mappings are selected.
- [x] Gemini CLI guidance respects native activation consent, workspace trust, and natural-language requests rather than assuming a universal skill slash command.
- [x] Gemini product and access limitations, including any relevant migration notice, are checked and documented without silently replacing the requested target with another product.
- [x] Cursor guidance distinguishes message-level invocation from session persistence and does not imply local skills automatically exist in remote or cloud environments.
- [x] Pi guidance documents its native skill invocation and relevant reload or trust requirements.
- [ ] Sequential agent switching preserves the same pending activity, topic identifiers, and quiz history.
- [x] Each compatibility entry distinguishes primary-documentation evidence from exercised behavior and identifies version/environment when exercised.
- [x] Missing agents, permissions, or credentials remain explicit verification gaps. No compatibility success is fabricated.
- [x] Installation preserves unrelated configuration, installed skills, and personal data.
- [x] Do not generate automated tests, install agent software, authenticate services, create commits, or publish anything without the applicable explicit authorization.

## Outcome and verification gap

Documented integrations and native copy layouts are implemented. See [verification-09.md](../verification-09.md). Both independent review axes found no actionable implementation defects. The actual sequential handoff criterion remains unchecked, and native teaching behavior is unverified in these four agents. The user authorized this commit before ticket 10; no software installation, login, model prompt, automated tests, push, or public publication was performed.
