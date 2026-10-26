# 05: Export a Concept Map and Explanation

**What to build:** A learner invokes `to-docs` for one or several selected topics and receives two reusable Markdown documents suitable as inputs to third-party podcast or explanatory-video tools.

**Blocked by:** 01 — Start and Resume a Study Topic.

**Status:** done

## Context

Read the [source specification](../spec.md), project glossary, and common workspace contract. `to-map` provides orientation before studying; `to-docs` creates self-contained export material. This replaces the original video workflow's photography method.

## Acceptance criteria

- [x] `to-docs` works independently for an explicit selection of one or multiple topics; its normal orchestrated scope is the current specific topic.
- [x] Each request produces exactly two primary Markdown exports: a concept map and a self-contained explanatory document.
- [x] The map includes a readable hierarchy and explicit relationships; any Mermaid diagram supplements rather than replaces readable text.
- [x] The explanation covers the selected scope with examples supported by the material and source references at available precision.
- [x] Multi-topic exports preserve topic boundaries and include only supported cross-topic relationships.
- [x] Missing, conflicting, or inaccessible material is identified. Authorized external additions remain clearly distinguished from supplied sources.
- [x] Export scope and provenance are recorded so later agents can identify which topics and materials the documents cover.
- [x] Regeneration preserves originals and does not silently overwrite unrelated exports or user edits.
- [x] The skill does not claim to generate audio, podcasts, or video directly, or to guarantee compatibility with every third-party service.
- [x] Document observable acceptance evidence and remaining gaps; do not create automated tests or Git commits without explicit authorization.

## Outcome

Implemented as instructions and a versioned paired-export contract. Checked criteria indicate implementation coverage, not exercised learner sessions. See [evidence and gaps](../verification-05.md). Both independent review axes reported no actionable findings. The user subsequently authorized this ticket's commit before implementing tickets 06 and 07; no tests or push were authorized.
