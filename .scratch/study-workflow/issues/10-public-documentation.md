# 10: Document and Prepare the Public Workflow

**What to build:** A prospective user can understand and install the study workflow from an English README, follow realistic examples, interpret progress metrics, and identify actual compatibility and limitations without receiving personal study data or unrelated development skills.

**Blocked by:** 08 — Use the Workflow in the Three Priority Agents; 09 — Use the Workflow in Four Additional Agents.

**Status:** done

## Context

Read the [source specification](../spec.md), [compatibility findings](../compatibility-notes.md), implementation decisions, and integration evidence. Public GitHub publication is intended but not yet authorized as an operation.

## Acceptance criteria

- [x] An English README explains the workflow's purpose, active-learning principle, eight skills, and their standalone and orchestrated use.
- [x] Installation and invocation instructions cover all seven targets with support accurately labeled as documentation-confirmed, exercised, or still limited.
- [x] Explain the final shared workspace structure, original/generated/progress separation, required references, and safe installation of individual skills versus the complete workflow.
- [x] Examples show main-topic initialization, progressive specific-topic study, interruption and cross-agent resumption, due-review choice, and multi-topic document export.
- [x] Explain first-review timing, later interval anchors, adaptive scheduling, and the absence of autonomous notifications or background execution.
- [x] Explain cumulative quiz defaults, correction timing, history, per-topic correctness, coverage, sample-size limitations, and review/deeper-study thresholds.
- [x] Explain contextual fundamental-concept classification and why study-cycle completion is not proof of mastery.
- [x] Document source access limitations, authorized external additions, third-party media export, and the unchanged role of the existing `teach` skill.
- [x] Credit the source video and describe the intentional replacement of photography with document export without repeating unsupported speed or outcome claims.
- [x] Use clearly synthetic examples rather than learner materials or real learning records.
- [x] Define the public deliverable boundary and safeguards so unrelated preinstalled skills, credentials, and personal study data are not inadvertently included.
- [x] Leave any license decision requiring owner approval explicit; do not assume the right to redistribute unrelated installed material.
- [x] Keep documentation consistent with implemented behavior and unresolved compatibility limitations.
- [x] Do not create automated tests, commits, remotes, pushes, or a public repository without explicit authorization.

## Outcome

English public documentation, installation guidance, synthetic examples, publication boundaries, and privacy/tooling ignore rules are implemented. See [verification-10.md](../verification-10.md). Independent review axes reported no residual actionable findings. Actual learner flows/handoffs and schema-instance validation remain unverified; license and GitHub publication remain owner decisions. The user authorized this commit only, not a remote, push, public repository, or tests.
