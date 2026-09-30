# The Four Rules (condensed from Nate Herk, AI Automation Society)

Source: "How Anthropic Actually Prompts Fable 5.1" by Nate Herk. Video: https://youtu.be/FBVNS1l5Vb8. Free community discussion: https://www.skool.com/ai-automation-society/new-video-how-anthropic-actually-prompts-fable-51?p=35dd3c14. Full guide (AIS Plus members): https://www.skool.com/ai-automation-society-plus/new-video-how-anthropic-actually-prompts-fable-51?p=b01132a1&ref=19944f44610a4d36a91c33f2c97b3f65. This file is a condensation; the guide has the full text and the Anthropic documentation it cites.

Core principle: give Fable a clear finish line, choose the right effort, require evidence, and let independent work happen at the same time.

## Rule 1: Define done, then tell it to finish

Give a destination, not a task list. The finish line has four parts:

- Outcome: the completed result you want to receive.
- Context: why the work matters and who it is for.
- Definition of done: the observable conditions the result must satisfy.
- Constraints: the genuine boundaries Fable must respect.

Why fewer instructions can be better: Fable 5 and 5.1 have strong instruction following and can often choose a better method when given the goal and boundaries without every move scripted. Skills and prompts written for older models tend to over-prescribe steps.

Why the completion instruction matters: Fable 5.1 can execute very long tasks with little methodological guidance when the goal is clear, but it can still stop after describing its next step or ask permission for work already authorized. An explicit completion instruction prevents repeated "continue" prompts.

Anthropic guidance cited: "When you have enough information to act, act." (Fable 5) and "Finish the whole task." (Fable 5.1)

Template:
- Goal: Here is the outcome I need and why it matters: [goal and context].
- Success: The work is complete when: [definition of done].
- Completion: Complete this end to end. Make routine reversible decisions yourself. Do not stop with a plan or ask permission for steps already included in the request.

## Rule 2: Match the effort to the task

Effort controls how much intelligence, time, and token usage Fable applies. The highest setting is not automatically best.

The effort ladder:

| Level | Use for |
|---|---|
| Low | Simple extraction, classification, brainstorming, routine transformations |
| Medium | Routine research, document work, spreadsheet work, normal coding |
| High | Recommended starting point for complex or consequential work |
| X high | Difficult reasoning where the user's own tests show a meaningful quality improvement |
| Max | Exceptional work where capability matters more than latency or usage |

Decision rule: start at high. Test the same representative task at medium. If quality holds, try low. Move to xhigh or max only when the additional reasoning produces a better usable result. Anthropic reports medium Fable 5.1 roughly matches Fable 5 at lower cost; the user's own repeatable examples matter more than anyone else's preferred setting.

Caveats:
- Low effort is less likely to call search or retrieval tools and more likely to answer from memory. Raise effort for turns where current research or careful retrieval matters.
- X high and max can spend extra tokens thinking before a long written deliverable. High may be more efficient for long documents when higher settings do not improve quality.
- Effort can be changed mid-conversation in supported interfaces, so a prompt can direct different effort for different phases.

Template:
- Effort: Use the lowest effort level that reliably produces the required quality. Increase effort for difficult reasoning and reduce it for routine execution.

## Rule 3: Require verification, not confidence

The model saying something works is not proof. Build a verification loop that checks the output the way a capable human reviewer would.

The human review test: ask what you would do if a person handed you the result and claimed it was finished.

| Output type | Reviewer check |
|---|---|
| Website or landing page | Open it, click the controls, inspect mobile behavior, capture screenshots |
| Research | Open the sources, check dates, verify important claims |
| Interface or app | Exercise the important user paths, inspect failure states |
| Video | Watch the rendered result, check transitions, timing, visual errors |
| Document or report | Compare it with the brief, inspect the rendered pages |
| Code | Run the build and tests, exercise the change, read the diff |
| Spreadsheet or data | Tie totals to source, spot-check rows at the tails, confirm formulas recalc |

Objective vs. subjective quality: some outputs have objective tests (build passes, value equals target). Others need judgment (design feels premium, message is persuasive). For subjective work, define the quality criteria before asking Fable to judge, so it has a standard to apply repeatedly instead of vague confidence. Quality standard = what good looks like, how it will be inspected, and which failures require another revision.

The verification loop:
1. Produce the first complete version.
2. Compare it with the specification and quality criteria.
3. Identify concrete defects or unsupported claims.
4. Fix the defects and repeat the checks.
5. Stop only when the checks pass or the remaining uncertainty is clearly disclosed.

Separate verifier agents provide fresh context and catch what the original agent overlooks. Anthropic reports evidence-based progress reporting nearly eliminated fabricated status reports in its testing: failed tests, skipped steps, and unverified work get reported plainly, not hidden behind a confident completion message.

Vision verification: for charts, websites, slides, and other visual work, have Fable inspect the real rendered output iteratively. Cropping and enlarging specific regions finds details a single broad screenshot hides.

Anthropic guidance cited: "Only report work you can point to evidence for." (Fable 5) and "Verify your work however you like." (Fable 5.1)

Template:
- Verification: Before calling this complete, test the result using the same checks a capable human reviewer would use. Show what passed, what failed, what you fixed, and anything that remains unverified.

## Rule 4: Parallelize and delegate independent work

Parallelization: running independent operations at the same time (searches, file reads, checks). Delegation: assigning a substantial independent workstream to another agent while the lead agent keeps coordinating.

Assembly line model: one process does not require one agent to do every step. Independent pieces can be assigned to separate agents, completed simultaneously, and combined by a lead at the end.

Benefits: faster completion, narrower focus per agent, broader coverage, cleaner lead context, less waiting.

When not to delegate:
- Do not parallelize steps that depend on earlier results.
- Do not delegate a task that can be completed in a few simple tool calls.
- Do not split work that requires constant shared context.
- Do not create so many agents that coordination costs exceed the benefit.

Lead agent strategy: Fable operates as the strategist. It defines workstreams, dispatches agents, interprets results, starts follow-up work, and performs the final quality pass. This reserves the strongest reasoning for direction and judgment.

Accountability rule: delegation does not transfer responsibility. The lead agent still owns the final result and must verify the combined output before delivering it.

Anthropic guidance cited: "Parallel subagents." (Fable 5) and "Batch independent tool calls in agent loops." (Fable 5.1). Unnecessary sequential tool turns increase tokens, round trips, and elapsed time without improving answer quality.

Template:
- Execution: Identify which parts of this task are independent. Run independent tool calls at the same time. Delegate substantial independent workstreams when useful, continue productive work while they run, and keep dependent operations sequential.

## Master prompt (all four rules)

- Goal: Here is what I need to accomplish and why it matters: [goal and context].
- Definition of Done: The work is complete when: [observable success criteria].
- Completion: Complete the task end to end. Make routine reversible decisions yourself. Stop only for a destructive action, a material scope change, or information only I can provide.
- Effort: Use the lowest effort level that reliably produces the required quality. Increase effort for difficult reasoning and reduce it for routine execution.
- Verification: Check every material result before calling the task complete. Correct failures and clearly disclose anything unverified.
- Execution: Run independent operations at the same time. Delegate substantial independent workstreams and continue useful work while they run.

## Quick checklist

- Is the final outcome unambiguous?
- Does Fable know why the work matters?
- Are the success criteria observable?
- Is the effort level appropriate for the difficulty?
- Is there a real verification method?
- Which workstreams can run independently?
- Does the lead agent remain responsible for the combined result?
