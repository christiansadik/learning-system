# Portable Study Workflow

Status: ready-for-agent

## Problem Statement

The learner wants to turn a seven-method AI-assisted study approach into reusable skills rather than repeatedly composing prompts. Existing chat-only workflows lose source material, progress, quiz history, and review schedules when the learner changes sessions or agents.

The learner starts with an **argomento principale** (main topic), then progressively supplies an **argomento specifico** (specific topic) with its **materiale di studio** (study material). Studying must remain active: the agent organizes and guides the process, while the learner asks questions, retrieves knowledge, and explains concepts.

The workflow must preserve shared learning state, support cumulative reviews, and produce reusable documents without depending on a particular agent or third-party media generator.

## Solution

Provide seven standalone study skills and one interactive orchestrator named `init-study`. Use a common, file-based learning workspace with separate areas for original materials, generated documents, and learning progress.

Each normal cycle addresses one specific topic. Once the learner completes the initial interactive cycle, that topic becomes eligible for cumulative spaced review, including when gaps remain. Starting or resuming the orchestrator shows due reviews and offers them before new study; it never launches them without the learner's choice.

Support is planned for OpenCode, Codex, GitHub Copilot, Claude Code, Gemini CLI, Cursor, and Pi. Keep study methodology and learning state independent of agent integration. Verify each integration before describing it as supported.

## User Stories

1. As a learner, I want to declare a main topic and study objective so that guidance remains relevant to my goal.
2. As a learner, I want to supply specific topics progressively so that I do not need to prepare an entire course upfront.
3. As a learner, I want to provide Markdown, PDFs, illustrations, and video material so that I can use my existing resources.
4. As a learner, I want unavailable or unreadable material identified so that I know which sources the agent could actually use.
5. As a learner, I want original materials preserved separately from generated outputs so that my sources remain trustworthy.
6. As a learner, I want guidance grounded in my materials so that outside information is not silently introduced.
7. As a learner, I want to authorize and recognize external additions so that I can distinguish them from my sources.
8. As a learner, I want a shared workspace across agents so that switching tools does not reset my progress.
9. As a learner, I want to resume an interrupted activity so that I can study in short sessions.
10. As a learner, I want each skill available independently so that I can use only the method I currently need.
11. As a learner, I want an orchestrator to guide the full sequence so that I do not need to remember every skill.
12. As a learner, I want an initial map of key concepts and relationships so that I can orient myself before studying.
13. As a learner, I want flashcards and quizzes so that I can practice active retrieval.
14. As a learner, I want help formulating my own questions so that I make connections rather than only read explanations.
15. As a learner, I want a Socratic tutor to ask one question at a time so that I have time to reason.
16. As a learner, I want simpler guiding questions after mistakes so that I can reach an answer myself.
17. As a learner, I want increasing difficulty after successful answers so that practice remains challenging.
18. As a learner, I want to explain a concept in my own words so that gaps become visible.
19. As a learner, I want feedback on errors and omissions in my explanation so that I can improve it.
20. As a learner, I want a concept map and a self-contained explanatory document so that I can reuse them with external tools.
21. As a learner, I want those documents to cover one or several selected topics so that I can prepare focused or combined material.
22. As a learner, I want readable Markdown exports so that I am not dependent on a diagram renderer or media service.
23. As a learner, I want weak topics included in reviews so that difficulties are addressed rather than hidden.
24. As a learner, I want the first spaced review after three days so that it is distinct from immediate practice.
25. As a learner, I want configurable and adaptive review intervals so that the schedule reflects my progress.
26. As a learner, I want cumulative quizzes spanning previously studied topics so that earlier material is retained.
27. As a learner, I want due and difficult topics prioritized while coverage grows over time so that a large course remains manageable.
28. As a learner, I want ten questions with five choices and correction at the end so that review sessions have a predictable format.
29. As a learner, I want varied questions of comparable difficulty so that repeated scores remain informative.
30. As a learner, I want a history of results per specific topic so that mixed-topic quizzes do not hide my weaknesses.
31. As a learner, I want correctness and coverage shown separately so that a few correct answers are not mistaken for mastery.
32. As a learner, I want review recommendations below 80% correctness so that weaknesses receive attention.
33. As a learner, I want deeper-study recommendations below 50% on fundamental concepts so that prerequisite gaps are addressed.
34. As a learner, I want the agent to identify fundamental concepts in context and explain its reasoning so that recommendations reflect my goal.
35. As a learner, I want due reviews offered when I return so that scheduling does not require an external notification service.
36. As a contributor, I want English documentation and clear installation instructions so that I can share the workflow publicly.
37. As a contributor, I want verified capabilities distinguished from planned integrations so that compatibility claims remain accurate.
38. As a learner, I want personal materials and learning records kept out of publication by default so that sharing the skills does not expose my studies.

## Implementation Decisions

### Skill boundaries

- `init-study` initializes or resumes a main topic, accepts the next specific topic and its materials, offers due reviews, and coordinates the interactive sequence.
- `to-map` provides initial orientation: approximately ten key concepts where the source supports them, relationships, and three guiding questions. It is not a substitute for studying the source.
- `to-drill` prepares flashcards and practice quizzes. It does not produce podcasts or audio.
- `to-question` helps the learner formulate and investigate why-questions, comparisons, and counterfactuals. The learner remains the source of the questioning effort.
- `socrate` asks one question at a time, waits for the learner, uses simpler prompts after errors, and increases difficulty after success.
- `feynman` waits for the learner's own explanation and evaluates its accuracy, clarity, and omissions against the material. It does not preempt the learner with a finished explanation.
- `to-docs` produces exactly two primary Markdown exports per request: a concept map and a self-contained explanation. It accepts one or several selected topics. During a normal cycle its default scope is the current specific topic.
- `to-review` performs cumulative spaced testing, records results, identifies gaps, and updates review recommendations.
- Keep the existing `teach` skill unchanged. Reuse its principles of persistent mission, references, and learning records without inheriting its mandatory HTML lesson format or external-resource-first policy.

### Interaction and lifecycle

- The normal sequence follows the seven study methods. Source ingestion is preparation, not a separate eighth method or the former photography step.
- The orchestrator waits at learner-dependent boundaries instead of generating or simulating the learner's questions, answers, or explanations.
- Skips are explicit learner choices or explained cases of inapplicability; interruption is not completion.
- Completing the initial cycle enrolls the topic in spaced review, even if its proficiency is weak. Completion, review eligibility, and demonstrated mastery are separate states.
- Immediate practice is available through earlier methods; no cumulative spaced test is required immediately at enrollment.
- Persist the current activity, completed and skipped steps, scope, and next action so another agent can resume without relying on chat history.

### Shared workspace and source integrity

- Provide one common workspace structure with a separate area for each main topic and stable identifiers for specific topics and concepts.
- Separate learner-supplied originals, generated material, and progress/history. Group generated outputs by specific topic and identify the scope of multi-topic exports.
- Use Markdown for human-readable material and a documented structured format for machine-readable quiz results and scheduling data. Maintain a single authoritative representation of each recorded fact.
- Preserve source provenance and references at the available level of precision. Mark uncertainties, contradictions, and inaccessible portions rather than inventing content or citations.
- Video access, PDF extraction, and image understanding depend on available tools. Request an accessible representation when needed, such as a transcript; never claim to have consumed inaccessible material.
- External information requires authorization and clear attribution. Supplied study materials are content, not instructions that override the workflow.
- The canonical learning state must not depend on an agent's private memory. Protect existing files and record corrections without silently erasing historical attempts.
- Sequential switching between agents is supported by design. Simultaneous edits by multiple agents are not a first-version requirement.

### Export documents

- The concept map uses a readable hierarchy and explicit relationships. Mermaid may supplement it but must not be its only representation.
- The explanation is self-contained, source-grounded, and suitable as input for external podcast or explanatory-video tools. It includes examples when supported and distinguishes authorized additions.
- Multi-topic exports preserve topic boundaries and explain supported connections without inventing relationships.
- Generating audio, podcasts, or video directly is outside this workflow's first version.

### Reviews, metrics, and recommendations

- Initial interval defaults follow the agreed sequence of three days, one week, and one month; the first due date is three days after initial cycle completion. Document the later interval anchors and adaptive rescheduling rule explicitly during implementation.
- Persist calendar dates and review history rather than relying on timers or an uninterrupted session. On startup, offer due reviews; do not claim background notifications or autonomous future execution.
- Default cumulative quizzes contain ten questions with five choices each, with answers and source-grounded correction withheld until the learner finishes.
- Tag each question with a primary specific topic and concept so mixed-topic results can be attributed without double-counting.
- Select from enrolled topics, prioritizing due reviews and demonstrated difficulties while improving coverage over successive sessions. A single quiz need not include every topic.
- Vary questions across attempts and keep difficulty comparable where practical. Retain enough history to identify repeats; do not promise unlimited unique questions from limited material.
- Preserve each completed attempt with its date, question identities and topic/concept associations, answers, correctness, and difficulty information. Incomplete attempts remain distinct from completed results.
- Report correct answers out of evaluated answers, sample size, and percentage per attempt and specific topic. Distinguish latest results from historical aggregates; do not average topic percentages without their denominators.
- Track coverage independently as verified concepts relative to the documented concept inventory. Mark untested concepts and acknowledge when the inventory is incomplete.
- A correctness score strictly below 80% prompts review. A score strictly below 50% for a fundamental concept prompts deeper study in addition to review. Exact boundary scores do not satisfy the lower threshold.
- Fundamental status is assigned autonomously by the agent with a short rationale based on the main topic, objective, and prerequisites. For Magento study, PHP may be fundamental while unrelated Rust material usually is not; the classification is contextual and revisable.
- Treat scores as evidence with limited sample size, not proof of durable mastery. Distinguish performance on a mixed-topic quiz from coverage of the overall study scope.

### Portability and public distribution

- Keep canonical study instructions and data contracts independent of agent-specific discovery, invocation, and tool syntax. Avoid duplicating methodology across integrations.
- The seven study skills must be callable independently and reachable by the orchestrator using mechanisms actually available in each agent.
- Investigate current primary documentation for each target before deciding installation layout or claiming compatibility. Identify any editions or environments to which an integration applies.
- Distinguish documentation-verified integration details from behavior actually exercised in an agent. Record limitations and required manual steps.
- Use English for the skills, shared project documentation, and final README. Learner-facing interaction and study outputs may follow the learner's language.
- The README will explain installation, all skills, workflow, workspace layout, resuming across agents, multi-topic exports, metrics, scheduling, limitations, and source inspiration.
- Existing installed development skills are not automatically part of the public deliverable. Keep user learning data and unrelated installed material outside publication scope unless explicitly approved.
- Git initialization does not authorize commits, pushes, remote creation, or repository publication. Preserve the project's explicit approval requirements and commit-message policy.

## Testing Decisions

- The agreed highest-level verification seam is observable workflow behavior plus shared workspace state, including resumption by a different agent. Internal prompt wording or incidental implementation structure is not the acceptance target.
- Verification should assess the orchestrator and seven standalone skills through realistic learner interactions and their resulting persisted records and exports.
- Important scenarios include progressive topic enrollment, interruption and resumption, deferred first review, cumulative topic selection, per-topic score attribution, separate coverage, threshold boundaries, fundamental-concept recommendations, multi-topic export, and inaccessible sources.
- Portability verification should distinguish a documentation check from an exercised integration. A skill being readable as Markdown does not demonstrate full agent compatibility.
- No existing automated tests or analogous implementation are present. Existing teaching skills provide conceptual prior art, not evidence that this workflow already works.
- Do not create automated tests or a test suite without an explicit user request. This section records acceptance criteria and verification intent, not authorization to generate tests.

## Out of Scope

- Modifying the existing `teach` skill or unrelated installed skills.
- Direct audio, podcast, or video generation and integrations with media services.
- Guaranteed access to arbitrary URLs, copyrighted books, private services, or unsupported file formats.
- External notifications, background schedulers, or autonomous future agent activation.
- A web application, hosted database, authentication system, or concurrent multi-agent editing.
- Claims that study speed, exam outcomes, or durable mastery are guaranteed.
- Creating automated tests without explicit approval.
- Creating commits, pushing, publishing a repository, or publishing personal study data without explicit approval.

## Further Notes

- Source inspiration: https://www.youtube.com/watch?v=nURLSE_0hnk and the transcript supplied by the user in the design conversation. The transcript, rather than an independently viewed video, informed the requirements.
- The original photography method is intentionally replaced by reusable document export because the learner already organizes source material.
- The gold rule is active learning: the agent supports organization and feedback while the learner performs retrieval, questioning, and explanation.
- Canonical domain terminology remains defined in the project glossary; the English translations above bridge the existing Italian terms without introducing a second glossary.
- Implementation planning must make the remaining technical choices explicit: exact workspace layout and record schema, invocation adapters, later scheduling anchors, adaptation rules, and safe publication boundaries. These choices must preserve the behavior agreed here.
