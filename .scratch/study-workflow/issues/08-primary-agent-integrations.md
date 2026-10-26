# 08: Use the Workflow in the Three Priority Agents

**What to build:** A learner can install, discover, invoke, and resume the same workflow in OpenCode, Codex, and GitHub Copilot CLI without maintaining different study methodologies or separate learning records.

**Blocked by:** 07 — Run and Resume the Complete Study Flow.

**Status:** done

## Context

Read the [source specification](../spec.md) and [compatibility findings](../compatibility-notes.md). Recheck current official documentation when implementing host-specific syntax. Copilot CLI findings do not establish support for every Copilot surface.

## Acceptance criteria

- [x] Provide a minimal documented installation and invocation route for OpenCode V2, Codex CLI or the documented IDE environment, and GitHub Copilot CLI.
- [x] Keep canonical study instructions and data contracts shared, with host-specific configuration isolated and unrelated existing configuration preserved.
- [x] Native skill discovery and activation respect host permissions and keep component skills reachable by the orchestrator.
- [x] Cross-skill and supporting-reference resolution work with the selected distribution layout; no developer-machine absolute paths are embedded.
- [x] Instructions distinguish installation scope, agent-specific invocation syntax, refresh requirements, and required workspace access.
- [ ] A sequential switch between available target agents preserves learner activity and history through the same workspace contract.
- [x] Report documentation-confirmed behavior separately from behavior actually exercised, including agent version and environment for exercised evidence.
- [x] Unavailable agents, credentials, or permissions are recorded as verification gaps rather than reported as passing.
- [x] Limit Copilot compatibility claims to surfaces actually investigated; do not silently promise cloud or editor support.
- [x] Installation never publishes personal study data or replaces unrelated installed skills.
- [x] Do not generate automated tests, install agent software, authenticate services, create commits, or publish anything without the applicable explicit authorization.

## Outcome and verification gap

Installation and documentation implementation is complete. Checked criteria describe implemented routes and the limited observations in [verification-08.md](../verification-08.md), not end-to-end behavior. The handoff criterion remains unchecked: no real learner-state switch was exercised and Codex was unavailable. The user authorized this ticket's commit; no software installs, authentication, model prompts, tests, push, or publication were performed.
