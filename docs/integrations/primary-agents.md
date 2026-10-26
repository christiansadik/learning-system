# Priority Agent Integrations

Documentation checked: 2026-10-26. Use the [shared installer](install.md); no host-specific copy of the teaching methodology is needed. The supported installation route is a local filesystem bundle with `_study` beside the selected skill folders.

## OpenCode V2

- **Project discovery:** `.agents/skills`, `.opencode/skills`, or `.claude/skills`. The shared installer uses `.agents/skills` to avoid host-specific configuration.
- **Request:** `@init-study I want to study Magento to develop custom modules.`
- **Standalone example:** `@to-docs Export the concept map and explanation for topics t001 and t002 in my selected workspace.`
- **Loading:** OpenCode advertises descriptions and uses its native `skill` tool for full content; the path-derived skill ID matches the directory name. The agent must read `_study` references explicitly.
- **Permissions:** normal skill/file-write permission applies. Leave components model-reachable; do not set `disable-model-invocation` or blanket permission grants to work around a blocked method.
- **Refresh:** begin a fresh session after installation if definitions are not visible. No special config file is required for this route. Check source precedence if a different same-named skill loads.
- **Local evidence:** OpenCode 2.0.32 advertised all eight study skills. Native loading of `init-study` and `to-map` succeeded in the current session and returned the expected skill base directories. This is loader evidence, not an executed learner flow.

Source: [OpenCode V2 skills](https://opencode.ai/v2/docs/skills).

## Codex CLI / IDE extension local skills

- **Project discovery:** `.agents/skills` along the working-directory-to-repository-root chain. Start in the study project, not the distribution checkout unless it is also your workspace.
- **Request:** `$init-study I want to study Magento to develop custom modules.` Select a skill through `/skills` when needed.
- **Loading:** Codex's progressive-disclosure mechanism reads `SKILL.md` when explicitly requested or matched by description; the main agent reads required references. Native activation here does not mean launching another CLI or inventing an OpenCode-style tool call.
- **Policy:** preserve implicit reachability of component methods. No OpenAI-specific UI metadata or tool dependencies are required by this instruction-only bundle.
- **Refresh:** Codex documents automatic change detection; restart if a definition does not appear. Resolve duplicate names before studying.
- **Local evidence:** Codex was not on `PATH`. The route is documentation-confirmed only; CLI/IDE activation and cross-agent study resumption were not exercised. No cloud/plugin compatibility is implied.

Source: [Codex Build skills](https://developers.openai.com/codex/build-skills).

## GitHub Copilot CLI

- **Project discovery:** `.agents/skills`, `.github/skills`, or `.claude/skills`. This guide is for CLI, not an unverified claim about editor or cloud-agent surfaces.
- **Request:** `Use /init-study to study Magento and resume the workspace I selected.`
- **Inspection:** `copilot skill list --json` lists local skill metadata without running a learner session. In the interactive CLI, `/skills reload` refreshes discovery and `/skills info init-study` inspects its definition.
- **Loading:** Copilot activates skills from explicit requests or matching descriptions. Supporting references remain normal files requiring permission. Do not add broad `allowed-tools` grants or use a single-file installer that omits `_study`.
- **Local evidence:** Copilot CLI 1.0.90 listed all eight study skills as enabled. No model prompt, learner session, authentication change, or background task was launched. Cross-agent teaching/quiz resumption remains unexercised.

Sources: [Adding CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

## Compatibility claims

All three have documented filesystem discovery routes. Only the limited local observations above were exercised; they do not establish successful end-to-end study, schema migrations, or cross-agent resumption. Installation-copy/reference integrity is separate evidence. Unavailable software/credentials are verification gaps, not passed checks. The workflow must stop and explain if the host cannot load a required component natively or read a required reference.
