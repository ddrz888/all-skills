# Worked examples

Three before-and-after rewrites showing the expected depth and the light touch on a good draft. Not templates to copy; they show how much a draft changes and how specific each section gets.

## Example 1: Task list to outcome (research plus build)

### Before

> Research voice agent solutions, find sources, pick the best options, organize the findings, write an offer, build a landing page, and deploy it.

### Gaps found

Outcome: inferable (a live landing page). Context: missing audience. Definition of done: missing. Stop conditions: missing, and the task deploys. Everything else: decide, do not ask. Mistakes matched: task list, no audience, risky action with no stop condition.

### Questions asked (one batch, two questions)

1. Done means: a) staged at a preview URL for my review before publish (recommended) / b) live on the production domain / c) copy and structure only, no build. Who is the buyer? Pick one: small business owners losing inbound calls / agencies reselling voice agents / our own sales team.
2. Stop before: a) publishing and any spend (recommended) / b) never, run fully.

User picked: a, small business owners, a.

### After

```
Goal: Build a landing page that sells our voice agent solution to small business owners who are losing inbound calls and want an AI receptionist they can trust. The page is the top of the funnel for this offer, so it must be credible, current, and persuasive to a non-technical buyer. Use current market research and our existing business context (positioning docs, pricing, past customer language) to decide what the page needs rather than following a fixed outline.

Definition of Done: The work is complete when:
1. A single-page site is staged at a preview URL, not published to the production domain.
2. A small business owner can state the offer, the pricing model, and the next step after one read.
3. Every factual claim about the market or competitors links to a source dated within the last twelve months.
4. The page renders correctly on mobile and desktop with no broken controls, missing images, or layout overflow.
5. The call to action submits and I receive the test submission.

Constraints: Use the brand palette and fonts from the brand kit in the project folder. No paid tool signups. No publish to production.

Completion: Complete this end to end. Make routine reversible decisions yourself (section order, headline variants, image selection). Stop only before publishing, before any spend, or if you need business information that is not in the project folder.

Effort: Use high for the research, positioning, and copy, where the first angle is often wrong. Drop to medium for the build and staging. Keep effort high for any turn that pulls current sources, since low effort tends to answer from memory instead of searching.

Verification: Before calling this complete, review the staged page the way a skeptical buyer and a front-end developer would: open it at phone width and desktop width, click every control, submit the form with a test entry, and screenshot each section, cropping and enlarging any region where text or images look off. Open each cited source and confirm the date and the claim. For persuasion, the standard is: the headline names the buyer's problem, the offer is stated in one sentence, one clear next step, no unexplained jargon. Any failure sends the page back for a revision. Show what passed, what failed, what you fixed, and anything that remains unverified.

Execution: Market research, competitor pricing scan, and pulling our internal positioning are independent; run them at the same time or delegate each to a focused agent. Copywriting depends on all three and stays sequential. Build depends on approved copy. A separate verifier pass with fresh context on the staged page is worth the cost here. You own the combined result and verify it before handing it to me.

Session Style: Run lite. No filler, no hedging, no pleasantries, no narration of tool calls or of what you are about to do. Full sentences, exact technical terms, exact numbers and error strings. Report only at milestones and in the final verification report: what passed, what failed, what you fixed, what is unverified. Switch to full detail only for a security warning, an irreversible action, or a step where compression would make the order ambiguous, then return to lite. Deliverables themselves (documents, code, comments, messages to other people) are written in normal prose.
```

## Example 2: Routine data task, no questions needed

### Before

> Clean up this week's leads export and load it into the CRM import template like last week.

### Gaps found

Outcome, context, constraints: present ("like last week" plus the template in the project). Definition of done: inferable from the template. Stop conditions: the task writes an import file but does not import; no risk. Mistake matched: none serious. The user has done this before, so no questions.

### After

Assumed: same template and dedupe rules as last week; the import itself is done by you, not by this run.

```
Goal: Turn this week's leads export into a completed CRM import file using the template and rules from last week's run, so the leads can be imported before Monday's outreach.

Definition of Done: The work is complete when the import file is in the output folder in the template's exact column order, every row has passed the duplicate check against last week's import and the CRM export, malformed emails and phone numbers are fixed or moved to an exceptions tab with a reason, and a summary tab shows rows in, rows out, and exclusions that tie exactly.

Completion: Complete this end to end. Make routine decisions yourself. Stop only if the export's columns do not match last week's layout.

Effort: Use medium. This is routine spreadsheet work with a known procedure. Raise to high only if the duplicate check returns a pattern that needs judgment.

Verification: Before calling this complete, tie the output row count to the input, open the first, last, and every exceptions row and confirm each against the source, and confirm the file opens with no formula errors. Report counts in, counts out, exclusions with reasons, and anything unverified.

Execution: The duplicate check and the format validation are independent; run them at the same time. File assembly depends on both. No delegation needed for a task this size.

Session Style: Run lite. No filler, no hedging, no pleasantries, no narration of tool calls or of what you are about to do. Full sentences, exact technical terms, exact numbers and error strings. Report only at milestones and in the final verification report: what passed, what failed, what you fixed, what is unverified. Switch to full detail only for a security warning, an irreversible action, or a step where compression would make the order ambiguous, then return to lite. Deliverables themselves (documents, code, comments, messages to other people) are written in normal prose.
```

## Example 3: Good draft, light touch

### Before

> Goal: Write the Q3 board update for our investors, who care most about net revenue retention and the two enterprise deals that slipped. Done when: it is under two pages, every number ties to the finance workbook in the project, the slipped deals each have a one-paragraph cause and a dated next step, and the ask of the board is stated in the first paragraph. Constraints: use the board memo template, no new charts.

### Gaps found

Outcome, context, done, constraints: all present and sharp. Missing: Completion, Effort, Verification, Execution, Session Style. No questions.

### After

```
Goal: Write the Q3 board update for our investors, who care most about net revenue retention and the two enterprise deals that slipped.

Definition of Done: The work is complete when the memo is under two pages, every number ties to the finance workbook in the project, each slipped deal has a one-paragraph cause and a dated next step, and the ask of the board is stated in the first paragraph.

Constraints: Use the board memo template. No new charts.

Completion: Complete this end to end. Make routine decisions yourself. Stop only if a number in the workbook conflicts with itself or if the cause of a slipped deal is not documented anywhere in the project.

Effort: Use high. The numbers are routine, but the framing of two slipped deals to a board is consequential and the first draft of that framing is usually wrong.

Verification: Before calling this complete, open the finance workbook and check every number in the memo against it, render the memo and confirm it fits in two pages in the template, and read the first paragraph as a board member would: the ask must be unmistakable. Show what passed, what failed, what you fixed, and anything that remains unverified.

Execution: Pulling the retention figures and pulling the two deal histories are independent; do them at the same time. Writing depends on both. No delegation needed.

Session Style: Run lite. No filler, no hedging, no pleasantries, no narration of tool calls or of what you are about to do. Full sentences, exact technical terms, exact numbers and error strings. Report only at milestones and in the final verification report: what passed, what failed, what you fixed, what is unverified. Switch to full detail only for a security warning, an irreversible action, or a step where compression would make the order ambiguous, then return to lite. Deliverables themselves (documents, code, comments, messages to other people) are written in normal prose.
```
