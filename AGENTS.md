# Project Instructions

Build portable study skills with shared learning state.
Keep agent-specific integration separate from the study methodology.

## Working rules

- Preserve original study materials and existing user work.
- Create tests only when explicitly requested.
- Commit and push only when explicitly requested.
- Never commit personal study materials or learning records
  without explicit approval.
- Document verified agent support separately from planned support.

## Skill packaging

Edit canonical templates in `authoring/skills/` and shared contracts in
`authoring/references/`. `skills/` contains generated, self-contained packages
for standard Agent Skills installers; never maintain their contents by hand.
Preview changes with `python3 scripts/build_skills.py`, regenerate with
`--write`, and inspect reproducibility with `--check`. Keep learner data and
local `.agents/skills` installations outside the published source tree.

## Commit messages

Follow [Baeldung's commit message guidelines](https://www.baeldung.com/ops/git-commit-messages).

- Write messages in English using Conventional Commits:
  `<type>(optional scope): <subject-description>`.
- Use the imperative mood and keep the entire subject within 50 characters.
- Separate the subject, optional body, and optional footer with blank lines.
- Explain what changed and why when a body is needed; wrap it at 72 characters.
- Include issue references and breaking-change notices when applicable.
- Omit `Co-authored-by` trailers and other co-author attribution.

## Agent skills

### Issue tracker

Specs and tickets use local Markdown files.
See `docs/agents/issue-tracker.md`.

### Triage labels

Use canonical triage roles separately from implementation lifecycle status.
See `docs/agents/triage-labels.md`.

### Domain docs

Use a single-context glossary and optional ADRs.
See `docs/agents/domain.md`.
