# Synthetic Usage Examples

All topics, paths, and requests below are illustrative. They are not real learner records, executed demonstrations, bundled source files, or passing compatibility results. Replace paths/materials with your own and use the invocation syntax documented for your agent.

## Start with a main topic

OpenCode example:

```text
@init-study
Main topic: Magento.
Goal: develop custom modules, not prepare for an exam.
Workspace: /path/to/my-study-project/study.
Language: Italian.
```

The agent can record the mission while waiting for a specific topic. It should not invent chapters or answer an exercise on your behalf.

## Add topics progressively

```text
First specific topic: dependency injection.
Here are my Markdown notes and the PDF section to use.
```

After completing that cycle:

```text
Next specific topic: events and observers.
Here is the material for this topic. Keep the earlier topic in the review pool.
```

An unreadable source should produce a concrete request for a transcript, file, or narrower accepted scope, not a fabricated summary.

## Pause, then resume in another agent

```text
Pause here and save the current activity and exact pending question.
```

Close or pause the first agent. In Codex, against the same project and workspace:

```text
$init-study Resume /path/to/my-study-project/study and show the saved pending activity before continuing.
```

This illustrates the intended handoff contract, not a locally verified Codex session. If a review is offered first, you can ask to continue the saved activity instead without moving due dates.

## Choose a due review

```text
Show the due topics. Review the nonconflicting due scope first, then return to my interrupted study activity.
```

The agent should preserve the teaching checkpoint, save the accepted review scope, wait for actual quiz answers, and restore the checkpoint afterward. If those topics have conflicting active work, it should ask rather than abandon it silently.

## Export multiple topics

Claude Code example, after installing its native bundle:

```text
/to-docs Create the concept map and explanatory document for t001 and t002 in /path/to/my-study-project/study. Use only their supplied sources, label missing connections, and preserve previous exports.
```

Expect two Markdown paths from one versioned export record, not an audio/video file or automatic upload. New combined documents do not complete the other topics' study gates merely by including them.

## Use a method independently

Pi example:

```text
/skill:feynman I will explain dependency injection in my own words. Use the supplied topic material, wait for my explanation, then identify errors and gaps.
```

The agent should initialize/reuse source-grounded state, wait for your explanation, and save feedback without requiring that you first run every predecessor skill. An independent request is not permission to auto-run the whole flow.
