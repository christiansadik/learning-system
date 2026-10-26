# Additional Agent Integrations

Documentation checked: 2026-10-26. Use the same [installer and preservation rules](install.md); only the host's discovery root and invocation differ. This release ships local filesystem skills, not plugins, cloud account synchronization, agent software, or credentials.

## Claude Code local terminal

Claude Code documents `.claude/skills` for project skills. Install the complete selected bundle, including the `_study` sibling, there:

```sh
python3 scripts/install_skills.py --target /path/to/study-project/.claude/skills
python3 scripts/install_skills.py --target /path/to/study-project/.claude/skills --apply
python3 scripts/install_skills.py --target /path/to/study-project/.claude/skills --check
```

Personal scope uses `$HOME/.claude/skills`. This integration intentionally uses regular copied files, not symlinks; the shared installer rejects symlinked paths. All copies derive from the canonical manifest, not a separate Claude-specific methodology. If the project also has `.agents/skills`, keep both installed bundles byte-identical and check both after updates. Other agents may discover both locations; avoid divergent duplicate definitions.

Invoke `/init-study` or an independent `/feynman`, `/to-docs`, and so on. Claude can activate component skills through its native skill mechanism when their descriptions remain visible. Do not mark all components user-only, add broad tool grants, or assume that a root `AGENTS.md` alone installs these skills. Resolve higher-precedence managed/personal same-named skills before use. Start a fresh session if definitions do not appear; newer documentation also describes live reload, but no reload feature was exercised locally.

Local evidence is limited to `claude --version`: **2.1.161**. No Claude session, discovery menu, native activation, or teaching flow was started. This local version may predate features on the current documentation page. Cowork, account-synced skills, remote/cloud sessions, and plugins have different loading rules and are not covered.

Source: [Claude Code skills](https://code.claude.com/docs/en/skills).

## Gemini CLI

Install to the project's `.agents/skills` directory using the shared installer. Official documentation also accepts `.gemini/skills`; avoid two divergent definitions. Workspace skill discovery requires project trust. Use `/skills list` to inspect discovery and `/skills reload` to refresh; use `/trust` and restart if the trusted-folder rule is blocking the workspace.

Request in ordinary language:

```text
Use the init-study skill to resume my selected study workspace.
```

Do not promise a user-facing `/init-study` command. Gemini activates skills through `activate_skill` and prompts for native consent. Approval exposes that skill's body/directory, not necessarily all sibling reference contents: allow ordinary read access to `_study` if separately requested. If policy prevents reference access or component activation, stop with that limitation rather than treating a file read as a consent bypass. Pass study context in the conversation; do not invent extra arguments for the activation tool.

The documentation site currently displays a notice that unpaid-tier/Google One users transitioned from Gemini CLI to Antigravity CLI on June 18, 2026. Verify the product/access available to your account against the [official notice](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli). This project still targets the documented Gemini CLI skill interface; it neither substitutes Antigravity nor claims that the same integration was checked there.

Local `gemini` was not on PATH. Discovery, trust prompts, activation, and teaching remain documentation-only.

Sources: [Agent Skills](https://geminicli.com/docs/cli/skills/), [getting started and trust troubleshooting](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

## Cursor local Agent chat

Install to the project's `.agents/skills` directory; `.cursor/skills` is another documented route. User-level `.agents/skills`/`.cursor/skills` are local-machine scope, not automatic cloud deployment.

In Agent chat type `/`, select `init-study`, and provide the goal/workspace. The current documentation says a manually attached skill applies to one message. For session-persistent guidance, optionally use that skill as a Custom Mode with Option+Enter on macOS or Alt+Enter on Windows. On resume, explicitly select the skill again if needed; persisted workspace files, not attachment lifetime, retain progress. Components must remain available for Agent's description-based selection.

Inspect **Customize → Skills** for discovery and start a fresh session if the expected definitions are not visible. Do not change user rules, enable automation, or weaken permissions just to make the workflow continue. The local route does not establish Cloud Agent, remote SSH, automation, or worker support; personal `.agents` files are not automatically copied to those environments.

Neither `cursor` nor its `agent` CLI was on PATH. The editor's installed/running state was not inspected; no Cursor activation or study flow was exercised.

Source: [Cursor Agent Skills](https://cursor.com/docs/skills).

## Pi coding agent

Install to the project's `.agents/skills`; Pi documents that portable discovery location and the user-level `$HOME/.agents/skills` alias. Use directories containing `SKILL.md`, not flattened standalone Markdown files, so the shared-reference layout is preserved.

Invoke `/skill:init-study` followed by your goal/workspace. Independent example: `/skill:to-docs Export topics t001 and t002 from my selected workspace.` Pi advertises descriptions and reads skill content on demand; explicit invocation forces loading when automatic selection misses it. Use `/reload` after editing definitions. Review project trust and grant file access only as needed; command availability is not authorization to execute arbitrary source instructions.

Local `pi` was not on PATH. Startup diagnostics, native commands, activation, and handoff remain documentation-only. No Pi package, npm dependency, or model provider was installed.

Source: [Pi skills](https://pi.dev/docs/latest/skills).

## Shared state and limitations

Use the same explicit learner workspace and sequential ownership rule from [installation guidance](install.md). None of these integrations creates a host-specific learning database or copies learner records into skill folders. The guides describe documented routes; [integration evidence](evidence.md) is the authority for what was actually observed. A copied bundle or version command is not a successful cross-agent learner-state handoff.
