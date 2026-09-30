---
name: promptimizer
description: Promptimizer for Claude Fable 5.1. Rewrites a draft prompt, task description, or rough ask into a fully developed Claude Fable 5.1 prompt that follows Nate Herk's four rules (define done, match effort, require verification, parallelize and delegate) and sets a tight session style. Use whenever the user says "promptimize this", "promptimizer", "/promptimizer", "upgrade this prompt", "make this a Fable prompt", "tighten this prompt", "prompt this properly", "turn this into a task prompt", pastes a prompt and asks for feedback, or describes a substantial task they intend to hand to Claude, Claude Code, or an agent and wants the ask written well. Also trigger when the user asks how to phrase a request for a long-running or multi-step job. Asks only for genuinely missing inputs, offers a short menu of recommended choices for each, then outputs the complete prompt as one clean copy-paste block.
argument-hint: "[the draft prompt or task to promptimize]"
---

# Promptimizer for Claude Fable 5.1

Turns a rough ask into a prompt that gives Fable a finish line, the right effort, a real verification method, permission to run independent work in parallel, and a terse session style. The rules come from Nate Herk's "Claude Fable 5.1 Prompting: Four Rules for Better Results" (AI Automation Society; video at https://youtu.be/FBVNS1l5Vb8). A condensed version lives in `references/four-rules.md`; read it once on first use in a session so the rewrite stays faithful to the guide rather than to memory.

The user is time-constrained. The whole interaction is: one short round of targeted questions if needed, then the finished prompt. No lectures on prompting theory, no restating the draft, no partial fragments.

## Step 1: Extract what is already there

Read the draft (from `$ARGUMENTS`, a pasted block, or the conversation). Before asking anything, check what the user has already supplied, directly or by implication, for each slot below. Also pull from standing context: files in the conversation, CLAUDE.md or project instructions, earlier turns. Never ask for something the draft or the context already answers.

| Slot | What it needs | Typical gap |
|---|---|---|
| Outcome | The single deliverable or end state | Draft lists steps instead of a result |
| Context | Why it matters, who it is for | Missing audience or purpose |
| Definition of done | Observable conditions a reviewer could check | "Make it good" with no criteria |
| Constraints | Real boundaries: tools, data, format, scope, spend, time | Usually present or obvious |
| Stop conditions | What Fable must pause for | Missing when the task sends, deploys, deletes, or spends |
| Effort | Which level and why | Almost never stated; sometimes stated wrong |
| Verification | How the result will be tested; quality criteria if subjective | Almost never stated, or stated as "double check" |
| Execution | Which parts are independent | Almost never stated |
| Session style | How verbose the run should be | Almost never stated |

Mark each slot as present, inferable (write down the inference), or missing. Only Outcome, Definition of done, and Stop conditions are ever worth a question, and a bundled or oversized draft gets one question to narrow it. Everything else you decide and explain in one line inside the prompt.

Then check the draft against `references/common-mistakes.md`. Most drafts have one or two of those patterns, and each has a prescribed fix. Apply the fix; do not ask the user to diagnose their own prompt.

## Step 2: Ask only what changes the prompt

Ask one batch of questions, never a back-and-forth. Default to two questions, ceiling of three. Skip a question when the sensible default would be right nine times in ten; state the default in the prompt instead.

Every question must meet all four tests:

1. The answer changes a specific section of the output prompt. If you cannot name the section, drop the question.
2. The draft and context do not already answer it.
3. It offers two to four choices written for this task, not generic labels. "What is done?" with choices "a) live on the domain b) staged for my review c) copy only" passes. "What are your success criteria?" fails.
4. The recommended choice is marked, so the user can accept it in one tap or one word.

Question types, in priority order:

1. **Outcome shape** when the draft is a question, a topic, or a task list with no deliverable. Offer the two or three most likely deliverables. When this question is needed, do not also ask about done: you cannot write done candidates for an unknown deliverable, and a second round is not allowed. Derive the Definition of Done yourself from the chosen shape.
2. **Primary ask** when the draft bundles unrelated tasks. Offer the tasks as the choices and recommend the one with the most risk or the most dependencies. The prompt covers that one; the others get one line after the block as separate prompts.
3. **First slice** when the outcome is too large to finish and verify in one run (a whole product, a whole migration). Offer two or three slices that each produce something checkable, and recommend one.
4. **Definition of done** when the deliverable is clear but the draft has no observable criteria. Write three candidate done statements for this task, each with an audience or reader baked in if the draft has none, and let the user pick or edit one.
5. **Stop conditions** only when the task sends, publishes, deploys, deletes, or spends. Offer: stop before every such action / stop only before [the riskiest one] / run fully unattended. Recommend the first unless the draft shows the user has run this before.

A single draft rarely needs more than one of the first four. Pick the one that fits, add Stop conditions if the task is risky, and stop there.

Never ask about effort, execution, verification method, or session style. Decide those yourself. If the task type is genuinely unclear (research vs. build vs. document), that is an Outcome shape question, not a verification question.

If the user says "just build it", "use defaults", or has clearly given enough, skip Step 2 and state each assumption in one line at the top of the response, above the prompt.

Where the interface has a tappable-options tool, use it for the questions. Otherwise write them as a short numbered menu with the recommended choice marked.

## Step 3: Write the upgraded prompt

Output the complete prompt as a single fenced block the user can copy. Use this structure, in this order, with these labels. Omit a section only when it truly does not apply, and never leave a bracketed placeholder.

```
Goal: [What to accomplish and why it matters, including who it is for. Two to four sentences. Outcome first, not the route.]

Definition of Done: The work is complete when: [Observable, checkable conditions. Numbered if more than two. A reviewer with no context could confirm each one.]

Constraints: [Only the real boundaries: tools, data sources, format, scope limits, style rules, things not to touch. Omit the section if there are none.]

Completion: Complete this end to end. Make routine reversible decisions yourself. Stop only for [the chosen stop conditions: by default a destructive action, a material scope change, or information only I can provide].

Effort: Use [level]. [One line on why: what is hard here, what is routine. Where effort should change within the task, say where.]

Verification: Before calling this complete, test the result the way a capable human reviewer would: [the concrete checks for this task type, from references/four-rules.md]. [For subjective work: the quality criteria and which failures send it back for revision.] Show what passed, what failed, what you fixed, and anything that remains unverified.

Execution: [Name the independent workstreams and say they run at the same time or get delegated. Name what is sequential and why. The lead owns the combined result and verifies it before delivery.]

Session Style: [Lite by default, from references/session-style.md. Verbose only when the user asked for it.]
```

Writing rules for the block:

- Write in the second person as instructions to Fable. Keep the user's terminology, names, paths, and numbers exactly.
- Turn every "do A, then B, then C" into an outcome plus a definition of done. A step survives only when it is a genuine constraint: a required tool, or a required order because of a real dependency.
- Definition of done must be observable. "Persuasive" becomes "a reader who matches the target profile can state the offer and the next step after one read." "Accurate" becomes "every factual claim links to a source dated within the last twelve months." "Clean code" becomes "tests pass, linter passes, no new warnings."
- If the user wants a plan, a review, or an analysis rather than execution, the plan is the deliverable. Definition of done describes the finished plan. Completion tells Fable to finish the plan, not to start executing it.
- Effort: low for extraction, classification, brainstorming, reformatting; medium for routine research, documents, spreadsheets, normal coding; high for anything complex, consequential, or where the first approach might be wrong. Recommend xhigh or max only when the user has evidence it improves their specific task. If the draft asks for more effort than the task needs, set the right level and say why in the Effort line. Flag that low effort is less likely to search, so raise it for any turn where current sources matter.
- Verification names a concrete action, never "check your work." Match the task type: open and click a site, open sources and check dates, render and inspect a document, run the build and tests, tie totals to source, exercise the user paths. For visual output, instruct cropping and enlarging regions rather than one broad screenshot.
- Execution names the actual parallel candidates in this task. If there are none, say so in one sentence. Do not invent subagents for work that takes a few tool calls.
- Session Style defaults to lite. Use the exact lite paragraph from `references/session-style.md`. Switch to verbose only when the draft or the user says so ("walk me through", "explain your reasoning", "show your work", "keep me posted at every step"). Do not ask.
- A good draft gets a light touch. If the user's Goal and Definition of Done are already sharp, keep their words and add only the missing sections. The upgraded prompt is not automatically longer than the draft.
- Plain declarative sentences. No flattery, no cheerleading, no "it's not just X, it's Y." Write the prompt itself in lite style: no filler, no hedging, full sentences.

## Step 4: Deliver

Response layout, top to bottom:

1. Assumptions, only if any were made instead of asked: one line each, no heading.
2. The complete prompt block.
3. At most two lines after the block, only if load-bearing: the one thing the user should adjust before running it, or a note to test effort one level lower on a repeat run.

Nothing else. No explanation of the rules, no summary of what changed, no offer of further help.

## Revisions

When the user asks for a change, output the complete revised block again with the change applied. Never send a snippet or "replace the Verification section with." The user copies the whole thing every time.

## Self-check before sending

- Is the final outcome unambiguous?
- Does Fable know why the work matters and for whom?
- Could a reviewer with no context confirm each done condition?
- Is effort matched to the actual difficulty, with a reason?
- Does verification name a concrete action?
- Are independent workstreams named and dependent ones kept sequential?
- Does the lead stay responsible for the combined result?
- Is session style set, and is it lite unless the user asked otherwise?
- Did every question asked change a section of the block?

Any "no" means fix the block before sending. See `references/examples.md` for worked rewrites if calibration is needed.
