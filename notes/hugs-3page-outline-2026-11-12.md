# HUGS 3-Page Abstract: Outline and Source List

*Drafted 12 Nov 2026 with Claude, based on the current HUGS draft in `paper/main.tex`. HUGS is due Fri 13 Nov 2026, 23:59 AoE (Sat 14 Nov, 6:59 AM ET).*

## Before submitting

- **`paper/main.tex` still describes studies you've decided not to run**, including the line "We have written ten pilot prompts." It needs updating to match this outline.
- **Check that the HUGS call for papers accepts a literature-review or position abstract.** Your notes say it expects a research plan, so a short "what a study would need" section (§7) helps it fit.

## Outline (IEEE two-column, references included)

Word counts are approximate. The total is about 1,600–1,700 words, close to the current draft.

**Title.** Keep it close to the current one, but match the new format. For example:
*"Reviewing What You Never Wrote: Memory-Model Literacy and the Limits of Abstraction at the Python/C Boundary."*

**Abstract (~120 words).** High-level languages, memory-safe languages and AI tools make software easier to write, but they still rest on C/C++. Argue from the literature that not every developer needs to understand that layer, but the ecosystem needs enough specialists who do, because someone must check and fix what the tools produce. Propose L1/L2/L3 as a way to describe the levels of understanding involved.

### 1. Problem (~400 words), mostly from the current draft
- *The abstraction runs on C:* the NumPy and CPython native-code share (state the counting rule), and the 70% memory-safety figure.
- *The boundary is where it breaks:* Yang & Cai's bug study, and Hu & Zhang's reference contract (new, borrowed and stolen references).
- *AI writes more of this code, and humans review it:* Pearce, Perry, Sandoval and Khalid, plus the shrinking junior-developer pipeline (Brynjolfsson).
- *Gap:* "We found no prior evaluation of the security of LLM-generated Python/C API code."

### 2. What garbage collection solves and where it stops (~200 words), new
- *Strengths first:* GC removes use-after-free and double-free in managed code, makes programming accessible, makes memory-safe languages practical, and modern collectors are fast.
- *Then weaknesses:* it only covers memory the runtime knows about, the C boundary is managed by hand (refcounting *is* CPython's GC), the collector is itself written in C, some leaks remain, and it hides the memory model.
- Existing line that fits here: *"Garbage collection does not eliminate memory-related vulnerabilities; it relocates them."*

### 3. Construct: three levels of memory-model literacy (~250 words plus table), kept from the draft
- The L1 (managed model), L2 (manual model) and L3 (boundary contract) table.
- Present it as a framework built from the literature. The old hypothesis becomes a supporting claim: L3 depends on L2 and can't be inferred from L1 alone.
- Central claim (refined 13 Nov): most developers can work at L1 with AI help, but the ecosystem needs a smaller group of specialists at L2/L3.

### 4. Motivating example (~150 words plus code), kept from the draft
The tuple-packing refcount bug. It's the clearest "you need to know what's underneath" moment in the paper.

### 5. Why better tools don't remove the need (~300 words), replaces "Research Plan"
- *Memory-safe languages:* give Android's Rust results full credit, then the limits: rewriting is slow, unsafe Rust still calls C, and Rust code can still have memory bugs.
- *AI security tools:* give AIxCC and Big Sleep full credit, then note that CodeMender's patches are all reviewed by a human.
- *The ironies of automation:* the more automated a system gets, the more it depends on rare human skill (Bainbridge).

### 6. Implications for education and tool design (~150 words)
- How AI is used matters: in Shen & Tamkin, developers who asked for explanations kept their understanding.
- The risks: struggling students overestimate their understanding (Prather), people do less critical thinking when they trust the AI more (Lee), and secure-programming teaching has gaps (Almansoori).
- *The pipeline question:* if junior roles shrink (Brynjolfsson) and rarely used skills erode (Bainbridge), where do the next L2/L3 specialists come from?
- *Design question:* how can AI tools and courses keep that specialist pipeline alive instead of replacing it?

### 7. Proposed research agenda (~150 words), updated 13 Nov
The pitch: problem → framework → studies. Proposed, not run.
- **Main study: can AI tools build understanding?** Compare an AI assistant that explains the memory model with one that only writes code, then measure L2/L3 understanding.
  - *Hypothesis (pro-AI):* explaining assistants build understanding (supported by Shen & Tamkin).
  - *Skeptical view, built in:* AI help causes dependence and overconfidence (Prather, Lee). If the explaining assistant doesn't do better, the skeptics are right for this setting.
- **Supporting study: does understanding predict catching bugs?** Compare reviewers at different L1/L2/L3 levels on the same boundary code. This answers what happens when someone doesn't understand the code.
- **Supporting study: how do specialists form?** Interviews with CPython/NumPy maintainers.
- Keep a shortened version of the defeat conditions. They show the claim could be proven wrong.

### 8. Questions for the workshop (~60 words), kept from the draft

*The transhumanism and* Magnifica Humanitas *section stays in the thesis, not this abstract.*

## Source list (about 21; references count toward the 3 pages)

| § | Source | Status |
|---|---|---|
| 1 | Yang & Cai 2026 | in refs.bib |
| 1 | Hu & Zhang 2023 | in refs.bib |
| 1 | Li, Li & Cai 2022 | in refs.bib |
| 1 | Miller 2019 (Microsoft, 70%) | in refs.bib, confirm title |
| 1 | CISA et al. 2023 | in refs.bib |
| 1 | Pearce et al. 2022 | in refs.bib |
| 1 | Perry et al. 2023 | in refs.bib |
| 1 | Sandoval et al. 2023 | in refs.bib |
| 1 | Khalid et al. 2027 | in refs.bib |
| 1 | Brynjolfsson et al. 2025 | in refs.bib |
| 1 | OMPL 2026 (no binding benchmark) | in refs.bib |
| 2 | Staicu et al. 2023 | in refs.bib |
| 2 | Jones, Hosking & Moss 2023, *The Garbage Collection Handbook* (2nd ed.) | **not yet in refs.bib** |
| 5 | Google 2025, Rust in Android | in refs.bib, check figures |
| 5 | Astrauskas et al. 2020 | in refs.bib |
| 5 | DARPA 2025, AIxCC | in refs.bib |
| 5 | DeepMind 2025, CodeMender | in refs.bib, confirm title |
| 5 | Bainbridge 1983 | in refs.bib |
| 6 | Shen & Tamkin 2026 | in refs.bib, **title still TODO** |
| 6 | Prather et al. 2024 | in refs.bib, complete authors |
| 6 | Lee et al. 2025 | in refs.bib |
| 6 | Almansoori et al. 2023 | in refs.bib |

**Cut for space:** Fulton 2024, Braz 2022 and Firouzi 2026 were study-design citations and are no longer needed. Edmundson 2013, the Chromium 70% figure, ONCD 2024, Becker 2023, Hertz & Berger 2005 and Spolsky 2002 stay in the thesis. If still over 3 pages, the first cuts are Li, Li & Cai and OMPL.
