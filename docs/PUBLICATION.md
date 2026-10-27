# Public Distribution Checklist

The repository destination is [christiansadik/learning-system](https://github.com/christiansadik/learning-system), and the project is licensed under [MIT](../LICENSE). This checklist does not authorize an upload, push, or release.

## Distribution boundaries

| Content | Intended scope |
| --- | --- |
| Generated `skills/<name>/` packages | Eight installable, self-contained skills; 12 files each, including references and MIT license |
| `authoring/` and `skill-bundle.json` | Canonical templates/contracts and generation allowlist, not independently discoverable skills |
| Installer, manifest, English README, integration/evidence/examples documentation | Public project support |
| Project-owned `AGENTS.md`, glossary, agent conventions, spec/tickets/review records | Development documentation, reviewed separately from the installable product |
| Local `.agents/skills` or other agent installation folders and `skills-lock.json` | Local tooling/installations; excluded, not redistributed |
| Learner `study/` or custom workspace, sources, answers, state/snapshots, exports | Private by default; never publish without explicit approval |
| Credentials, `.env` files, caches, generated archives | Excluded from normal version control |

The generator uses explicit canonical sources and validates each package's links within its own folder. Its root build receipt is generation metadata, not an installed skill. Git ignore rules hide local agent installations/tooling; they do not delete files or remove already tracked content. Inspect these boundaries rather than treating them as a security scanner.

## Before staging or publishing

1. Decide which authored project files belong in the public repository. Use explicit paths rather than blindly adding every local file.
2. Inspect `git status --short`, `git ls-files`, and `git diff --cached --name-only`; inspect actual content when provenance or privacy is uncertain.
3. Run `python3 scripts/build_skills.py --check` and confirm only the eight generated package directories contain published `SKILL.md` files. Include all generated files and their build receipt in the commit; canonical templates must not be duplicated as discoverable skills. Keep local agent tooling outside the staged/tracked deliverable.
4. Confirm no learner workspace, supplied book/video transcript, real answers, credentials, local absolute machine paths, or private configuration is included. Synthetic examples must stay clearly labeled.
5. For custom workspaces, verify effective exclusion and whether any files were already tracked. Stop and ask before untracking, removing, or rewriting existing user work.
6. Inspect standard CLI discovery with `npx skills add ./skills --list`, or use the fallback's read-only `--check` for copied bytes. These checks do not establish teaching behavior or a general secrets/licensing audit.
7. Review [integration evidence](integrations/evidence.md). Keep native loader observations, filesystem checks, documentation-only routes, and actual learner execution distinct. Real cross-agent handoff is still unverified.
8. Retain each skill's generated `LICENSE`; the root `LICENSE` is canonical. Generated licenses and metadata must match it. This does not grant third-party redistribution rights.
9. Request explicit approval before creating a GitHub repository/remote, pushing, uploading an archive, or publishing a release. Commits alone are not publication permission.

## Publication status and remaining checks

- **License:** MIT selected with the owner's delegated approval; retain its notice in copies or substantial portions.
- **Destination/publication:** the owner created the GitHub repository and supplied its URL. Local `origin` points to that repository; pushing and release publication still require explicit approval.
- **Standard installation:** repository-shorthand `npx skills add` requires the generated packages to reach the published branch. A local CLI install does not prove that unpushed code is downloadable from GitHub.
- **Compatibility assurance:** real learner sessions and sequential cross-agent handoff remain unverified. Publish the current limitation, not a claim that all seven agents have passed an end-to-end check.

## Maintenance

Keep methodology/contracts in `authoring/` and host details in integration guides. Review the manifest and regenerate committed packages after source changes; do not hand-edit distribution copies. Ignore all local agent installations. Preserve learner-state migration and privacy rules. Respect explicit-request policies for tests, commits, and pushes.
