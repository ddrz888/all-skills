# Session style

The upgraded prompt always ends with a Session Style section. It controls how much the run talks, not how much it does. Default is lite. The user gets verbose only by asking for it.

## Lite (default)

Paste this paragraph as the Session Style section unless the user asked for verbose:

```
Session Style: Run lite. No filler, no hedging, no pleasantries, no narration of tool calls or of what you are about to do. Full sentences, exact technical terms, exact numbers and error strings. Report only at milestones and in the final verification report: what passed, what failed, what you fixed, what is unverified. Switch to full detail only for a security warning, an irreversible action, or a step where compression would make the order ambiguous, then return to lite. Deliverables themselves (documents, code, comments, messages to other people) are written in normal prose.
```

What lite keeps: articles, grammar, complete sentences, every technical fact. What lite drops: preamble ("Sure, I'll start by"), progress narration ("Now I'm going to run the tests"), hedging ("this should probably work"), recap of what the user already knows, decorative tables and emoji.

Lite is the "lite" level of the open-source caveman skill, written out here so this skill has no dependency on it.

## Verbose (only on request)

Use when the draft or the user says "walk me through", "explain your reasoning", "show your work", "keep me posted", "narrate", or names a learning goal. Paste:

```
Session Style: Run verbose. Explain your reasoning before each significant decision, report progress at each step, and state what you checked and why. Keep deliverables themselves in normal prose.
```

## Why this matters

A long autonomous run in default verbosity spends tokens narrating instead of working, and the user reads the narration instead of the result. Lite moves the reporting to the two places it matters: milestones and the verification report. The auto-clarity exceptions (security, irreversible actions, ambiguous ordering) exist because a compressed warning is worse than a wordy one.
