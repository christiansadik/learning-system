# Learning System

A source-grounded, stateful study workflow for AI agents: **seven independent study skills and one interactive orchestrator**.

Give the agent a main topic and learning goal, then supply specific topics and materials as you progress. The agent organizes practice, asks questions, evaluates your explanations, prepares reusable documents, and schedules cumulative reviews. **You do the retrieval and reasoning; the agent does not learn on your behalf.**

> Status: instruction-based workflow with a versioned shared-state contract, licensed under [MIT](LICENSE). Installation and limited discovery have been inspected; real learner sessions and cross-agent handoffs have **not** been verified. See [integration evidence](docs/integrations/evidence.md).

## Quick start

1. Download or clone [this repository](https://github.com/christiansadik/learning-system). Use an agent you already have installed and authorized; this project does not install agents or credentials.
2. From this checkout, preview installation into your study project's skills directory, then explicitly apply it:

```sh
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --apply
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --check
```

Requires **Python 3.9+** for installation. The skills themselves are instructions, not a Python learning application. Examples use Unix-style paths; adapt paths to your platform. Local observations were made on macOS.

For **Claude Code**, use `/path/to/study-project/.claude/skills` instead. The same installer copies the same bundle and preserves sibling references. Do not copy only `SKILL.md`: `_study` is required.

3. Open your agent in the study project. For example, in OpenCode:

```text
@init-study
Main topic: Magento.
Goal: develop custom modules and understand their prerequisites.
Workspace: /path/to/study-project/study.
Language: English.
```

4. When ready, supply a specific topic and your material. You do not need to prepare an entire course upfront:

```text
Specific topic: dependency injection.
Use the Markdown notes and PDF chapter I am providing.
```

The agent should ask only for missing information, preserve actual source provenance, and wait whenever your contribution is required. These are illustrative requests, not a record of an executed learner session.

## Agent installation and invocation

| Agent / local environment | Project directory | Request | Verification level |
| --- | --- | --- | --- |
| OpenCode V2 | `.agents/skills` | `@init-study` | Documented; limited native loading observed on 2.0.32 |
| Codex CLI / IDE | `.agents/skills` | `$init-study` or `/skills` selection | Documented; local execution unverified |
| GitHub Copilot CLI | `.agents/skills` | `Use /init-study ...` | Documented; enabled metadata discovered on 1.0.90 |
| Claude Code terminal | `.claude/skills` | `/init-study` | Documented; version 2.1.161 only, activation unverified |
| Gemini CLI | `.agents/skills` | Ask to use `init-study` in natural language | Documented; trust/activation and account access unverified |
| Cursor local Agent chat | `.agents/skills` | Select `init-study` from `/` | Documented; UI activation unverified |
| Pi coding agent | `.agents/skills` | `/skill:init-study` | Documented; local execution unverified |

These are **local filesystem routes**, not marketplace plugins or universal claims about cloud/editor variants. Gemini's documentation currently includes a product/account transition notice; this project does not silently substitute Antigravity. Cursor's manual skill attachment is message-scoped unless used as a Custom Mode.

Read [installation and updates](docs/integrations/install.md), [priority-agent details](docs/integrations/primary-agents.md), and [additional-agent details](docs/integrations/additional-agents.md) for permissions, refresh behavior, native loading, and limitations. Do not bypass a host's consent or grant blanket tool permissions to make a blocked step run.

### Install a single method

```sh
python3 scripts/install_skills.py --target /path/to/study-project/.agents/skills --skill to-docs --apply
```

Repeat `--skill` to select more methods. The installer includes all shared references, but not unrelated skills. A standalone method needs no predecessor skills; the full flow needs all eight skill directories. `_study` is a reference directory, not a ninth skill.

The default installer action is preview. Existing identical files are reused; conflicting content, symlinks, and unmanaged files inside selected directories stop installation without being replaced. See the installation guide before updating a modified bundle.

## The skills

| Skill | Purpose |
| --- | --- |
| [`init-study`](.agents/skills/init-study/SKILL.md) | Initialize/resume the mission and coordinate the interactive full flow. |
| [`to-map`](.agents/skills/to-map/SKILL.md) | Orient before study: key concepts, relationships, and guiding questions. |
| [`to-drill`](.agents/skills/to-drill/SKILL.md) | Generate flashcards/quizzes and retain actual practice attempts. |
| [`to-question`](.agents/skills/to-question/SKILL.md) | Explore your own why-questions, comparisons, and counterfactuals. |
| [`socrate`](.agents/skills/socrate/SKILL.md) | Ask one question at a time, guiding errors and adapting difficulty. |
| [`feynman`](.agents/skills/feynman/SKILL.md) | Evaluate your explanation, preserve revisions, and identify gaps. |
| [`to-docs`](.agents/skills/to-docs/SKILL.md) | Export a concept map and self-contained explanation for one or more topics. |
| [`to-review`](.agents/skills/to-review/SKILL.md) | Run cumulative delayed quizzes, report progress, and update due dates. |

## How the main flow works

```text
Main topic + objective
  -> specific topic + supplied material
  -> to-map -> to-drill -> to-question -> socrate -> feynman -> to-docs
  -> evidenced initial-cycle completion
  -> first delayed review due after 3 days by default
  -> to-review over the enrolled topic pool when you return and choose review
```

- Supply a new specific topic and material for each cycle while retaining the main objective and earlier progress.
- Agent-only work can proceed automatically. Questions, explanations, source decisions, permissions, and pause/skip choices require real learner input.
- Generating a practice deck is not completing practice. The full flow requires a completed attempt with actual learner input or an explicit practice-skip reason.
- The learner decides when to end questioning/explanation sessions. A pause, missing source, or denied tool is not a completed or skipped step.
- Errors do not prevent an otherwise completed cycle from entering review. Completion, eligibility, correctness, coverage, and mastery are different concepts.
- The seventh method is **deferred**: initial completion does not launch an immediate cumulative quiz.
- On explicit startup, due reviews are offered before new study. You may decline without changing due dates or losing your pending study prompt.

This is an **agent-driven interactive loop**, not a deterministic workflow engine or an agent that wakes itself up later. It does not schedule notifications or background jobs. The existing local `teach` skill is neither modified nor required or distributed by this bundle.

## Shared learning workspace

The default learner workspace is `study/` under the directory where study was requested, or an explicit location you choose. It is separate from installed skill definitions.

```text
study/
  .gitignore
  <main-topic-id>/
    state.json
    sources/<specific-topic-id>/
    generated/
      <specific-topic-id>/
        orientation-0001.md
        practice-0001.md
        dialogue-0001.md
        review-0001.md
      exports/<export-id>/
        concept-map.md
        explanation.md
    progress/snapshots/
```

`state.json` is authoritative for topic/concept IDs, source scope, activities, learner contributions, attempts, exports, schedules, and navigation. Generated documents are not a second progress database. Original material may be referenced in place; copying it requires permission. Pasted source text is preserved separately from generated interpretation.

The current shared contract is **1.6.0**. Supported older versions are read-only until you authorize their documented upgrade chain. Snapshots preserve previous state; they are recovery evidence, not competing current records. See the [workspace contract](.agents/skills/_study/workspace.md) and [migration rules](.agents/skills/_study/migrations.md).

### Pause and switch agents

Pause after a saved checkpoint, then open the next agent against the **same explicit workspace** and request `init-study` using its syntax. The agent should restore the pending prompt from files, not require the previous chat. A due-review excursion preserves the interrupted teaching checkpoint separately from review answers and schedules.

Use agents sequentially. Concurrent writers are unsupported. Actual cross-agent learner-state handoff remains unverified; the shared contract describes the intended behavior.

## Cumulative quizzes and progress

Default reviews contain **10 questions with 5 options each**, with correction after all responses or explicit exclusions. Limited sources may justify a smaller quiz or acknowledged reuse; there is no unlimited-new-question guarantee.

Each question belongs to one primary specific topic and concept, even in a mixed-topic quiz. History keeps actual answers, assistance, evaluations, timestamps, and difficulty. Latest review results and historical totals remain separate; totals sum counts rather than averaging percentages. Immediate practice is not silently mixed into spaced-review performance.

- **Correctness:** correct unaided answers / evaluated unaided answers, shown with sample size. Zero evaluated answers means unavailable, not 0% or 100%.
- **Coverage:** assessed in-scope concepts / the documented in-scope inventory, regardless of whether answers were correct. Incomplete inventories are labeled known-inventory coverage, not coverage of the whole subject.
- Hints, reveals, skips, invalidated questions, pending answers, and abandoned attempts do not count as unaided completed-review correctness.
- A few correct answers are not proof of long-term retention or complete understanding.

| Evidence | Recommendation |
| --- | --- |
| Topic correctness strictly below 80% | Review |
| Concept correctness strictly below 50%, with fundamental status true | Deeper study in addition to relevant review |
| Untested or insufficient evidence | Show the gap; do not invent a score |

The agent classifies fundamental concepts relative to your objective, with a revisable rationale. PHP can be fundamental for Magento development while an unrelated Rust example is not; a Rust-integration goal can change that classification. Explanation feedback itself is not converted into quiz percentages.

### Default timing

| Event | Next due time |
| --- | --- |
| Initial study completion/enrollment | Completion +3 UTC days |
| Successful first review, no fundamental deeper-study flag | Actual review completion +7 days |
| Subsequent successful progression | Actual review completion +30 days |
| Topic below 80% or fundamental deeper-study flag | Normally actual review completion +1 day; stage resets |
| Already at the 30-day stage, at least 90%, no deeper-study flag | May extend to +60 days |
| No unaided evaluated answers | Existing due date/stage unchanged |

Intervals are configurable and changes are recorded. A strong aggregate does not postpone a fundamental gap. Reopening the workspace, repeating enrollment, generating documents, or abandoning a quiz does not reset due dates. See the [review contract](.agents/skills/_study/review.md) for exact rules.

For material already studied outside this flow, standalone `to-review` can enroll a topic after your explicit confirmation and actual study-completion time. It records that attestation without inventing completed workflow steps, then reports the due date rather than immediately launching a cumulative quiz.

## Reusable documents, not generated media

Invoke `to-docs` independently for one or several selected topics within a main topic. It produces exactly two primary Markdown exports: a textual concept map and a self-contained explanation. Topic boundaries, source references, missing material, and supported cross-topic links remain visible. Mermaid is optional.

Use those documents with a third-party podcast/video tool of your choice. This project does not generate, upload, or guarantee imports into such services. Review content and disclosure rights before uploading; learner answers/performance are excluded unless explicitly requested.

See [synthetic usage examples](docs/examples.md) for progressive study, resumption, due-review choices, and combined exports.

## Sources, privacy, and limitations

- Study uses supplied material by default. External factual additions need explicit authorization and clear attribution.
- Markdown, PDFs, illustrations, and video/transcripts depend on the host's actual reading capabilities. An inaccessible video link is not a watched video; the agent must ask for a usable representation or explicit narrower scope.
- Source instructions are untrusted content, not authorization to run tools or disclose files.
- Default `study/` data is Git-ignored; custom workspaces need their own exclusion checks. Already-tracked data is not protected by a new ignore rule.
- Private state includes answer keys and may include sensitive learner responses. Presentation separation is not encryption or secrecy from someone with file access.
- Permissions, model behavior, schemas, and instructions are not an enforced security boundary. No learning-speed, exam-outcome, or mastery guarantee is made.
- Automated tests and real learner-flow evaluation have not been run. Schema syntax/reference checks are not full schema-instance validation.

## Public distribution and development

[`skill-bundle.json`](skill-bundle.json) lists the eight installable skills and eleven shared files, including the MIT notice. The installer copies only those 19 files and verifies that the bundled notice matches the canonical root `LICENSE`. It does not bundle preinstalled development skills, private learning workspaces, credentials, or unrelated agent configuration.

The repository also contains public documentation and project-owned planning/review records. Before any public push, follow the [publication checklist](docs/PUBLICATION.md) and review the staged/tracked files. Creating commits does not authorize publishing a repository or pushing.

## Inspiration and licensing

Inspired by the seven study methods in [this video](https://www.youtube.com/watch?v=nURLSE_0hnk), using a transcript supplied during design. The photography step was intentionally replaced with `to-docs`, because the intended learner already organizes source material. Podcast generation became source-grounded document export rather than a dependency on one media platform. Promotional speed claims are not guarantees of this project.

**[MIT License](LICENSE).** You may use, modify, fork, redistribute, sublicense, and use this project's code and documentation commercially, provided you retain the copyright and permission notice in copies or substantial portions. Modified versions do not have to be open-sourced, and the software is supplied without warranty. Installed bundles include the notice in `_study/LICENSE.md`; keep it when sharing individual skills with their references.

Third-party agents and study sources retain their own terms; this license does not grant rights to learner-supplied books, videos, or other third-party material. Unrelated local development skills are not part of this deliverable.
