# Explanation Feedback and Fundamental Concepts

Available from state **1.3.0**. Read [workspace.md](workspace.md), [dialogue.md](dialogue.md), and [state.schema.json](state.schema.json). A `feynman` session uses the same immutable turns, active-session checkpoint, summary, and pause/finalization rules as other dialogues.

## Feedback on the learner's explanation

Wait for and preserve an actual explanation. For each submitted explanation or revision, save a linked tutor response covering these four categories; explicitly say when a category has no finding rather than inventing one:

| Category | Feedback |
| --- | --- |
| `factual_error` | A specific claim contradicts the inspected source; cite both the learner's claim and source evidence. |
| `missing_concept` | A source-backed concept necessary for the selected explanation scope is absent or lacks an important connection. Do not demand unrelated parts of the book. |
| `unclear_wording` | Wording or structure makes the meaning ambiguous; distinguish this from proven conceptual misunderstanding and request clarification when appropriate. |
| `supported_connection` | A correct explanation or connection supported by the source; recognize it without claiming durable mastery. |

Append actual findings to session observations with the corresponding `category`, concept ID, source evidence, learner-turn ID, and `gap` or `insight` kind. Do not create an observation for an empty category. Tutor turn text contains the full categorized feedback; observations are its structured findings, not independent alternative evaluations.

Unclear or source-insufficient content may be `not_assessed`. Feedback can contain a short targeted correction, but never substitutes a polished full explanation for the learner's revision effort. Preserve every revision as a new learner turn and each feedback as a linked tutor turn. When a previous gap is resolved, append a supported insight referencing the later contribution; do not erase the earlier gap or claim all gaps are closed.

The session summary groups the explanations/revisions, four-category feedback, unresolved gaps, demonstrated connections, and next suggested practice. It is a `dialogue_summary`, not the later `to-docs` explanatory export. It does not convert these observations into practice questions, scores, percentages, or assessed-concept references.

## Contextual fundamental status

The agent autonomously classifies encountered concepts according to whether they are necessary to understand or apply the main topic for the declared objective. Evaluate prerequisites and central practices, not merely the programming language or topic label. For Magento development, PHP may be fundamental while an unrelated Rust example is not; a Rust integration objective could change that decision.

Set `fundamental` to true or false with a nonempty `fundamental_rationale` explaining its relationship to the objective and available source/context support. Null means not yet classified, not nonfundamental. An inferred prerequisite may be labeled as such in the rationale; classification alone does not authorize adding unsupported instructional facts or external sources. Missing evidence must remain explicit rather than hidden by confident language.

Classification is revisable when the objective, material, or demonstrated prerequisites change. Before changing it, append history preserving the concept ID, previous status/rationale, new status/rationale, time, and reason. Do not delete or rewrite older session observations. Apply the same provenance and source-scope rules as other study work; external factual additions still require authorization.

Classifying a concept does not mark it assessed, complete the topic inventory, or trigger numeric review/deeper-study thresholds. Those thresholds apply to evaluated quiz evidence in later review work, not an LLM's impression of an explanation.
