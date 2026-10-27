# Additional Agent Integrations

Host documentation checked: 2026-10-26; packaging updated 2026-10-27. Use the [standard Skills CLI](install.md) to select your agents, or the conservative Python fallback. Every skill now contains its references and license. These are local skills, not cloud account synchronization, agent software, or credentials. Earlier native/version observations below remain historical.

## Claude Code local terminal

Claude Code documents `.claude/skills` for project skills. With the standard CLI:

```sh
npx skills add christiansadik/learning-system --agent claude-code
```

Personal scope uses `$HOME/.claude/skills`; select `--global` when appropriate. The standard CLI supports canonical-copy/symlink installations and `--copy`; each package is self-contained in either mode. A single `to-docs` copy installation was exercised locally with the standard CLI, without launching Claude. The optional Python fallback still rejects symlinked destinations and conflicting files. Avoid divergent duplicate definitions in multiple discovery roots.

Invoke `/init-study` or an independent `/feynman`, `/to-docs`, and so on. Claude can activate component skills through its native skill mechanism when their descriptions remain visible. Do not mark all components user-only, add broad tool grants, or assume that a root `AGENTS.md` alone installs these skills. Resolve higher-precedence managed/personal same-named skills before use. Start a fresh session if definitions do not appear; newer documentation also describes live reload, but no reload feature was exercised locally.

Local evidence is limited to `claude --version`: **2.1.161**. No Claude session, discovery menu, native activation, or teaching flow was started. This local version may predate features on the current documentation page. Cowork, account-synced skills, remote/cloud sessions, and plugins have different loading rules and are not covered.

Source: [Claude Code skills](https://code.claude.com/docs/en/skills).

## Gemini CLI

Install to the project's `.agents/skills` directory using the shared installer. Official documentation also accepts `.gemini/skills`; avoid two divergent definitions. Workspace skill discovery requires project trust. Use `/skills list` to inspect discovery and `/skills reload` to refresh; use `/trust` and restart if the trusted-folder rule is blocking the workspace.

Request in ordinary language:

```text
Use the init-study skill to resume my selected study workspace.
```

Do not promise a user-facing `/init-study` command. Gemini activates skills through `activate_skill` and prompts for native consent. Each package's `references/` now lives inside that activated skill's directory, rather than a sibling `_study` folder. Still respect all read/write permission prompts; if policy prevents required access or activation, stop rather than bypass consent. Pass study context in the conversation; do not invent extra activation-tool arguments. Select `--agent gemini-cli` with the standard installer.

The documentation site currently displays a notice that unpaid-tier/Google One users transitioned from Gemini CLI to Antigravity CLI on June 18, 2026. Verify the product/access available to your account against the [official notice](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli). This project still targets the documented Gemini CLI skill interface; it neither substitutes Antigravity nor claims that the same integration was checked there.

Local `gemini` was not on PATH. Discovery, trust prompts, activation, and teaching remain documentation-only.

Sources: [Agent Skills](https://geminicli.com/docs/cli/skills/), [getting started and trust troubleshooting](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

## Cursor local Agent chat

Select `--agent cursor` with the standard installer. Native project discovery includes `.agents/skills` and `.cursor/skills`. User-level `.agents/skills`/`.cursor/skills` are local-machine scope, not automatic cloud deployment.

In Agent chat type `/`, select `init-study`, and provide the goal/workspace. The current documentation says a manually attached skill applies to one message. For session-persistent guidance, optionally use that skill as a Custom Mode with Option+Enter on macOS or Alt+Enter on Windows. On resume, explicitly select the skill again if needed; persisted workspace files, not attachment lifetime, retain progress. Components must remain available for Agent's description-based selection.

Inspect **Customize → Skills** for discovery and start a fresh session if the expected definitions are not visible. Do not change user rules, enable automation, or weaken permissions just to make the workflow continue. The local route does not establish Cloud Agent, remote SSH, automation, or worker support; personal `.agents` files are not automatically copied to those environments.

Neither `cursor` nor its `agent` CLI was on PATH. The editor's installed/running state was not inspected; no Cursor activation or study flow was exercised.

Source: [Cursor Agent Skills](https://cursor.com/docs/skills).

## Pi coding agent

Select `--agent pi` with the standard installer. Pi documents project `.agents/skills` and the user-level `$HOME/.agents/skills` alias. Preserve the complete skill folder with `SKILL.md`, `references/`, and `LICENSE`, not a flattened Markdown file.

Invoke `/skill:init-study` followed by your goal/workspace. Independent example: `/skill:to-docs Export topics t001 and t002 from my selected workspace.` Pi advertises descriptions and reads skill content on demand; explicit invocation forces loading when automatic selection misses it. Use `/reload` after editing definitions. Review project trust and grant file access only as needed; command availability is not authorization to execute arbitrary source instructions.

Local `pi` was not on PATH. Startup diagnostics, native commands, activation, and handoff remain documentation-only. No Pi package, npm dependency, or model provider was installed.

Source: [Pi skills](https://pi.dev/docs/latest/skills).

## Shared state and limitations

Use the same explicit learner workspace and sequential ownership rule from [installation guidance](install.md). None of these integrations creates a host-specific learning database or copies learner records into skill folders. The guides describe documented routes; [integration evidence](evidence.md) is the authority for what was actually observed. A copied bundle or version command is not a successful cross-agent learner-state handoff.
