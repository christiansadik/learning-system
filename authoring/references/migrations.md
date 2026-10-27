# Study State Migrations

Read [workspace.md](workspace.md) and [state.schema.json](state.schema.json). Older supported versions are read-only until upgraded. Preserve unknown, malformed, or inconsistent state as a blocker; never reset it to make migration succeed.

## Procedure

Explain the version chain and changes, then obtain explicit learner consent. A single consent may cover the full described chain. If declined, leave the state unchanged and explain that the installed release cannot update it.

For each transition, follow the workspace save protocol: inspect legacy structure and semantic invariants, check revision, snapshot the exact old bytes, transform only documented fields, increment revision once, update the actual timestamp, and append migration history. Preserve IDs, sources, artifacts, answers, observations, prompts, completed steps, and all unrelated work. Inspect the result before saving. Do not overwrite existing snapshots or silently repeat a partially completed transition; reconcile observed files first. Never downgrade populated state for an older reader.

## 1.0.0 → 1.1.0

- Set `schema_version` to `1.1.0` before inspecting and saving the transformed state.
- Add `active_attempt_id: null` to every checkpoint and `question_ids: []` to existing orientation artifacts. Questions and attempts remain empty.
- Make the installed `to-drill` step pending if previously unavailable, clearing the unavailable reason. Unexpected prior step states require reconciliation, not guessing.
- A checkpoint blocked solely at missing `to-drill` may become an offer to activate it. Preserve all other activities/prompts.
- Keep review eligibility false and enrollment/due dates null.

## 1.1.0 → 1.2.0

- Set `schema_version` to `1.2.0` before inspecting and saving the transformed state.
- Add `active_session_id: null` to every checkpoint. Keep existing active practice attempt IDs and their prompts unchanged.
- `learning_records` remains empty until a real dialogue starts. No turns, observations, summaries, or learner contributions are invented.
- For installed `to-question` and `socrate`, change unavailable steps to pending and clear their unavailable reasons. Preserve other states and the unavailable later methods.
- Only a checkpoint blocked solely at the newly available next method may become an offer to activate it, and only when no practice attempt is active. Do not advance an unfinished or declined activity.
- Preserve question/attempt history, concept assessment indices, cycle status, and null review dates.

## 1.2.0 → 1.3.0

- Set `schema_version` to `1.3.0`. Make installed `feynman` pending only if previously unavailable, clearing the unavailable reason.
- Existing concepts retain null fundamental status/rationale until actually classified in context. Do not retroactively reinterpret older turns or add categorized feedback to them.
- Preserve all active attempts/sessions, prompts, turns, observations, maps, and quiz evidence. Only a checkpoint blocked solely at newly available `feynman`, with no active work, may become an activation offer.
- New explanation sessions use the existing session shape with activity `feynman`; their actual observations require the documented feedback category. No record is fabricated during migration.

## 1.3.0 → 1.4.0

- Set `schema_version` to `1.4.0`, initialize `exports: []`, and add `active_export_id: null` to every checkpoint.
- Make installed `to-docs` pending only if previously unavailable, clearing its unavailable reason. Do not invent export files or artifact registrations.
- Preserve active practice/dialogues, all source scope, classification history, outputs, and quiz evidence. Only a checkpoint blocked solely at newly available `to-docs`, without active work, may become an activation offer.
- Existing artifacts retain their single-topic scope and fields. Multi-topic scope is permitted only for newly created paired export artifacts. Review enrollment and due dates remain unset.

## 1.4.0 → 1.5.0

- Set `schema_version` to `1.5.0` and initialize the persisted review-policy defaults from the review contract.
- Extend each previously unenrolled review state with `basis: null`, `study_completed_at: null`, and `stage: 0`; retain false eligibility, null enrollment/due dates, and empty history. Migration itself never enrolls a topic or invents completion.
- Add `inventory_note: null` to each topic and `in_scope: true` to existing concepts as the known inventory, retaining `inventory_complete: false`. Reconcile known scope changes explicitly rather than deleting historical concepts.
- Add `purpose: practice`, `topic_ids: [topic_id]`, `selection_note: null`, and `report_artifact_id: null` to every old attempt, preserving its ID, answers, exclusions, status, and pending work.
- Make installed `to-review` pending if previously unavailable. A checkpoint blocked solely at that method may offer standalone enrollment only when no other work is active. Preserve all other prompts, pointers, outputs, classifications, and source records.

## 1.5.0 → 1.6.0

- Set `schema_version` to `1.6.0`; initialize the empty flow navigation record from the flow contract. Do not create a pending review offer or suspended checkpoint during migration.
- Add `started_at: null` and `practice_resolution: null` to each cycle. Do not infer a historical orchestration start or invent learner participation. Actual matching completed practice may be selected later by the controller after checking its scope.
- Preserve existing cycle completion times/statuses, enrollment basis, policy, due dates, schedule outcomes, active work, prompts, source scope, and all artifacts. Migration never automatically enrolls or resets a topic.
- An explicit later `init-study` request may enter the full flow and validate existing evidence; standalone calls remain standalone and cannot retroactively complete unrelated methods.
