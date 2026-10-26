# Ticket 05: Evidence and Limitations

Baseline reviewed: ticket 04 commit `aefb11b`, now `62bb9ee` with an identical tree after wrapping the preceding ticket 03 commit message. Scope: `to-docs`, paired export records/reservations, consent-based upgrade to 1.4.0, and minimal resumption/continuation integration. No media service, cumulative reviews, or full orchestration is implemented.

## Observed structural evidence

- OpenCode advertised `to-docs` after file creation.
- The updated schema parsed as JSON; all 157 local references resolved and its patterns compiled during structural inspection.
- All 33 inspected bundled Markdown links resolved; seven skill frontmatters had matching names and descriptions.
- Independent Standards and Spec reviews found no actionable findings. These were read-only document/schema inspections, not successful export scenarios.

## Implementation coverage

The method accepts one or multiple specific topics within one main topic, defaulting to the current topic in orchestrated mode. It prepares exactly two primary Markdown files: a readable concept map and a self-contained explanation, with scope, citations, limitations, and supported cross-topic links.

An export reserves both paths and its selected topics before generation, records a single owner checkpoint, and links both artifacts on completion. Resumption inspects partial files rather than overwriting them, generates only missing work with unchanged scope, and reconciles registration idempotently. Revised scope or regenerated documents receive a new export ID. Other topics' checkpoints and completion statuses are not advanced merely by inclusion in a combined export.

Source originals, earlier exports, and user edits are preserved. Private learner performance is excluded from exports unless explicitly requested. Completion does not schedule reviews, finish a study cycle, or claim understanding; no audio/video is generated or uploaded.

## Remaining gaps

No real learner export, multi-topic source inspection, interrupted write/finalization, recovery, state migration, or third-party media import was exercised. Dedicated JSON Schema meta-validation/state-instance validation and actual multi-agent behavior remain unverified. No automated tests, package installations, or synthetic learner progress were created. Ticket 05 was uncommitted when this inspection was recorded; its commit was subsequently authorized.

Checked ticket criteria represent instruction/schema implementation coverage and structural review, not demonstrated end-to-end execution.
