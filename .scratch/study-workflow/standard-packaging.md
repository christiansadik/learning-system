# Standard Agent Skills Packaging

Status: done

## Request

Make the project installable like other ecosystem skills through `npx skills add christiansadik/learning-system`, both as the complete flow and as individual methods. Preserve one canonical source rather than maintaining independent copies by hand. This request authorizes implementation and local installation inspection, not commits, pushes, npm publication, or learner test generation.

## Decisions

- Move the eight canonical templates to `authoring/skills/<name>.md` and ten canonical contracts to `authoring/references/`. Templates deliberately lack the discoverable `SKILL.md` filename.
- Generate committed `skills/<name>/` packages, each with `SKILL.md`, internal `references/`, and root `LICENSE`. Every individual package is self-contained and declares MIT in frontmatter.
- Keep manifest format separate from learner-state version: bundle manifest becomes version 2, while learner state stays 1.6.0 with unchanged schema bytes.
- Preserve unrelated ignored development skills and local agent configuration. Ignore all local agent skill-installation roots; they are not distribution sources.
- Generate from an explicit manifest. Check all Markdown links remain within each installed skill. Preserve edited/unknown/obsolete output instead of silently deleting it; use a generated hash receipt for controlled regeneration and a read-only reproducibility mode.
- Retain the conservative Python copy installer as an optional fallback consuming the same generated packages. Standard Skills CLI overwrite/link/update semantics are distinct and must be documented honestly.
- Do not publish a custom npm installer: the standard CLI handles agents and selection once generated packages reach the GitHub branch.

## Observed local evidence — 2026-10-27

- Skills CLI 1.7.4 from the official npm package, Node.js 24.21.0; lifecycle scripts and CLI telemetry disabled during controlled local inspection.
- Reproducibility check matched eight generated packages and 96 package files; each package has 12 files and no sibling reference dependency.
- A clean local source with both canonical authoring and generated packages yielded exactly eight discovered skills, without duplicate template entries.
- Standard CLI `--copy` installed the full eight-skill set for OpenCode and a single `to-docs` package for Claude Code. Every expected file/reference/license matched.
- Default installation accepted all seven target agent IDs and retained the complete canonical `to-docs` package; the created agent link resolved correctly.
- The Python fallback's read-only check matched the generated 96-file distribution.

These are local installer/package observations, not native teaching, state migration, or learner-state handoff. No automated test files/suite, agent application, model session, login, commit, or push was created. GitHub-shorthand download cannot be verified against unpushed packaging; remote availability remains a publication condition.

## Standards

No actionable findings. Generated duplication is controlled by one canonical authoring source and a reproducible build receipt; user-modified/unknown output is preserved.

## Spec

The initial review identified a local-import bytecode side effect contradicting read-only preview/check claims. The fallback now disables bytecode generation before importing the generator. Fresh-checkout preview/check inspection created neither local bytecode nor installation files, and the final follow-up found no residual actionable issues. Learner-state schema bytes match the baseline exactly.

Summary at implementation completion: Standards 0 findings; Spec 0 residual findings after one minor correction. Learner behavior, handoff, and GitHub download were then unverified; commit/push had not yet been authorized.

## Subsequent authorized publication

The owner later requested commit/push. Packaging commit `545c2d7` was pushed to `origin/master`, and the remote default branch resolved to it. HTTPS push lacked credentials, so the existing SSH authentication for the same owner/repository was used through a per-command URL rewrite; the stored HTTPS origin URL was left unchanged. Skills CLI 1.7.4 subsequently downloaded the published repository shorthand and found exactly eight skills. Actual teaching and cross-device handoff remain for separate learner verification; no model session or automated test suite was run.

## Sources

- https://github.com/vercel-labs/skills
- https://github.com/vercel-labs/skills/blob/main/docs/commands.md
- https://github.com/vercel-labs/skills/blob/main/docs/agents.md
- https://registry.npmjs.org/skills/latest (version/engine metadata at inspection time)
