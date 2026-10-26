# Integration Evidence

Observed on 2026-10-26, macOS. This page is the authority for local verification claims; product documentation is cited in the per-agent guides. None of these observations establishes an end-to-end learner session or a successful cross-agent handoff.

| Environment | Documentation route | Local evidence | Not exercised |
| --- | --- | --- | --- |
| OpenCode V2 | Confirmed | 2.0.32: all eight skills advertised; native `init-study` and `to-map` loading succeeded | Full teaching flow, migrations, quiz behavior, relocation in another OpenCode session, cross-agent handoff |
| Codex CLI / IDE | Confirmed | CLI not on PATH | Native discovery/activation, IDE behavior, handoff |
| Copilot CLI | Confirmed | 1.0.90: all eight enabled skill metadata entries discovered in both the current project and a fresh relocated bundle | Model activation, teaching/quiz execution, handoff; editor/cloud surfaces are not covered |

## Installer and reference observations

- Python syntax parsed without executing a learner flow or generating bytecode/test files.
- Read-only `--check` matched all 18 selected source bundle files.
- In a fresh disposable project outside the repository, preview reported 18 missing files, apply created those files, and check verified identical installed bytes and resolvable references.
- Copilot CLI's noninteractive skill list identified all eight enabled skills from that relocated project. Unrelated global skills were filtered out of the observation.
- No agent application was installed or updated. No model prompt, authentication flow, learner source, learning record, test suite, or scheduled/background task was created.

## Known verification gaps

The shared state contract is designed for sequential switching, but real learner-state handoff has not been demonstrated. An executable on PATH, parsed skill metadata, or matching copied files is not proof of agent interpretation, permission handling, persistence, scoring, or recovery. Unavailable agents/credentials must remain gaps rather than recorded successes.

Practical continuation requires the learner to use an authorized agent session against the same explicit workspace, permit native skill/reference access, and inspect the saved pending prompt before answering. Schema-instance validation and behavioral evaluation remain separate from this installation evidence. No automated tests were authorized or generated.
