# Ticket 09: Evidence and Limitations

Baseline: ticket 08 commit `ef920e5`. Implementation: documented native filesystem routes for Claude Code, Gemini CLI, Cursor local Agent chat, and Pi using the existing canonical installer and state contract. No host-specific teaching copies or configuration edits were authored.

Official sources were retrieved through Context7 and direct documentation pages. Claude Code reported version 2.1.161, but no session or native skill was launched. Gemini/Pi CLIs and Cursor's CLI entrypoints were not on PATH; Cursor editor availability was not inferred from that result. The Gemini product transition notice was retained as an account/product limitation rather than silently changing the target.

Installation observations cover a fresh 18-file `.claude/skills` copy layout and an independent 11-file `to-docs` selection with all shared references. These do not demonstrate native agent interpretation or a learner-state handoff. No real study source/state, agent install/update, login, model prompt, automated tests, push, or publication was created.

The [public integration evidence](../../docs/integrations/evidence.md) remains authoritative for exercised vs documentation-only behavior. Real sequential handoff and all four native teaching integrations remain unverified acceptance gaps, not passing claims.

Independent Standards and Spec reviews reported no actionable implementation defects and explicitly retained those verification limitations.
