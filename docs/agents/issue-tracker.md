# Issue Tracker: Local Markdown

Specs and tickets live under `.scratch/<feature>/`.

- Spec: `spec.md`.
- Tickets: `issues/<NN>-<slug>.md`, one file per ticket.
- Record implementation lifecycle in `Status:`: `ready-for-agent`,
  `in-progress`, or `done`.
- Record incoming triage roles in an optional `Triage:` field, using
  `triage-labels.md`. Generated implementation tickets are already agent-ready;
  their initial `Status: ready-for-agent` is a lifecycle state, not a request
  to repeat triage.
- Record dependencies in a `Blocked by:` field.
- Append discussion under `## Comments`.
- Work on blockers before dependent tickets.

When asked to publish a spec or ticket, create a local file.
Do not create GitHub issues unless explicitly requested.
