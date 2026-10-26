# Ticket 02: Implementation Evidence and Gaps

## Scope and baseline

The baseline is ticket 01 commit `02d169ac8c2995648180f7a867dbd44139e202fe`. Ticket 02 adds `to-drill` and its shared practice contract, extends state to 1.1.0 with read-only 1.0.0 compatibility and consent-based migration, and adjusts orientation continuation to offer optional immediate practice.

Full seven-method orchestration, spaced review, historical dashboards, and agent-specific installation remain outside this ticket. These are instruction-based skills and data contracts, not a deterministic runtime.

## Observed evidence

| Inspection | Observed result | Limitation |
| --- | --- | --- |
| OpenCode's live skill catalog | `to-drill` appeared after creation | Discovery only, not execution or multi-agent compatibility |
| Python standard-library JSON parsing | Updated schema parses successfully | No full JSON Schema meta-validation or state-instance validation |
| Recursive schema reference inspection | All 109 local references resolve | Does not enforce semantic cross-record invariants |
| Pattern compilation | All 11 schema patterns compile in Python | Not proof of behavior in every JSON Schema validator |
| Bundled Markdown references | All 10 inspected links resolve | Does not demonstrate selective installation in another workspace |
| Frontmatter inspection | All three skills have matching names and descriptions at the start of their files | Does not exercise other agents' parsers |
| Git whitespace inspection | Tracked changes passed `git diff --check` | Not a behavior or schema check |
| Ticket 01 commit inspection | Subject 44 characters; longest body line 66; no co-author trailer | Applies to the first-ticket commit only; ticket 02 was uncommitted at inspection time |

No automated tests, learner sessions, package installations, or personal study records were created for these checks. A dedicated JSON Schema validator was not available in the inspected Python environment; machine validation of example states is not claimed.

## Review findings addressed

Separate read-only Standards and Spec reviews examined tracked changes against the baseline and the explicitly scoped new practice files.

### Standards

- Active practice now blocks source-scope changes and map regeneration until the learner finishes or explicitly abandons that attempt. The original pending prompt and pointer remain intact.
- Raw learner text and normalized multiple-choice selection are separate fields, preserving the actual answer while allowing reproducible evaluation.
- Early correction records learner consent, evaluates eligible submitted responses before finalization, and only then makes the attempt abandoned and immutable; unanswered responses remain untouched.

### Spec

- Quiz correction explicitly accepts evaluated revealed/skipped/invalidated exclusions as resolved items, without fabricating answers or silently requiring abandonment.
- Selection validation applies to answer-bearing evaluations, while answerless exclusions explicitly permit a null selection.
- Final attempt reporting includes correct/evaluated counts, sample size, correctness percentage, exclusions, and a zero-denominator unavailable result. Partial abandoned results remain labeled partial and excluded from completed-session aggregates.

Final follow-up reviews on both axes reported no remaining actionable findings. These are structural review outcomes, not evidence of an exercised learner session.

## Implementation coverage

- Standalone practice initializes or reuses the same workspace and concept IDs without requiring a prior map or the orchestrator.
- Question records preserve immutable prompts, answer keys, source evidence, topic/concept associations, difficulty, and supersession links.
- Learner-facing deck artifacts omit solutions; the private state retains the keys. This is presentation separation, not secrecy from someone with file access.
- Attempts retain order, actual responses, selection, assistance, evaluation, timestamps, and pending work. Generation alone creates no learner attempt.
- Only completed unaided evaluated responses contribute to the derived assessed-question index; assessed coverage is distinct from correctness.
- Existing 1.0.0 workspaces require consented, snapshot-preserving migration before writes. Later phases and review enrollment remain unavailable.
- A completed deck-generation step is explicitly distinct from a completed practice attempt, completed study cycle, and demonstrated mastery.

## Still unverified

- Real flashcard reveal timing, quiz correction timing, clarification, exclusion, and scoring in a learner session.
- Actual migration, interruption/recovery between response and evaluation, and repeat generation without overwriting records.
- Active-practice/map-revision conflict handling and cross-topic/cross-agent resumption.
- Full JSON Schema validity and instance acceptance/rejection with a dedicated validator.
- Source-reading, filesystem privacy, snapshots, and permissions in a real learner workspace.

Checked implementation criteria indicate authored behavior and structural review coverage, not successful end-to-end scenario execution. Later integration work must keep documentation evidence separate from exercised behavior.
