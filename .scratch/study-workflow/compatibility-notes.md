# Agent Skills Compatibility Notes

Checked: 2026-10-26

## Evidence level

These are the initial pre-implementation findings from primary documentation, located with Context7 and read directly where available. No study skill had been implemented or exercised when this research was recorded. See `docs/integrations/evidence.md` for later implementation observations; documentation-supported discovery is not an end-to-end compatibility result.

## Common authoring baseline

- Use a directory per skill containing an exactly named `SKILL.md`.
- Start the file with YAML frontmatter containing `name` and `description`.
- Match the name to the directory using lowercase kebab-case, with at most 64 characters and a short description within 1024 characters.
- Keep method instructions independent of concrete tool names, command prefixes, and host-specific argument substitution.
- Keep component skills model-reachable so the orchestrator can activate them. Do not universally apply user-only invocation flags.
- Resolve bundled references from the skill's location and learning data from the explicitly selected workspace, not from the installation directory.
- Follow each host's actual loading mechanism. Reading a skill file is not a universal substitute for native activation, especially where activation requires consent.
- Prefer shared source material and installation mappings to duplicated, independently maintained method instructions. Determine the final packaging layout during implementation.

## Documentation findings

| Agent / environment | Documented project discovery | Explicit request | Important limitation |
| --- | --- | --- | --- |
| OpenCode V2 | `.opencode/skills`, `.claude/skills`, `.agents/skills` | `@init-study` | Skill IDs derive from paths; loading uses the native skill tool and permissions. |
| Codex CLI / IDE | `.agents/skills` from the working directory through the repository root | `$init-study` or skill selection | Description-based activation and host-specific invocation policy must remain compatible with orchestration. |
| GitHub Copilot CLI | `.github/skills`, `.claude/skills`, `.agents/skills` | `/init-study` in the prompt | These findings apply to CLI; they do not automatically establish support in VS Code or the cloud agent. |
| Claude Code local terminal | `.claude/skills` | `/init-study` | Use its documented discovery location; symlinked skill folders are supported. User-only skills cannot be assumed reachable by the orchestrator. |
| Gemini CLI | `.gemini/skills` and `.agents/skills` alias | Ask in natural language to use `init-study` | Activation uses `activate_skill` and consent, not a universally available `/init-study` command. Workspace trust may gate discovery. |
| Cursor local Agent chat | `.agents/skills`, `.cursor/skills`, and documented compatibility directories | Select `/init-study` in Agent chat | Manual attachment applies to one message; a Custom Mode has different persistence. Local discovery does not prove cloud availability. |
| Pi coding agent | `.agents/skills` and native skill locations | `/skill:init-study` | Loading and reload behavior are host-specific; project trust and file permissions still apply. |

Six of these documented environments accept `.agents/skills`; Claude Code has a documented `.claude/skills` route. This suggests a common installation baseline, not a reason to create seven separate copies of the workflow.

## Sources

- OpenCode V2: https://opencode.ai/v2/docs/skills
- Codex: https://developers.openai.com/codex/skills (redirects to the current Build skills page, https://developers.openai.com/codex/build-skills)
- Copilot CLI: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills
- Claude Code: https://code.claude.com/docs/en/skills
- Gemini CLI: https://geminicli.com/docs/cli/skills/
- Gemini activation implementation: https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/tools/activate-skill.ts
- Gemini discovery troubleshooting: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/tutorials/skills-getting-started.md
- Cursor: https://cursor.com/docs/skills
- Pi: https://pi.dev/docs/latest/skills

## Implementation follow-ups

- Verify supporting-file resolution and cross-skill loading in the actual distribution layout, including selective installation and Claude Code's symlink route.
- Document requirements to install all eight skills for the complete workflow, while retaining standalone use of individual methods and their required references.
- Avoid generic claims about GitHub Copilot surfaces not covered by the CLI documentation. Investigate other surfaces separately if they are to be listed as supported.
- The Gemini CLI website currently displays a migration notice for unpaid-tier and Google One users. Record applicable product/access limitations before publishing installation guidance; do not silently substitute Antigravity CLI for the requested Gemini CLI target.
- Preserve explicit workspace state across message-level skill lifetimes and reloads; do not assume a skill stays active identically across hosts.
- Check installed versions, permissions, and available runtimes before any practical verification. Missing credentials or agent installations must be reported as verification gaps, not successes.
- Defer marketplace/plugin packaging unless necessary for the agreed initial installation route. A local discovery route and a marketplace distribution route are different capabilities.
- Keep unrelated preinstalled development skills and personal study records outside the public deliverable. Do not modify them merely to simplify packaging.
