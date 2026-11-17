# Thesis Assembly Plan: From Outline to Full Draft

*Drafted 17 Nov 2026. Builds on `notes/lit-review-outline-2026-11-12.md` (the argument). This file covers how to assemble it: chapter by chapter, what each one claims, what feeds it, and when to write it.*

**Goal:** a complete, rough full draft by **mid-December 2026**. Rough is fine. A finished draft you can revise beats three polished chapters.

**Target length:** roughly **12,000–15,000 words** of body text (about 40–50 pages double-spaced). *Confirm the expected length with the honors program and advisor;* the budgets below scale proportionally.

---

## The one-sentence spine

Every chapter should advance this claim (from the 13 Nov refinement):

> Software built with high-level languages and AI tools still depends on C and C++. Not every developer needs to understand that layer, but the ecosystem needs enough specialists who do, because someone must be able to check and fix what the tools produce. Education and AI tool design should keep that specialist pipeline alive.

When a paragraph doesn't serve the spine, cut it or move it to the research agenda.

---

## How a literature review differs from a summary

The common failure is "Source A said X. Source B said Y." Organize each section **by claim, not by source**: state the claim, bring in sources as evidence, say where they agree or conflict, and end with what it means for the spine. Each chapter should end with a short **"so what"** paragraph that hands off to the next one.

---

## Chapter map

| # | Chapter | What it claims | Words | Main sources (`refs.bib` keys) | Mine from |
|---|---|---|---|---|---|
| 1 | **Introduction** | Guiding question; the stakes; pro-AI stance; roadmap | 1,200 | cisa2023, oncd2024, perry2023 | `paper/main.tex` §1, `prior-art-review.md` intro scaffold |
| 2 | **The stack under the language** | "Memory-safe" software runs on a C/C++ core | 1,500 | staicu2023, lilicai2022, huzhang2023, yangcai2026, astrauskas2020 | `notes/paper-concept-native-core.md`, `notes/hu-zhang-2020-digest.md`, SQ1 counts in `thesis-plan.md` |
| 3 | **Why memory safety keeps coming back** | ~70% of serious vulnerabilities are memory-safety bugs; policy has noticed; GC relocates the problem rather than eliminating it | 1,800 | miller2019, chromium2020, cisa2023, oncd2024, staicu2023 | `thesis-plan.md` §1 (GC list), HUGS outline §2 |
| 4 | **The fixes and where each stops** | Rust, hardware, sanitizers/fuzzing and AI tools each shrink the problem; none removes the need for a human who can read C | 2,500 | google2025rust, astrauskas2020, darpa2025aixcc, deepmind2025codemender | lit-review outline §3 ("just use Rust") |
| 5 | **AI-assisted development and security** | AI-written code has security flaws and users trust it too much; review is the safeguard | 1,800 | pearce2022, perry2023, sandoval2023, khalid2027, lee2025, braz2022, fulton2024, edmundson2013 | `notes/the-ai-question.md`, `prior-art-review.md` |
| 6 | **Expertise and how it forms (or erodes)** | Automation depends on rare human skill; the routes into that skill are narrowing; AI can help or hurt depending on use | 2,000 | bainbridge1983, brynjolfsson2025, prather2024, becker2023, shentamkin2026, almansoori2023, *Sorva 2013 (add)* | `notes/theoretical-grounding-two-transfers.md`, `notes/literature-search-low-level-languages.md`, `notes/annotated-abstracts-v1.md` Part B |
| 7 | **Synthesis: memory-model literacy (L1/L2/L3)** | The framework that ties chapters 2–6 together: most developers at L1, the ecosystem needs specialists at L2/L3 | 1,500 | spolsky2002 (essay), Sorva, plus the ch. 6 sources | `thesis-plan.md` §1 table, motivating example in `paper/main.tex` |
| 8 | **Proposed research agenda** | Four studies that would test the framework, with defeat conditions | 1,200 | firouzi2026, ompl2026 + the design sources | lit-review outline §7, `thesis-plan.md` §3 defeat conditions, `prompts/pilot/` (as an appendix example only) |
| 9 | **Closing: augmentation, not replacement** | Normative: keeping this expertise lets people verify AI, so AI augments rather than replaces | 1,200 | *Magnifica Humanitas* (paragraph numbers from your printed copy), bainbridge1983 | memory notes; new writing |
| 10 | **Limitations** | Lit-review scope, fast-moving field, sources checked only at abstract level, single author | 400 | n/a | `thesis-plan.md` §7 (adapted) |

**Total ≈ 15,100.** Chapters 4 and 6 carry the argument, so they get the most words. If you need to cut, trim chapters 2 and 3 first.

**Cross-cutting rules** (from `CLAUDE.md`): give each abstraction full credit before its limits; state the NumPy counting rule wherever 38% or 55.7% appears; keep chapter 9's normative claims clearly separate from what the literature shows; personal experience is motivation only; no chatbot citations; APA style.

---

## Source gaps to close (small, targeted, not a sweep)

| Gap | Where it's needed | Notes |
|---|---|---|
| **Sorva 2013** (notional machines) is cited everywhere but **missing from `refs.bib`** | ch. 6, 7 | Add the entry |
| NSA 2022 memory-safety guidance | ch. 3 | Named in the outline, not in the bib |
| Citable sources for GC limits 2–5 (runtime is C; managed leaks; finalizers/cycles; PEP 703 free-threading) | ch. 3 | `thesis-plan.md` §1 TODO. PEP 703 itself is citable for item 5 |
| CS2023: what it actually says about memory safety | ch. 6 | Entry 7 in `literature-search-low-level-languages.md`; check before citing |
| Deskilling / automation-bias source beyond Bainbridge | ch. 5 or 6 | One solid source is enough |
| Flagged entries from 12 Nov (Shen & Tamkin title, "and others" author lists, Android figures) | throughout | Verify against originals |
| Optional: xz-utils 2024 | ch. 6 | Only if "maintainability" stays in the thesis statement |

About 5–7 additions, not 30. Folding the strongest entries from `annotated-abstracts-v1.md` and `literature-search-low-level-languages.md` into `refs.bib` covers most of the education side.

---

## Writing schedule (17 Nov → mid-Dec)

Write the chapters that have the most material first. Write the introduction **last**, once you know what the thesis actually says.

| Week | Write | Also |
|---|---|---|
| **17–23 Nov** | Ch. 4 (fixes and limits) and ch. 3 (memory safety) | Add Sorva + NSA to `refs.bib` |
| **24–30 Nov** *(Thanksgiving)* | Ch. 5 (AI and security), ch. 2 (stack) | Lighter week; ch. 2 is mostly mining existing notes |
| **1–7 Dec** | Ch. 6 (expertise), ch. 7 (L1/L2/L3 synthesis) | Close the CS2023 / deskilling gaps |
| **8–14 Dec** | Ch. 8 (agenda), ch. 9 (closing), ch. 10, **then ch. 1** | Full rough draft exists → send to advisor |
| **After** | Revise; verify every figure and citation | Decide on CHI 2027 SRC (due 21 Jan): the 5-page abstract is a compression of chs. 2, 4, 7, 8 |

---

## Housekeeping (decide, don't do yet)

- **Format.** Write the thesis in the honors program's required format, which may be Word or LaTeX. `paper/main.tex` is IEEE-format HUGS text; its prose can be reused, but probably not its template.
- **Stale files.** `thesis-plan.md` and `proposal.md` still describe the empirical design. Leave them as an archive, or add a one-line "superseded by the lit-review format" banner at the top of each.
- **Thesis statement.** Still open from 12 Nov: keep or drop "maintainability."

## Suggested first writing session

Start with **chapter 4, section "Answering 'just use Rust'."** The argument is already outlined (rewriting is slow → Rust still calls C → Rust can still have memory bugs → AI tools still need human review), the sources are already in `refs.bib`, and it's the chapter that most directly defends the thesis against its strongest objection.
