# Integration Evidence

Observed on 2026-10-26, macOS. This page is the authority for local verification claims; product documentation is cited in the per-agent guides. None of these observations establishes an end-to-end learner session or a successful cross-agent handoff.

| Environment | Documentation route | Local evidence | Not exercised |
| --- | --- | --- | --- |
| OpenCode V2 | Confirmed | 2.0.32: all eight skills advertised; native `init-study` and `to-map` loading succeeded | Full teaching flow, migrations, quiz behavior, relocation in another OpenCode session, cross-agent handoff |
| Codex CLI / IDE | Confirmed | CLI not on PATH | Native discovery/activation, IDE behavior, handoff |
| Copilot CLI | Confirmed | 1.0.90: all eight enabled skill metadata entries discovered in both the current project and a fresh relocated bundle | Model activation, teaching/quiz execution, handoff; editor/cloud surfaces are not covered |
| Claude Code local terminal | Confirmed | 2.1.161 version command only; the native `.claude/skills` copy layout was inspected separately | Native discovery/activation, teaching, handoff; cloud/account-synced surfaces are not covered |
| Gemini CLI | Confirmed, subject to product/account availability | CLI not on PATH | Trust/activation/teaching; Antigravity is not a substituted target |
| Cursor local Agent chat | Confirmed | `cursor` and `agent` CLIs not on PATH; editor state not inspected | UI discovery, message/Custom Mode behavior, teaching, remote/cloud scope |
| Pi coding agent | Confirmed | CLI not on PATH | Native discovery/commands, teaching, handoff |

## Installer and reference observations

- Python syntax parsed without executing a learner flow or generating bytecode/test files.
- Read-only `--check` matched all 18 selected source bundle files.
- In a fresh disposable project outside the repository, preview reported 18 missing files, apply created those files, and check verified identical installed bytes and resolvable references.
- Copilot CLI's noninteractive skill list identified all eight enabled skills from that relocated project. Unrelated global skills were filtered out of the observation.
- The same installer copied and checked 18 files in a separate fresh `.claude/skills` layout, and an independent `to-docs` selection retained its 11 required files. These are filesystem/reference observations, not native Claude activation.
- No agent application was installed or updated. No model prompt, authentication flow, learner source, learning record, test suite, or scheduled/background task was created.

## License packaging update — 2026-10-27

MIT licensing was added after the initial observations above. At that stage the allowlist contained 19 files, including `_study/LICENSE.md`, rather than the original 18. The installer verified that the bundled notice matched the canonical root `LICENSE`; its read-only check matched those 19 source files. These counts describe the former sibling-reference layout, not the current packages. No additional agent activation or learner behavior was exercised for that update.

## Standard self-contained packaging — 2026-10-27

- Canonical authoring moved outside skill discovery; eight generated `skills/<name>/` packages each include `SKILL.md`, ten reference files, and `LICENSE`. The reproducibility check matched all 96 package files and the build receipt.
- Skills CLI **1.7.4**, run through `npx` with Node.js 24.21.0, discovered exactly eight skills in a clean local source containing both `authoring/` and `skills/`.
- A project-scoped `--copy` installation of all eight skills for `opencode` preserved all expected package bytes, internal references, and license notices.
- A separate `--copy` installation of only `to-docs` for `claude-code` preserved its complete 12-file package; no sibling `_study` directory was needed.
- Default installation of `to-docs` accepted all seven documented target-agent IDs. Its canonical package matched all 12 files and the created agent link resolved to that package. Shared canonical locations mean this did not create seven separate directory copies.
- Inspections used disposable local projects, not learner workspaces. Telemetry was disabled; no agent application, model session, login, automated test suite, commit, or push was launched by these packaging checks.

These observations exercise the standard installer, not native teaching or handoff. At initial local inspection, the new packages had not yet been published; the subsequent GitHub discovery check is recorded below. Earlier native-loader observations are historical and have not been repeated for this new packaging.

## Published repository discovery — 2026-10-27

After the owner authorized commit/push, packaging commit `545c2d7` was published to `master`. The remote default branch resolved to that same commit. In a separate disposable directory, Skills CLI 1.7.4 successfully downloaded `christiansadik/learning-system` through the repository shorthand and reported exactly eight available skills. No installation into a real learner project or agent model session was launched by this discovery check. Remote download/discovery is verified; teaching behavior and cross-device learner-state handoff remain unverified.

## Known verification gaps

The shared state contract is designed for sequential switching, but real learner-state handoff has not been demonstrated. An executable on PATH, parsed skill metadata, or matching copied files is not proof of agent interpretation, permission handling, persistence, scoring, or recovery. Unavailable agents/credentials must remain gaps rather than recorded successes.

Practical continuation requires the learner to use an authorized agent session against the same explicit workspace, permit native skill/reference access, and inspect the saved pending prompt before answering. Schema-instance validation and behavioral evaluation remain separate from this installation evidence. No automated tests were authorized or generated.
