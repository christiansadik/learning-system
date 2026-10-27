# Orientation Map Format

Write in the learner's language. Save under the selected main topic's generated area for the specific topic, using the next unused `orientation-NNNN.md` filename.

## Required sections

1. **Scope and provenance**: main topic, specific topic ID/title, study objective, actual creation time, included source IDs and inspected portions, and any accepted partial scope. Mark external additions if authorized.
2. **Key concepts**: approximately ten when supported; each entry contains the stable concept ID, plain-language label, one or two orienting sentences, and source evidence with a real locator. Use fewer for narrow material and explain why. Preserve IDs from earlier maps for unchanged meanings.
3. **Relationships**: a readable hierarchy or explicit links between concept IDs, each briefly explained and supported by source evidence. Distinguish supported relationships from unanswered connections. A Mermaid diagram is optional, never the only map.
4. **Guiding questions**: three central questions the material can help the learner answer, associated with relevant concept IDs. Use fewer if the source is too narrow; do not pad or include ready-made answers.
5. **Limitations and next action**: inaccessible portions, uncertainties, contradictions, and the available continuation. Identify the orientation-only release boundary instead of claiming the chapter was learned.

Keep this short enough to read before study: no exhaustive explanation, full chapter summary, fabricated connections, answer key, score, or mastery claim. Later `to-docs` exports have a different purpose and are not implemented by this format.

An evidence reference may look like `[s001, heading "Constructor arguments"]` or `[s002, PDF page 4]` only when that heading or page was actually inspected. Concepts and relationships without a supporting source must be omitted or listed as open questions, not presented as established facts.
