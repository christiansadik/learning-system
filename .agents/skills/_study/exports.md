# Paired Study Exports

Available from shared state **1.4.0**. Read [workspace.md](workspace.md) and [state.schema.json](state.schema.json) before writing. One export request produces exactly two primary Markdown documents: a concept map and a self-contained explanation. State, snapshots, and history are internal progress metadata, not additional primary exports.

## Scope, identity, and checkpoints

Use one main-topic state per request. `topic_ids` is the explicit, nonempty, unique list of specific topics included. Default to the current specific topic only for orchestrated use; resolve a standalone multi-topic selection explicitly. Preserve topic IDs in both documents, explaining source scope and limitations for each.

Allocate main-topic-scoped export IDs `x001`, `x002`, and so on. Store records in `exports` with an `owner_topic_id` chosen from the selected topics: the current topic if included, otherwise the learner-selected first topic. Select that owner in `current.topic_id` without rewriting other topics' checkpoints. Its checkpoint points through `active_export_id` to the in-progress export, with activity `to-docs`, null attempt/session pointers, and the exact pending prompt or next generation action.

Before reserving, check every selected topic for active attempts, learning sessions, or other unfinished exports. Require those activities to finish or be explicitly abandoned through their owning method first. An unfinished export reserves all its selected topics against conflicting activity/source changes, even though only its owner checkpoint holds the pointer. Unrelated topics remain usable and retain their own checkpoints.

Each record stores selected topic/source IDs, accepted `scope_note`, mode, planned pair paths, status, timestamps, end reason, and both artifact IDs. At creation status is `in_progress`, artifact IDs/end time/reason are null. Persist planned paths before writing so an interrupted export can identify its exact partially written pair. The owner checkpoint stores `next_action: generate_documents` or an exact missing-source/scope request; the export record does not duplicate the prompt.

## Exactly two primary documents

Reserve a fresh numbered pair inside the main topic's generated area, such as `exports/x001/concept-map.md` and `exports/x001/explanation.md`. Persisted paths include the main-topic prefix and resolve inside the workspace. Use a new export ID for every requested regeneration; preserve all older files and user edits.

**Concept map** contains:

- Main topic/objective, selected specific-topic IDs/titles, actual creation time, source IDs/locators, accepted scope, and limitations.
- Readable concept hierarchy per topic, with stable existing concept IDs or newly registered source-backed IDs.
- Explicit, briefly explained relationships and supporting evidence. Keep unsupported links as open questions, not facts.
- Supported cross-topic connections, clearly separate from within-topic links. Mermaid may supplement but never replace readable text.

**Explanation** contains:

- The same declared scope and source basis, then a self-contained explanation in the learner's language for a reader without the original chat or generated files.
- Clear sections per topic, definitions, mechanisms, relevant examples, and supported connections between topics. Distinguish source-grounded illustrations from authorized external additions; do not invent examples that introduce unsupported factual claims.
- References at the precision actually inspected, explicit contradictions/uncertainties, and any missing prerequisites or omitted unreadable portions.
- A coherent narrative suitable for reuse as external podcast/video input, without claiming that audio/video has been created or uploaded.

Use explanations and citations within each file rather than making one file require the other to be understandable. Do not include learner answers, private performance history, or unrelated materials in exports unless the learner explicitly requests that disclosure.

## Safe writes, interruption, and finalization

Follow the workspace snapshot/revision protocol. Once paths are reserved, write each file only if it does not already exist. Inspect an existing planned file after interruption; reuse it only if its scope/content is verified unchanged, or ask to preserve it and start a new version. Never overwrite an incomplete file or user edits silently. Record any already-written but unregistered document as partial/orphaned work, not a completed pair.

On resumption, restore the owner and the saved export record, inspect both planned paths, and generate only a missing document after confirming the selected scope still matches. Changed scope requires explicit abandonment of the old export and a fresh pair; do not combine one old and one newly scoped file.

When both documents exist and their contents/provenance have been inspected, register two artifacts with kinds `concept_map` and `explanation`, the same export's `topic_ids`/source IDs, and `question_ids: []`. Link their IDs from the export, set its status `completed` with actual end time, and complete the owner's `to-docs` step using the map artifact as entry point; the export record links the paired explanation. Clear `active_export_id` and follow the workspace continuation rule. Do not advance other selected topics' checkpoints or mark their steps/cycles completed merely because a combined export includes them.

An interrupted finalization is reconciled idempotently from the reserved record and existing artifact registrations; do not create duplicate IDs or a third document. Until the pair is finalized, retain any previous completed `to-docs` step/artifact; the checkpoint/export tracks current generation separately. No export schedules a review, completes a study cycle, or demonstrates mastery.

On explicit abandonment, save its reason/end time, preserve files and registrations, clear the owner's export pointer, and ask whether to restart or select another activity. Preserve any previously completed export step. A pause is not abandonment. An explicit method skip additionally marks only the owner's step skipped with a reason, without inventing a completion time. Finalized export records/artifacts are immutable; corrections create a new export ID.

## Semantic checks

- Export IDs are unique; owner belongs to the selected topic IDs and all topic/source/artifact references resolve.
- Sources and concept evidence belong to the declared selected scope. Every selected topic has readable evidence or an explicitly accepted partial scope; absent topics are never silently removed.
- Exactly one map and one explanation belong to a completed export, at distinct planned paths. Artifact kinds, scope, source IDs, and paths match that export.
- An active export pointer references an in-progress export owned by that topic; it cannot coexist with an active attempt/session. No two in-progress exports overlap selected topic IDs.
- Single-topic orientation, practice, and dialogue artifacts retain their one-topic scope; only paired export artifacts accept multiple topics.
- Completion requires both artifact IDs, no end reason, and an actual end time; abandonment requires a reason. Planned paths and generated writes remain workspace-confined.
