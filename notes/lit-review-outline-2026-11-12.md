# Literature Review Outline: Thesis Statement and Structure

*Drafted 12 Nov 2026 with Claude. The thesis layout agreed with the advisor by email is mostly a literature review, so pilot prompts aren't strictly needed.*

> **Note:** `CLAUDE.md`, `thesis-plan.md` and `proposal.md` still describe the earlier empirical design (corpus study and student pilot). They should be reconciled with this format.

## Working thesis statement

> Although high-level programming languages and AI-assisted development have made software creation increasingly accessible, their reliance on underlying native-code implementations introduces persistent memory-safety challenges. The long-term security and maintainability of these systems depend not only on improvements in automated tools but also on preserving the systems-programming expertise necessary to identify, understand, and remediate vulnerabilities within their underlying C and C++ components.

**Refined central argument (13 Nov):** see section 6. Not every developer needs to understand the C layer, but the ecosystem needs enough specialists who do.

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

   **Answering "just use Rust."** Accept that Rust works, then argue that it isn't the whole answer:
   - *Rewriting is slow.* Even Google, one of the strongest Rust adopters, writes new code in Rust and leaves most old C/C++ in place. Android's memory-safety share fell below 20% in 2025 (Google 2025) mainly because new code is memory-safe, not because old code was replaced.
   - *Rust still calls C.* Unsafe Rust is more common than expected, and its main use is calling other unsafe functions, including C (Astrauskas et al. 2020). The same boundary risk shows up in scripting-language native extensions (Staicu et al. 2023).
   - *Rust code can still have memory bugs.* Google describes nearly shipping its first Rust memory-safety bug (Google 2025).

   Claim: memory-safe languages shrink the problem for new code, but the existing native layer and the boundaries into it still need people who can read C.

   **AI tools have the same limit.** AIxCC systems found 86% and patched 68% of planted bugs (DARPA 2025), and Big Sleep found a SQLite bug before release. But CodeMender's patches are all reviewed by a human before submission. The strongest AI security tools still depend on human experts.
4. **AI-assisted development and security.** Pearce et al. 2022 ("Asleep at the Keyboard"). Perry et al. 2023: people using AI assistants wrote less secure code but felt more confident. Automation bias.
5. **Expertise and how it wears away.** Bainbridge, "Ironies of Automation" (1983): the more automated a system gets, the more it depends on rare human skill for the cases automation misses. Add sources on deskilling and on what CS programs teach. The shrinking junior-developer apprenticeship fits here too.
6. **Synthesis.** Humans who can read and fix native code remain a dependency that tools don't remove. The L1/L2/L3 memory-model literacy construct (managed model / manual model / boundary contract) can organize the argument here, as a framework rather than a study.

   **Central claim (refined 13 Nov): the ecosystem needs specialists who understand what's under the abstraction.** This counters both "just use Rust" and "let the AI write it." Not every developer needs to understand C. But the system needs enough people who do, because someone must be able to check and fix what the tools produce. The claim is about how expertise is distributed, not about individual programmers, which keeps it pro-AI.

   How L1/L2/L3 fits:
   - Most developers can work at L1 (managed model) with AI help.
   - The ecosystem needs a smaller group at L2 (manual model) and L3 (boundary contract) who can check and fix the native layer.
   - The open question is how that group keeps forming. If junior roles shrink (Brynjolfsson 2025) and automation erodes rarely used skills (Bainbridge 1983), where do the next specialists come from? This is the education angle.

   Possible wording:
   > *Software built with high-level languages and AI tools still depends on C and C++. Not every developer needs to understand that layer, but the ecosystem needs enough specialists who do, because someone must be able to check and fix what the tools produce. Education and AI tool design should keep that specialist pipeline alive.*

   Support:
   - *Theory:* notional machines, simplified mental models of what the computer does underneath (see `notes/theoretical-grounding-two-transfers.md`). Spolsky's "Law of Leaky Abstractions" (2002) makes the same point informally; cite it as an essay, not research.
   - Bainbridge 1983: when automation fails, someone must understand the system well enough to step in.
   - Lee et al. 2025: limited domain knowledge made it harder for people to check AI output.
   - Shen & Tamkin 2026: developers who asked the AI for explanations kept their understanding. This is the pro-AI point: the problem is how AI is used, not AI itself.
   - Prather et al. 2024: struggling students overestimated how well they understood their code.
7. **Proposed research agenda (added 13 Nov).** The pitch: problem → framework (L1/L2/L3) → studies that would test it. These are proposed for future research, not run in the thesis.

   - **Study 2 (main): Can AI tools build understanding instead of replacing it?** Compare an AI assistant that explains what's happening in memory (refcounts, ownership, which allocator owns what) with one that only writes the code. Measure L2/L3 understanding afterward and on a later delayed test.
     - *Hypothesis (pro-AI):* AI designed to explain the memory model builds L2/L3 understanding. Shen & Tamkin 2026 support this: developers who asked for explanations kept their understanding.
     - *Skeptical view, built in:* AI help leads to dependence and weaker skills (Prather et al. 2024, illusion of competence; Lee et al. 2025, less critical thinking with more trust in AI). The study should be able to detect this: if the explaining assistant doesn't beat the plain one, or both groups overestimate their understanding, the skeptics are right for this setting.
   - **Study 1: Does understanding predict catching bugs?** Compare reviewers at different L1/L2/L3 levels on the same boundary code. This tests the framework directly and answers the counterfactual: what happens when someone *doesn't* understand the code.
   - **Study 3: How do specialists form today?** Interviews with maintainers of CPython, NumPy or similar projects about how they learned the C layer. Qualitative and feasible, and it speaks to the pipeline question.
   - **Study 4 (optional): What does AI leave behind at the boundary?** The original corpus study, as a technical baseline.

   Possible motivation line for the introduction (framed as why the question came up, not as evidence): *"I use AI daily to deepen my understanding, which raised the question of when it builds understanding and when it replaces it."*

8. **Normative close.** The transhumanism section using *Magnifica Humanitas*: keeping this expertise lets people check AI's work, so AI adds to human ability instead of replacing it. Keep the normative claims clearly separate from the literature findings.

## Sources by section

New entries are in `paper/refs.bib` (keys in brackets). Most were checked only against abstracts, official pages and news coverage, so verify figures in the originals.

1. **Stack:** Astrauskas et al. 2020 [astrauskas2020]. *Already in refs.bib:* staicu2023, huzhang2023, yangcai2026, lilicai2022.
2. **Memory safety:** Microsoft/Miller 2019 [miller2019], Chromium 2020 [chromium2020], ONCD 2024 [oncd2024]. *Already:* cisa2023. Microsoft counted patched CVEs and Chromium counted high-severity bugs, so they're similar findings, not the same measurement.
3. **Fixes and limits:** Google Android 2025 [google2025rust], DARPA AIxCC 2025 [darpa2025aixcc], DeepMind CodeMender 2025 [deepmind2025codemender]. Use DARPA's corrected AIxCC figures. The 20% and 1000× Android figures were only seen in secondary summaries.
4. **AI and security:** Lee et al. 2025 [lee2025]. *Already:* pearce2022, perry2023, sandoval2023, khalid2027.
5. **Expertise:** Bainbridge 1983 [bainbridge1983], Shen & Tamkin 2026 [shentamkin2026], Prather et al. 2024 [prather2024], Becker et al. 2023 [becker2023]. *Already:* almansoori2023, brynjolfsson2025. CS2023 curriculum: check what it says about memory safety before citing.
6. **Synthesis:** Spolsky 2002 [spolsky2002], plus the section 5 sources.

## To do

- [ ] Check every citation above against the original source, especially exact figures and dates (Google updates its Android Rust numbers every year).
- [ ] Decide whether to keep "maintainability" in the thesis statement.
- [ ] Write the research question into the introduction.
- [ ] Reconcile `CLAUDE.md`, `thesis-plan.md` and `proposal.md` with the literature-review format.
- [ ] Confirm the title of arXiv:2601.20245 (Shen & Tamkin) and the full author lists marked "and others" in `refs.bib`.
