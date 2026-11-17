# Thesis Outline (master)

**This is the one file to work from.** Merged 17 Nov 2026 from three files: the lit-review outline (12–13 Nov), the HUGS short-abstract outline (12–13 Nov) and the assembly plan (17 Nov). Those older files are still in `notes/` for history, but everything you need from them is here, organized by thesis chapter.

The only other working file is a chapter draft: [`draft/ch4-fixes-and-limits.md`](draft/ch4-fixes-and-limits.md), the paragraph-by-paragraph scaffold for chapter 4. New chapter scaffolds and drafts go in `draft/` as they're written.

**Legend:** ✅ in `paper/refs.bib` · ➕ needs adding to `refs.bib` · ⚠️ verify the figure or detail against the original

---

## Front matter

**Working title.** *Reviewing What You Never Wrote: Memory-Model Literacy and the Limits of Abstraction at the Python/C Boundary*. This adapts the old empirical title to the literature-review format; it can still change.

**Guiding question.**
> As AI becomes increasingly capable of writing and debugging software, what happens when both the developer and the AI are working with abstractions built on lower-level systems that the developer doesn't understand?

**Research question (the lit review answers this).**
> To what extent can automated tools, including AI, replace human systems-programming expertise in keeping native-code dependencies memory-safe?

**Thesis statement (12 Nov version).**
> Although high-level programming languages and AI-assisted development have made software creation increasingly accessible, their reliance on underlying native-code implementations introduces persistent memory-safety challenges. The long-term security and maintainability of these systems depend not only on improvements in automated tools but also on preserving the systems-programming expertise necessary to identify, understand, and remediate vulnerabilities within their underlying C and C++ components.

**The spine (13 Nov refinement).** Every chapter should advance this. If a paragraph doesn't, cut it or move it to the research agenda (ch. 8).
> Software built with high-level languages and AI tools still depends on C and C++. Not every developer needs to understand that layer, but the ecosystem needs enough specialists who do, because someone must be able to check and fix what the tools produce. Education and AI tool design should keep that specialist pipeline alive.

**The sharpest one-line version** (from `notes/the-ai-question.md`): as code generation moves to machines, the scarce human skill shifts from *writing* native code to *verifying* it.

**Stance.** Pro-AI. The claim is about how expertise is distributed across the ecosystem, not about individual programmers. AI can build understanding, not just replace it, depending on how it's used.

**Target length.** About 12,000–15,000 words of body text, roughly 40–50 pages double-spaced. *Confirm with the honors program and advisor.*

---

## Rules for the whole thesis

- **Organize by claim, not by source.** State the claim, bring in sources as evidence, say where they agree or conflict, and end each section with what it means for the spine. Avoid "Source A said X. Source B said Y."
- **End each chapter with a "so what"** paragraph that hands off to the next chapter.
- **Full credit first, then limits.** This applies to garbage collection, Rust, detection tools and AI security tools.
- **Lead with the data, not the AI.** AI-in-computing-education is crowded. Open with the dependency stack and memory-safety evidence, and bring AI in as the tension that makes those facts matter.
- **Name defeat conditions.** Don't claim the AI counterargument is defeated. It's an open empirical question, and saying what evidence would weaken the claim reads as confident, not weak.
- **NumPy native-code share:** Yang & Cai say 38%, our own count was 55.7%. State the counting rule wherever either number appears.
- **Novelty wording:** "We found no prior evaluation of the security of LLM-generated Python/C API code." Nothing stronger.
- Differentiate explicitly from Khalid et al. 2027, the closest prior art.
- Personal experience is motivation, never evidence. No chatbot citations. APA style. Don't single out Niagara University; present the scarcity of C/C++ expertise as a general trend backed by sources.
- Keep the normative claims in ch. 9 clearly separate from what the literature shows.

---

## Chapter plan at a glance

| # | Chapter | Words | Status |
|---|---|---|---|
| 1 | Introduction | 1,200 | **Scaffold done:** `draft/ch1-introduction.md` (write last) |
| 2 | The stack under the language | 1,500 | **Scaffold done:** `draft/ch2-stack-under-the-language.md` |
| 3 | Why memory safety keeps coming back | 1,800 | **Scaffold done:** `draft/ch3-memory-safety.md`; GC sources needed |
| 4 | The fixes and where each stops | 2,500 | **Scaffold done:** `draft/ch4-fixes-and-limits.md` |
| 5 | AI-assisted development and security | 1,800 | Material in notes |
| 6 | Expertise and how it forms (or erodes) | 2,000 | Material in notes; a few sources needed |
| 7 | Synthesis: memory-model literacy (L1/L2/L3) | 1,500 | Framework settled |
| 8 | Proposed research agenda | 1,200 | Designs settled |
| 9 | Closing: augmentation, not replacement | 1,200 | Not started |
| 10 | Limitations | 400 | Not started |

Chapters 4 and 6 carry the argument and get the most words. If you need to cut, trim chapters 2 and 3 first.

---

## Chapter 1. Introduction (≈1,200 words, write last)

**Paragraph scaffold: [`draft/ch1-introduction.md`](draft/ch1-introduction.md).**

**Claim:** AI and high-level languages have made software accessible. The stack underneath is still C/C++, and someone has to be able to check it.

- Open with the guiding question and the stakes: memory-safety policy (✅ cisa2023, ✅ oncd2024) and AI writing more code (✅ perry2023).
- State the stance (pro-AI) and the research question.
- Motivation, framed as why the question came up, not as evidence: classmates fluent in libraries but unable to picture what's underneath (told as a story about the system, not the people), and *"I use AI daily to deepen my understanding, which raised the question of when it builds understanding and when it replaces it."*
- State the thesis and give a roadmap of chapters 2–10.

**Draw from:** `paper/main.tex` §1; the introduction scaffold in `prior-art-review.md`.

---

## Chapter 2. The stack under the language (≈1,500 words)

**Paragraph scaffold: [`draft/ch2-stack-under-the-language.md`](draft/ch2-stack-under-the-language.md).**

**Claim:** "Memory-safe" software runs on a C/C++ core.

- The layers: CPython, the JavaScript engines in browsers and Node, NumPy and PyTorch native code, OpenSSL, libc.
- How much of the Python AI and scientific stack is native code. Our counts (Aug 2026, by file extension, vendored code excluded): NumPy 55.7%, CPython 47.4%, PyTorch 34.5%. Yang & Cai report NumPy at 38%; state both counting rules. ✅ yangcai2026
- The Python/C boundary is where things break: Yang & Cai's boundary bug taxonomy; Hu & Zhang's reference contract (new, borrowed and stolen references) and allocator families. ✅ yangcai2026, ✅ huzhang2023
- The interfacing mechanism itself drives vulnerability in multilingual code. ✅ lilicai2022
- Scripting-language native extensions carry real security risks. ✅ staicu2023
- Bindings for ML libraries are their own source of bugs. ✅ ompl2026; deep-learning framework bug studies in `notes/annotated-abstracts-v1.md` (A5–A9) ➕
- **So what:** the code most developers will never see is the code everything depends on.

**Draw from:** `notes/paper-concept-native-core.md`, `notes/hu-zhang-2020-digest.md`, `notes/annotated-abstracts-v1.md` Part A.

---

## Chapter 3. Why memory safety keeps coming back (≈1,800 words)

**Paragraph scaffold: [`draft/ch3-memory-safety.md`](draft/ch3-memory-safety.md).**

**Claim:** Memory-safety bugs remain the largest class of serious vulnerabilities; policy has noticed; garbage collection relocates the problem rather than eliminating it.

**3.1 The numbers.**
- About 70% of serious vulnerabilities at Microsoft and in Chromium are memory-safety bugs. ✅ miller2019 (confirm talk title), ✅ chromium2020. Microsoft counted patched CVEs and Chromium counted high-severity bugs, so they're similar findings, not the same measurement.
- CWE Top 25; Heartbleed as the canonical example. ➕ (one source each, or cut)

**3.2 Policy.**
- NSA 2022 memory-safety guidance ➕; CISA et al. 2023, *The Case for Memory Safe Roadmaps* ✅ cisa2023; ONCD 2024, *Back to the Building Blocks* ✅ oncd2024.

**3.3 What garbage collection solves and where it stops.**
- *Full credit first:* GC eliminates use-after-free and double-free in managed code, makes programming accessible, makes memory-safe languages practical, and modern collectors are fast. ➕ Jones, Hosking & Moss 2023, *The Garbage Collection Handbook* (2nd ed.); ➕ Hertz & Berger 2005 (GC performance)
- *Then where it stops.* Key line: **"Garbage collection does not eliminate memory-related vulnerabilities; it relocates them."**
  1. Native code sits outside it: C extensions, ctypes/cffi and the buffer protocol bypass the collector. ✅ staicu2023
  2. The runtime itself is C: CPython, including the collector, is written in an unsafe language. ➕ needs a source
  3. Leaks still happen in managed code: references kept alive by mistake (caches, globals, closures). ➕ needs a source
  4. Collector edge cases: reference cycles, finalizers (`__del__`) that resurrect objects, callbacks that run mid-operation. ➕ needs a source
  5. Concurrency: free-threaded CPython (PEP 703, 3.13+) changes how reference counting works under threads. ➕ PEP 703 itself is citable
- Framing: **reference counting *is* CPython's garbage collector.** At the boundary, the collector's bookkeeping becomes the programmer's job.
- **So what:** the memory problem doesn't disappear under a managed language; it moves to the boundary and the runtime.

**Draw from:** `thesis-plan.md` §1 (the GC list); this file.

---

## Chapter 4. The fixes and where each stops (≈2,500 words)

**Full paragraph scaffold: [`draft/ch4-fixes-and-limits.md`](draft/ch4-fixes-and-limits.md).** Work from that file; the summary below is only for orientation.

**Claim:** Memory-safe languages, detection tools and AI security systems each shrink the problem a great deal. None removes the need for people who can read and judge native code, and each moves the human role from *writing* code to *verifying* it.

- 4.1 The strongest objection, stated fairly
- 4.2 Memory-safe languages: Rust works (Android); limits: rewriting is slow, Rust still calls C, Rust's guarantee ends at `unsafe` (Astrauskas 2020, Xu 2021, Google 2025)
- 4.3 Detection tools: sanitizers, fuzzing, hardware, and their blind spots (MSET 2025, Firouzi & Ghafari 2026)
- 4.4 AI security tools: AIxCC credit and the concession that C memory bugs are among the most automatable; limits: much was plain fuzzing, and humans still review patches (DARPA 2025, CodeMender)
- 4.5 Synthesis: every fix moves the human from writer to verifier → hand-off to ch. 5

**Possible addition for ¶13 of the scaffold** (AI also writes native code): *LLM-CSEC* (arXiv 2511.18966, Nov 2025, preprint ⚠️), 10 models, CWE-classified weaknesses in AI-generated C. ➕

---

## Chapter 5. AI-assisted development and security (≈1,800 words)

**Claim:** AI-written code has security flaws at measurable rates, people trust it too much, and human review is the safeguard, but reviewing code you didn't write is hard.

- AI assistants produce insecure code. ✅ pearce2022 ("Asleep at the Keyboard"), ✅ sandoval2023
- People using AI assistants wrote less secure code but felt more confident. ✅ perry2023
- **Closest prior art:** 100 C-proficient developers reviewing real AI-generated C linked-list code couldn't reliably tell secure suggestions from insecure ones; only 22% of submissions were fully secure; participants who edited more produced fewer vulnerabilities. ✅ khalid2027. **Differentiate explicitly:** Khalid studies AI-generated pure C; this thesis is about the Python/C boundary and the L3 knowledge it requires.
- Complications to address head-on: in Khalid, developers with more than 3 years of experience submitted *more* vulnerabilities; Edmundson et al. found experience and education didn't predict security-review effectiveness. ✅ edmundson2013. Response: experience isn't the same as memory-model literacy, which is why ch. 7 proposes L1/L2/L3.
- Reviewers anchor on what an AI reviewer flags and search less elsewhere. Tufano et al. 2025 ➕
- Novices understand LLM-generated code poorly: 59.3% prompt comprehension vs. 32.5% code comprehension, with automation bias named as a barrier, in Python. *"I Would Have Written My Code Differently"* (FSE Companion 2025) ➕ (in `notes/literature-search-low-level-languages.md` #20)
- Less critical thinking with more trust in AI. ✅ lee2025
- Automation bias, briefly, as the general concept. ➕ one source, or use Bainbridge in ch. 6
- Static analyzers agree with ground truth only about 61–65% of the time on LLM-written code. ✅ firouzi2026 ⚠️
- **So what:** if the human role is verification, verification depends on understanding, which brings us to how that understanding forms.

**Draw from:** `prior-art-review.md` (Khalid, Edmundson, Tufano, Firouzi), `notes/the-ai-question.md`.

---

## Chapter 6. Expertise and how it forms (or erodes) (≈2,000 words)

**Claim:** Automation depends on rare human skill for the cases it misses; the routes into that skill are narrowing; AI can build or erode it depending on how it's used.

**6.1 The ironies of automation.** The more automated a system gets, the more it depends on rare human skill for the cases automation misses, and the less practice people get at that skill. ✅ bainbridge1983

**6.2 The pipeline is narrowing.**
- Junior roles are shrinking where AI adoption is high. ✅ brynjolfsson2025; Lichtinger & Hosseini Maasoum 2025 ➕ (both correlational; say so).
- What CS programs teach about memory now: CS2023 ➕ (check what it actually says about memory safety before citing); secure-programming knowledge gaps in students ✅ almansoori2023 (and Lam et al. 2022 ➕).
- Optional: maintainer burnout and xz-utils 2024, only if "maintainability" stays in the thesis statement.

**6.3 Mental models and notional machines.** Students can't review what they can't picture, and the abstraction hides the machine. Sorva 2013 ➕ (**missing from `refs.bib` and needed**). Main memory as a threshold concept (Kyriakou et al., `annotated-abstracts-v1.md` B5) ➕. Aliasing misconceptions ➕ (see `notes/theoretical-grounding-two-transfers.md`).

**6.4 AI can build understanding or replace it.**
- *Pro-AI evidence:* developers who asked the AI for explanations kept their understanding. ✅ shentamkin2026 (title still to confirm)
- *Skeptical evidence:* struggling students overestimated how well they understood their code ✅ prather2024; Becker et al. 2023 ✅ becker2023.
- **Strongest single finding for this chapter:** *Mitigating "Epistemic Debt"* (ACM L@S 2026, arXiv 2602.20206, preprint ⚠️) ➕. 78 novices, three conditions; in phase 2 the AI was removed and participants had to fix an injected race condition. Unrestricted AI produced the most working software (~90%) and the lowest repair success (23%); AI with an explanation gate reached 61%; manual control 69%. The authors define epistemic debt as software the user owns legally but not cognitively. This supports *both* sides: unrestricted AI erodes repair ability, while AI that requires explanation mostly preserves it.
- **So what:** the question isn't AI or no AI; it's which kind of AI use keeps the specialist pipeline alive.

**Draw from:** `notes/the-ai-question.md`, `notes/theoretical-grounding-two-transfers.md`, `notes/literature-search-low-level-languages.md`, `notes/annotated-abstracts-v1.md` Part B.

---

## Chapter 7. Synthesis: memory-model literacy, L1/L2/L3 (≈1,500 words)

**Claim:** Chapters 2–6 point to a specific gap in understanding, which this framework names. Most developers can work at L1 with AI help; the ecosystem needs a smaller group at L2/L3.

| Level | What the reader understands | Example question |
|---|---|---|
| **L1 — Managed model** | References, aliasing, mutation and object lifetime in a garbage-collected language | "After `b = a; b.append(1)`, what is `a`?" |
| **L2 — Manual model** | Allocation and release, ownership, dangling and null pointers, matching free to allocator | "Who frees this buffer, and with which function?" |
| **L3 — Boundary contract** | The collector's guarantees and the obligations C code takes on to keep them: new, borrowed and stolen references; exception state; allocator families | "This call returns a borrowed reference. What happens if a callback runs before it's used?" |

- Present it as a framework built from the literature, not a tested construct. Supporting claim: **L3 depends on L2 and can't be inferred from L1 alone.**
- Map the earlier chapters onto it: ch. 3's GC limits and ch. 4's `unsafe`/FFI limits are all L2/L3 problems; ch. 5's reviewers fail where L3 is required; ch. 6 asks where L2/L3 specialists come from.
- **Motivating example:** the tuple-packing refcount bug from `paper/main.tex` (`PyTuple_SET_ITEM` with a borrowed reference from `PyList_GET_ITEM`). Two standard static analyzers don't flag it and release CPython crashes silently. It's the clearest "you need to know what's underneath" moment in the thesis.
- **Counterargument:** "only a few specialists need L3, like mechanics vs. drivers." Agree, and say that's the point: the claim is about having *enough* specialists, and chapters 5–6 suggest the supply is at risk while AI increases the amount of code that needs checking.
- Informal support: Spolsky's "Law of Leaky Abstractions" ✅ spolsky2002 (cite as an essay, not research).
- **So what:** the framework makes the claim testable, which is what ch. 8 proposes.

**Draw from:** `thesis-plan.md` §1, `paper/main.tex` (motivating example).

---

## Chapter 8. Proposed research agenda (≈1,200 words)

**Claim:** The framework is testable, and here's how. These studies are proposed for future research, not run in the thesis. This chapter is also the pitch: "there is something worth researching here, and I'm the person to do it."

- **Study A (main): can AI tools build understanding instead of replacing it?** Compare an AI assistant that explains what's happening in memory (refcounts, ownership, which allocator owns what) with one that only writes the code. Measure L2/L3 understanding afterward and on a delayed test.
  - *Hypothesis (pro-AI):* AI designed to explain the memory model builds L2/L3 understanding. Support: Shen & Tamkin 2026; the epistemic-debt explanation-gate result.
  - *Skeptical view, built in:* AI help leads to dependence and overconfidence (Prather 2024, Lee 2025). If the explaining assistant doesn't beat the plain one, or both groups overestimate their understanding, the skeptics are right for this setting.
- **Study B: does understanding predict catching bugs?** Reviewers at different L1/L2/L3 levels review the same boundary code, with clean controls, all told to look for security problems, and no AI review shown (design choices from Braz 2022 ✅, Fulton 2024 ✅, Tufano 2025 ➕).
- **Study C: how do specialists form today?** Interviews with CPython, NumPy or similar maintainers about how they learned the C layer.
- **Study D (optional): what does AI leave behind at the boundary?** The original corpus study as a technical baseline: realistic prompts (the 10 pilot prompts in `prompts/pilot/` as an appendix example), sanitizers plus a debug CPython, static analyzers and an LLM reviewer; ground truth triangulated because tools disagree with labels (✅ firouzi2026).
- **Defeat conditions** (state them):
  - Automation catches almost everything at the boundary → the case for L2/L3 weakens.
  - L1 predicts bug-catching as well as L3 → GC-level understanding is enough.
  - An LLM reviewer alone matches the full tool set → the human role becomes "verifying the verifier."
  - Autonomous patching becomes reliable on real codebases without human verification → the case for broad L2/L3 literacy weakens considerably.
  - No predictor works → replicates Edmundson and Khalid at the boundary; still worth reporting.
- **Ethics** (if ever run): never recruit from classes Jessica teaches, TAs or grades; an advisor or another instructor announces the study; responses anonymous.

**Draw from:** `thesis-plan.md` §3 (designs and defeat conditions), `proposal.md`.

---

## Chapter 9. Closing: augmentation, not replacement (≈1,200 words)

**Claim (normative, labeled as such):** keeping this expertise is what lets people check AI's work, so AI augments human ability instead of replacing it.

- "You will need AI to compete" can slide into dependence or learned helplessness; the pro-AI answer is literacy that keeps humans able to verify.
- Transhumanism and posthumanism, drawing on Pope Leo XIV's encyclical *Magnifica Humanitas* (signed 15 May 2026, published 25 May 2026). Secondary sources point to ¶115, ¶118–130 and ¶172; **check paragraph numbers and quotes against your printed copy.** ➕ add to `refs.bib`
- Tie back to Bainbridge and the epistemic-debt finding: the risk is not AI itself but use that leaves people unable to step in.
- Keep the normative argument visibly separate from what chapters 2–7 showed.

---

## Chapter 10. Limitations (≈400 words)

- A literature review, not an empirical test; the framework is proposed, not validated.
- A fast-moving field: AI capability figures (AIxCC, Android) date quickly, and several key sources are preprints.
- Some sources were checked only at abstract level; flagged ⚠️ items should be verified before submission.
- Single author; Python/C focus (other boundaries such as JNI, cgo and Rust FFI are future work).

---

## Source gaps (targeted, not a sweep)

| Gap | Chapter |
|---|---|
| **Sorva 2013** (notional machines), missing from `refs.bib` | 6, 7 |
| NSA 2022 memory-safety guidance | 3 |
| Sources for GC limits 2–4 (runtime is C; managed leaks; finalizers/cycles); PEP 703 for limit 5 | 3 |
| Jones, Hosking & Moss 2023; Hertz & Berger 2005 (GC credit) | 3 |
| MSET 2025 authors; one AddressSanitizer/fuzzing source | 4 |
| Optional: CHERI/MTE source, Big Sleep post (or cut both) | 4 |
| *Epistemic Debt* (L@S 2026) and *"I Would Have Written My Code Differently"* (FSE 2025) | 6, 5 |
| Tufano et al. 2025; Lam et al. 2022; Lichtinger & Hosseini Maasoum 2025 (all in `prior-art-review.md`) | 5, 6, 8 |
| CS2023: check what it says about memory safety | 6 |
| *Magnifica Humanitas* entry | 9 |
| Already flagged: Shen & Tamkin title; "and others" author lists; Miller 2019 talk title; CodeMender post title; Android figures (only seen in secondary summaries); DARPA corrected figures | throughout |

---

## Writing schedule (17 Nov → mid-December)

| Week | Write | Also |
|---|---|---|
| **17–23 Nov** | Ch. 4 (from the scaffold), ch. 3 | Add Sorva and NSA to `refs.bib` |
| **24–30 Nov** *(Thanksgiving)* | Ch. 5, ch. 2 | Lighter week; ch. 2 is mostly mining notes |
| **1–7 Dec** | Ch. 6, ch. 7 | Close the CS2023 and epistemic-debt gaps |
| **8–14 Dec** | Ch. 8, 9, 10, **then ch. 1** | Full rough draft → advisor |
| **After** | Revise; verify every figure and citation | Venue: CHI 2027 SRC due 21 Jan. If HUGS (due 20 Nov) is pursued, see `notes/hugs-3page-outline-2026-11-12.md` |

---

## Open decisions

- Keep or drop "maintainability" in the thesis statement (if kept, add a maintainer-burnout source and xz-utils to ch. 6).
- Thesis format required by the honors program (Word or LaTeX). `paper/main.tex` is IEEE-format; its prose is reusable, its template probably not.
- Venue: HUGS (extended deadline 20 Nov; in-person attendance unclear) vs. CHI 2027 SRC (21 Jan). Check whether a HUGS publication would conflict with CHI SRC.

---

## What the other files are now

| File | Status |
|---|---|
| `draft/ch4-fixes-and-limits.md` | **Active.** Chapter 4 scaffold |
| `paper/refs.bib` | **Active.** All references |
| `notes/lit-review-outline-2026-11-12.md` | Superseded by this file; kept for history |
| `notes/hugs-3page-outline-2026-11-12.md` | Only for the short HUGS/CHI abstract, not the thesis |
| `thesis-plan.md`, `proposal.md` | Out of date (empirical design); mined for ch. 7–8 |
| `prior-art-review.md`, other `notes/` | Source material, drawn from per chapter above |
