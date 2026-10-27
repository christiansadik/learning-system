# Public Distribution Checklist

The repository destination is [christiansadik/learning-system](https://github.com/christiansadik/learning-system), and the project is licensed under [MIT](../LICENSE). This checklist does not authorize an upload, push, or release.

## Distribution boundaries

| Content | Intended scope |
| --- | --- |
| Eight skill definitions and eleven shared files in `skill-bundle.json` | Installable product; exactly 19 files, including the MIT notice |
| Installer, manifest, English README, integration/evidence/examples documentation | Public project support |
| Project-owned `AGENTS.md`, glossary, agent conventions, spec/tickets/review records | Development documentation, reviewed separately from the installable product |
| Other preinstalled `.agents/skills` folders and `skills-lock.json` | Local tooling; excluded, not redistributed |
| Learner `study/` or custom workspace, sources, answers, state/snapshots, exports | Private by default; never publish without explicit approval |
| Credentials, `.env` files, caches, generated archives | Excluded from normal version control |

The installer uses exact file allowlists and rejects unexpected files inside managed source directories. Git ignore rules additionally hide unrelated preinstalled skills; they do not delete them or remove already tracked content. Inspect both safeguards rather than treating either as a security scanner.

## Before staging or publishing

1. Decide which authored project files belong in the public repository. Use explicit paths rather than blindly adding every local file.
2. Inspect `git status --short`, `git ls-files`, and `git diff --cached --name-only`; inspect actual content when provenance or privacy is uncertain.
3. Confirm the tracked skill folders match the product manifest. Existing third-party development skills must remain outside the staged/tracked deliverable.
4. Confirm no learner workspace, supplied book/video transcript, real answers, credentials, local absolute machine paths, or private configuration is included. Synthetic examples must stay clearly labeled.
5. For custom workspaces, verify effective exclusion and whether any files were already tracked. Stop and ask before untracking, removing, or rewriting existing user work.
6. Run the installer's read-only `--check` against an intended installation. This checks copied bytes/references, not behavioral compatibility, licensing, or secrets.
7. Review [integration evidence](integrations/evidence.md). Keep native loader observations, filesystem checks, documentation-only routes, and actual learner execution distinct. Real cross-agent handoff is still unverified.
8. Retain the MIT copyright/permission notice, including `_study/LICENSE.md` in installed bundles. The root `LICENSE` is canonical and the installer verifies its bundled copy. This does not grant third-party redistribution rights.
9. Request explicit approval before creating a GitHub repository/remote, pushing, uploading an archive, or publishing a release. Commits alone are not publication permission.

## Publication status and remaining checks

- **License:** MIT selected with the owner's delegated approval; retain its notice in copies or substantial portions.
- **Destination/publication:** the owner created the GitHub repository and supplied its URL. Local `origin` points to that repository; pushing and release publication still require explicit approval.
- **Compatibility assurance:** real learner sessions and sequential cross-agent handoff remain unverified. Publish the current limitation, not a claim that all seven agents have passed an end-to-end check.

## Maintenance

Keep methodology/state contracts in the canonical bundle and host details in integration guides. A new skill/reference file requires reviewing the manifest and matching ignore exceptions. Preserve versioned state migration and privacy rules when updating installed bundles. Respect the project's explicit-request policies for tests, commits, and pushes.
