# Literature Review Outline: Thesis Statement and Structure

*Drafted 12 Nov 2026 with Claude. The thesis layout agreed with the advisor by email is mostly a literature review, so pilot prompts aren't strictly needed.*

> **Note:** `CLAUDE.md`, `thesis-plan.md` and `proposal.md` still describe the earlier empirical design (corpus study and student pilot). They should be reconciled with this format.

## Working thesis statement

> Although high-level programming languages and AI-assisted development have made software creation increasingly accessible, their reliance on underlying native-code implementations introduces persistent memory-safety challenges. The long-term security and maintainability of these systems depend not only on improvements in automated tools but also on preserving the systems-programming expertise necessary to identify, understand, and remediate vulnerabilities within their underlying C and C++ components.

## Feedback on the statement

The two sentences split well. The first gives the premise: high-level code still depends on C and C++ underneath. The second makes the claim: we still need people with systems-programming expertise.

1. **Give the counter-position a name and answer it.** The strongest objection is that we can rewrite in memory-safe languages like Rust and let tools find the bugs. Examples of those tools are fuzzing, sanitizers, hardware like CHERI and MTE, and AI bug-finders like Google's Big Sleep. The thesis gets sharper when it explains why that isn't enough:
   - The amount of old C/C++ code is huge, and rewriting it is slow.
   - Memory-safe code still calls into C through `unsafe` blocks and foreign-function interfaces.
   - Every automated tool needs a person who can check its findings and fixes.
2. **"Preserving" assumes the expertise is shrinking, so the literature has to show that.** Bring in sources on deskilling, on over-trust in AI-written code, and on what CS programs teach now.
3. **Phrase it as a question too.** Possible research question:
   *"To what extent can automated tools replace human systems-programming expertise in keeping native-code dependencies memory-safe?"*
   The statement then becomes the answer.
4. **"Maintainability" is a second claim.** Either back it with a source or two on open-source maintainer burnout (the 2024 xz-utils backdoor is a good example), or drop the word so the thesis stays focused on security.

## Possible structure

1. **The stack under the language.** CPython, the JavaScript engines in browsers and Node, NumPy and PyTorch native code, OpenSSL, libc. "Memory-safe" apps rest on C/C++. (For NumPy's native-code share, state the counting rule: Yang & Cai say 38%, our own count was 55.7%.)
2. **Why memory safety keeps coming back.** Microsoft and Chromium both report that about 70% of their serious vulnerabilities are memory-safety bugs. Also the CWE Top 25 and Heartbleed. Policy: the NSA's 2022 memory-safety guidance and the White House ONCD report *Back to the Building Blocks* (Feb 2024).
3. **What's being done about it, and where each fix falls short.** Moving to memory-safe languages (Google's Android reports on Rust adoption), hardware protections (CHERI, MTE), sanitizers and fuzzing, and AI-driven detection and repair.
4. **AI-assisted development and security.** Pearce et al. 2022 ("Asleep at the Keyboard"). Perry et al. 2023: people using AI assistants wrote less secure code but felt more confident. Automation bias.
5. **Expertise and how it wears away.** Bainbridge, "Ironies of Automation" (1983): the more automated a system gets, the more it depends on rare human skill for the cases automation misses. Add sources on deskilling and on what CS programs teach. The shrinking junior-developer apprenticeship fits here too.
6. **Synthesis.** Humans who can read and fix native code remain a dependency that tools don't remove. The L1/L2/L3 memory-model literacy construct (managed model / manual model / boundary contract) can organize the argument here, as a framework rather than a study.
7. **Normative close.** The transhumanism section using *Magnifica Humanitas*: keeping this expertise lets people check AI's work, so AI adds to human ability instead of replacing it. Keep the normative claims clearly separate from the literature findings.

## To do

- [ ] Check every citation above against the original source, especially exact figures and dates (Google updates its Android Rust numbers every year).
- [ ] Decide whether to keep "maintainability" in the thesis statement.
- [ ] Write the research question into the introduction.
- [ ] Reconcile `CLAUDE.md`, `thesis-plan.md` and `proposal.md` with the literature-review format.
