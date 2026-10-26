# Ticket 01: Implementation Evidence and Gaps

## Scope

The initial orientation slice provides `init-study`, `to-map`, shared workspace instructions, an orientation document format, a versioned JSON Schema, and default Git exclusion for private study data. It does not provide the remaining six methods or full review scheduling.

The repository has no commits or valid `HEAD`; reviews therefore examined the explicitly scoped new implementation files rather than a commit diff. Existing development skills and personal materials were not altered. No automated tests were created, no dependencies installed, and no commits made.

## Observed evidence

| Inspection | Observed result | What it does not establish |
| --- | --- | --- |
| OpenCode's live skill catalog after file creation | Both `init-study` and `to-map` appeared with their descriptions | Execution of a learner session or support in other agents |
| Python standard-library JSON parsing | The shared schema parses as JSON | Full JSON Schema conformance or validation of learner state instances |
| Recursive inspection of schema references | All 66 local references resolve | Cross-record semantic invariants or behavior of an agent |
| Pattern compilation during structural inspection | All 8 schema patterns compile in Python | Equivalent behavior across every JSON Schema implementation |
| Markdown reference inspection | All bundled links from the two skills and workspace contract resolve | Correct installation after copying only part of the bundle |
| Frontmatter inspection | Both skills start with frontmatter containing matching names and descriptions | Every target agent's parser behavior |
| `git check-ignore --no-index` on representative default source, state, and generated paths | All three paths are ignored by the repository rule | Protection of already-tracked data or arbitrary custom locations |
| Available validator inspection | Python `jsonschema` is not installed | A machine-validated schema or state instance; none is claimed |

These were structural inspections, not an automated test suite. No synthetic learner history was presented as real progress.

## Review and corrections

Separate read-only Standards and Spec reviews were performed under the code-review workflow.

### Standards

- Removed repeated orientation-format requirements from the method procedure; the format reference is authoritative.
- Clarified initialization prerequisites: a known main topic, objective, and language allow initialization without a specific topic. An unknown objective must be requested, not invented.

### Spec

- Added an authoritative per-topic checkpoint, selected through a lightweight current-topic pointer. Switching topics preserves and restores each topic's activity, mode, pending prompt, status, and next action without reconstructing narrative history.
- Added explicit completed-map resumption branches: reuse a valid existing artifact unless a revision or changed source scope is requested.
- Recorded the observed evidence and remaining gaps in this document rather than treating written instructions as demonstrated learner behavior.

## Acceptance mapping

- Main-topic initialization, topic selection, progressive intake, and source preparation are specified in `init-study` and the shared contract.
- Standalone mapping uses the same reference bundle and data contract without requiring the orchestrator to be installed.
- The JSON schema represents stable identifiers, per-topic checkpoints, seven step statuses, source records, concept inventory, artifacts, and append-only history; future questions, attempts, learning records, and review history are reserved explicitly.
- Privacy guidance covers the ignored default workspace, custom-workspace ignore files, and already-tracked data as a blocker requiring learner action.
- The release boundary is explicit: a completed orientation does not complete a cycle, enroll a topic, assess concepts, or create a due date.
- Preservation and recovery rules specify snapshots, nonoverwriting outputs, revision checks, actual source access, blocked inputs, and permission failures.

This mapping identifies implementation coverage, not successful execution of the corresponding learner scenarios.

## Still unverified

- Real interactive initialization and standalone mapping from supplied study materials.
- Pause/resume behavior, unavailable-source handling, and A → B → A topic switching in a learner session.
- Cross-agent resumption, host-specific activation, permission prompts, and installation mappings.
- Full JSON Schema meta-validation and learner-state instance validation with a dedicated validator.
- Effective privacy checks for a custom learner workspace, existing tracked files, and non-Git workspaces.
- Atomic save and recovery behavior in the actual host filesystem tools.

The implementation is instruction-based, not a deterministic runtime enforcing every invariant. Agents must follow the documented checks; do not describe structural inspection as proof of end-to-end reliability. Integration tickets remain responsible for distinguishing documentation-supported routes from behavior actually exercised.
