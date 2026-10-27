# Install the Study Bundle

Requires Python 3.9 or newer. Run the installer from this repository's checkout. It installs skill definitions, not an agent application, credentials, models, or learning data.

The canonical source is the allowlist in [`skill-bundle.json`](../../skill-bundle.json). `_study` is a required sibling reference directory, not a ninth skill. Do not install a lone `SKILL.md` or use a per-skill marketplace installer that drops sibling references. This release uses local filesystem installation, not marketplace/plugin packaging.

The full bundle has 19 files, including `_study/LICENSE.md`; individual selections also include that MIT notice. The installer verifies that the notice matches the canonical repository `LICENSE`. Preserve it when redistributing installed skills. An older installation without the notice can add it without replacing already-identical files; the usual conflict protections still apply.

## Project installation

For the documented OpenCode V2, Codex CLI/IDE, and Copilot CLI routes, choose the study project's `.agents/skills` directory:

```sh
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --apply
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --check
```

The first command previews; only `--apply` writes. Start the agent in that project and grant normal file access/trust for its study workspace and bundled references. Installation does not preapprove tools, bypass native activation consent, or edit host configuration.

## Personal installation

The same three documented agents accept a user-level `.agents/skills` location:

```sh
python3 scripts/install_skills.py --target "$HOME/.agents/skills" --apply
```

Use project scope first to avoid shadowing skills across unrelated projects. Keep only intended versions visible: hosts resolve duplicate names differently. Personal skill installation does not put learner state in the home skills directory; explicitly select the same learning workspace when switching agents.

## Other discovery roots

Gemini CLI, Cursor local Agent chat, and Pi also document `.agents/skills` for project use. Claude Code's local terminal route uses `.claude/skills`; pass that directory as `--target` to the same installer. It copies the same selected files and references, not an adapted teaching implementation. See [additional-agent guidance](additional-agents.md) for native invocation, trust, lifetime, and local/cloud limitations. This installer deliberately does not create symlink mappings or silently edit host settings.

## One method or the whole flow

```sh
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --skill to-docs --apply
```

Repeat `--skill` to select multiple methods. All shared references are included because they reference each other. Independent methods do not require predecessor skills, but `init-study` needs all seven component methods for the complete flow. Missing methods must remain visible blockers, never simulated successes.

## Preservation, updates, and interruptions

- The installer only considers explicitly listed skill directories and `_study`; unrelated directories/configuration remain untouched.
- Existing identical files are reused. Different content, symlinks, unexpected files inside managed directories, or unsafe destinations stop installation before copying. There is no force-overwrite option.
- To update, preview and inspect differences first. Preserve your modified/old bundle separately, then explicitly choose a clean installation location or move only the old managed directories after review. Do not mix shared-reference versions or broadly delete a skills directory.
- Exclusive file creation avoids overwriting files that appear after preflight. Installation is not a filesystem transaction or hardened concurrent-writer boundary. If interrupted, inspect partial files; rerunning fills missing files only when existing bytes match. A partial/different file requires explicit preservation/recovery, not automatic deletion.
- `--check` verifies selected installed bytes and local references, not agent activation or study behavior. A matching installation is not an end-to-end compatibility result.
- Copying references outside each individual skill folder requires ordinary read permission on `_study`. Hosts do not necessarily attach supporting file contents automatically.

## Switching agents

Finish the current file save, close or pause the first agent, and start the next against the same project and explicit workspace root. Invoke `init-study` using that host's syntax and ask to resume that workspace. Its persisted topic IDs, source records, prompts, answers, schedules, and navigation are authoritative; chat history is not required. Sequential switching is intended; concurrent writers are not supported.

Do not copy a real workspace into the public skill bundle. Keep the default `study/` excluded and follow custom-workspace privacy checks.
