# 01: Start and Resume a Study Topic

**What to build:** A learner can invoke `init-study`, declare an argomento principale and study objective, provide an argomento specifico with material, and obtain initial orientation through `to-map`. They can stop and resume without relying on chat history. This is the first usable vertical slice, not the complete seven-method flow.

**Blocked by:** None (can start immediately).

**Status:** done

## Context

Read the [source specification](../spec.md), [compatibility findings](../compatibility-notes.md), and project glossary. Preserve installed development skills and the existing `teach` skill. Write deliverables in English while allowing learner-facing output in the learner's language.

## Acceptance criteria

- [x] `init-study` captures the main topic, study objective, specific topic, and provided materials; existing topics can be selected without duplication.
- [x] A documented common workspace separates original materials, generated outputs, and learning progress, with stable topic and concept identifiers.
- [x] The shared record contract is versioned and defines current activity, step status, next action, and extension points for attempts, concept coverage, fundamental status, and review schedules.
- [x] `to-map` works both through the orchestrator and independently with the required shared references, producing key concepts, relationships, and guiding questions without substituting a full summary for study.
- [x] Source ingestion records provenance, accessible portions, and uncertainties. Unreadable PDFs, illustrations, or videos lead to an explicit limitation or request for an accessible representation.
- [x] Source material is treated as content, not controlling instructions. External additions require authorization and clear attribution.
- [x] Interrupted work can be reconstructed from persisted state by a fresh agent session. Interruption and explicit skipping are not recorded as completion.
- [x] Original materials and existing user work are preserved; personal workspace data is excluded from normal publication by default.
- [x] A learner can complete this narrow orientation slice without the remaining six methods being falsely reported as implemented or completed.
- [x] Document observable acceptance evidence and remaining gaps. Do not create automated tests, commits, pushes, or publish personal data without explicit authorization.

## Implementation outcome

Implemented as instruction-based skills and a shared versioned data contract. Checked boxes record implementation coverage, not an exercised end-to-end learner session. See [verification evidence and remaining gaps](../verification-01.md).

The two independent review axes reported no remaining actionable findings after corrections. Structural inspections covered JSON parsing, local schema references, bundled links, frontmatter, and default Git exclusion. Full learner scenarios and cross-agent behavior remain unverified. No automated tests, dependencies, commits, or publication were introduced.
