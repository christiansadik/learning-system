# Install with the Standard Skills CLI

Run from the project where you want to study, using Node.js 22.20+ with the current [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add christiansadik/learning-system
```

Select the desired skills and coding agents. Choose **all eight skills** for the complete flow, or just a method for standalone use. Each published skill contains `SKILL.md`, ten reference files, and `LICENSE`; there is no sibling-folder dependency or Python requirement for normal installation.

The repository shorthand downloads the published repository, not your uncommitted local work. It requires the generated `skills/` packages to be committed and pushed first. Until that is authorized and done, use the local checkout route below. No GitHub-download installation of the new packaging is claimed yet.

## Common commands

```sh
# Inspect available skills without installing
npx skills add christiansadik/learning-system --list

# Full flow for OpenCode
npx skills add christiansadik/learning-system --skill '*' --agent opencode

# One self-contained skill for Claude Code
npx skills add christiansadik/learning-system --skill to-docs --agent claude-code

# Personal rather than project scope
npx skills add christiansadik/learning-system --global
```

The documented target IDs are `opencode`, `codex`, `github-copilot`, `claude-code`, `gemini-cli`, `cursor`, and `pi`. Select agents interactively or through `--agent`; installation does not install those agents or authenticate a provider. Native skill/file-access consent remains in force.

Skills CLI defaults to canonical installation with agent-specific links where applicable; `--copy` requests ordinary copied files. References and the license remain inside each skill in either mode. This project's former no-overwrite Python policy is **not** a guarantee about the third-party CLI: inspect its prompts and back up skill customizations before replacement or update. Do not pass broad unattended flags to an unfamiliar destination merely to silence prompts.

## Local checkout and maintainer workflow

```sh
npx skills add /path/to/learning-system/skills --list
npx skills add /path/to/learning-system/skills --skill to-docs --agent claude-code
```

Use the explicit `skills` directory for local development so discovery does not pick up unrelated local `.agents/skills` tooling. Repository downloads include only tracked source/distribution files, not ignored local tools.

Authoritative content lives in `authoring/skills/<name>.md` and `authoring/references/`; those templates are deliberately not named `SKILL.md`. The committed `skills/<name>/` packages are generated from [`skill-bundle.json`](../../skill-bundle.json):

```sh
python3 scripts/build_skills.py          # preview
python3 scripts/build_skills.py --write  # regenerate
python3 scripts/build_skills.py --check  # read-only reproducibility/link check
```

Maintainer generation requires Python 3.9+. Every package is self-contained; the generated build receipt records prior file hashes to protect hand-edited output. Changed/unknown files, symlinks, or obsolete generated paths require explicit review rather than automatic deletion. Per-file writes are atomic where supported, but a build is not a concurrent-writer/security boundary or a whole-directory transaction. Preserve and inspect partial artifacts after an interrupted build.

## Conservative Python fallback

For an explicit copy destination and no-overwrite behavior, run from a full checkout:

```sh
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --skill to-docs
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --skill to-docs --apply
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --skill to-docs --check
```

Omit `--skill` for all eight packages; repeat it for a selection. Use `.claude/skills` for the manual Claude Code route. This fallback validates the published packages against canonical sources, includes the internal references/license, and refuses differing existing files, symlinked paths, or unknown files inside selected directories. Preview does not write. Exclusive creation protects existing files; an interrupted copy may require explicit preservation/recovery. It never silently removes an old `_study` folder or unrelated installed skills.

## Upgrading from the old sibling-reference layout

The old layout used a shared `_study` folder next to skills. The new packages put resources in each skill's `references/` and `LICENSE`. Back up any custom skill changes before replacing only the selected old skill directories. Do not delete the whole agent skills directory, other local tools, or your learning workspace. Leave an old `_study` folder untouched unless you explicitly confirm it is no longer needed.

This changes packaging only: learner state remains at contract 1.6.0 in the same explicitly selected workspace. There is no need to move sources, answers, due dates, or snapshots into the installed skill folder.

## Switching agents and assurance

Finish the current save and pause the first agent, then invoke `init-study` in the next agent against the same project and explicit learning workspace. Persistent topic IDs, prompts, answers, schedules, and navigation—not chat history—are authoritative. Use agents sequentially; concurrent writers are unsupported. See [per-agent guidance](additional-agents.md) and [evidence](evidence.md).

Local CLI discovery/full-copy and single-skill-copy installation were exercised with Skills 1.7.4. These are packaging observations, not proof of actual teaching, state migration, or cross-agent learner handoff. No agent applications, credentials, model requests, learner data, or automated test suite were created. Keep private `study/` data out of public packages.
