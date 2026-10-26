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
