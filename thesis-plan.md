# Thesis Plan — Reviewing What You Never Wrote

**Memory-Model Literacy and the Human Review of AI-Generated Code at the Python/C Boundary**

Jessica Dye · Niagara University · Honors thesis, defense Spring 2027
Last updated: 29 October 2026

Related files: `proposal.md` (full proposal), `prior-art-review.md` (literature and introduction scaffold)

---

## 1. Research question

**Main RQ.** When AI generates code that crosses the Python/C memory-management boundary, which defects survive automated review? What kind of memory-model literacy does a human reviewer need to catch them?

| | Sub-question | Part |
|---|---|---|
| **RQ1** | Which defects in LLM-generated Python/C boundary code survive the combined automated tier (sanitizers, static analysis, LLM review)? | 1 |
| **RQ2** | For each surviving defect, which literacy level is required to recognize it? | 1 |
| **RQ3** | Among undergraduates, does performance on a three-level literacy test predict detection of those defects better than years of experience does? How well calibrated is their confidence? | 2 (pilot) |

### Core construct: three levels of memory-model literacy

| Level | What the reader understands | Example question |
|---|---|---|
| **L1 — Managed model** | References, aliasing, mutation, and object lifetime in a garbage-collected language | "After `b = a; b.append(1)`, what is `a`?" |
| **L2 — Manual model** | Allocation and release, ownership, dangling and null pointers, matching free to allocator | "Who frees this buffer, and with which function?" |
| **L3 — Boundary contract** | The collector's guarantees and the obligations C code takes on to keep them: new, borrowed, and stolen references; exception state; allocator families | "This call returns a borrowed reference. What happens if a callback runs before it's used?" |

**Key framing:** reference counting *is* CPython's garbage collector. At the boundary, the GC's bookkeeping becomes the programmer's job.

**Hypothesis.** The residue that survives automated review is dominated by L3 defects. L3 depends on L2 and can't be inferred from L1 alone.

**Positioning.** Khalid et al. [S&P 2027] and Edmundson et al. [ESSoS 2013] found that years of experience don't predict detection. RQ3 tests whether a specific, teachable literacy does.

---

## 2. Targets and deadlines

| Venue | What | Deadline | Notes |
|---|---|---|---|
| **HUGS 2027** @ ICSE, Dublin | 3-page extended abstract, IEEE template, includes refs | **Fri 13 Nov 2026, 23:59 AoE** (= Sat 14 Nov, 6:59 AM ET) | Notification 11 Dec. Camera-ready 29 Jan 2027. Workshop 27 Apr 2027. Submit at icse2027-hugs.hotcrp.com |
| ICSE 2027 SRC *(optional)* | 800 words, 2 pp + 1 p refs, single-authored | Fri 13 Nov 2026 | Needs ACM student membership. Must differ from HUGS by ≥30%. One SRC per program year |
| CHI 2027 workshops, Pittsburgh *(fallback / follow-on)* | Varies by workshop | ~11 Feb 2027 | Calls posted 17 Dec 2026. Drivable |
| Thesis defense | Full thesis | Spring 2027 | |

---

## 3. Schedule

### Phase 1 — HUGS submission (now → 13 Nov)

**Week of 29 Oct – 4 Nov: set up and generate**
- [ ] Advisor sign-off on scope; settle co-authorship
- [ ] Create HotCRP account; download IEEE conference template
- [x] Write 10 pilot prompts (C-API extensions, ctypes wrappers, exception propagation) — `prompts/pilot/`
- [ ] Build the pipeline: generate → compile → ASan/UBSan/Valgrind → cppcheck/clang-tidy/CodeQL → LLM review; pin tool versions in the script
- [ ] Generate ~60 samples (10 prompts × 2 models × 3); log model, version, date, temperature
- [ ] Draft codebook from Yang & Cai [2026] taxonomy + Hu & Zhang [2020] 10 bug patterns

**Week of 5 – 10 Nov: audit and draft**
- [ ] Run the automated tier on every sample; record which tool caught what
- [ ] Manual audit of all samples; second coder on ~20%; compute Cohen's κ
- [ ] Identify the residue (missed by every tool); code each defect L1 / L2 / L3
- [ ] Draft the abstract (see §6 for page budget)
- [ ] Verify preprint status of cited papers (Khalid et al., Yang & Cai, OMPL)

**11 – 13 Nov: review and submit**
- [ ] Advisor read; revise
- [ ] Check format: 3 pages incl. refs, IEEE template, anonymity rules per CFP
- [ ] Submit (aim for 12 Nov)

*If doing the SRC:* ACM student membership, eligibility check, 800-word single-authored version.

**Bottleneck:** the manual audit and second coder. Pipeline must be producing samples by the weekend of 31 Oct.

### Phase 2 — Thesis (after submission)

| When | Work |
|---|---|
| Mid–late Nov | Submit IRB protocol for Part 2 |
| Nov – Jan | Scale Part 1 to 30–40 prompts × 3–4 models; complete audit and κ |
| 11 Dec | HUGS notification. If accepted: SIGSOFT CAPS, ICSE student volunteering, Niagara travel funds |
| Late Jan | HUGS camera-ready (29 Jan) |
| Feb | CHI 2027 workshop submission with full Part 1 results |
| Feb – Mar | Run Part 2 after IRB approval |
| Mar – Apr | Write and defend thesis |
| Late Apr | Present at HUGS, Dublin (if accepted) |

---

## 4. Study design

### Part 1 — Corpus study (no IRB; core of thesis and HUGS paper)

1. **Prompts.** 30–40 realistic developer requests that force boundary code, phrased without hinting at security. Strata: C-API extension functions (argument parsing, building containers, calling back into Python); ctypes/cffi wrappers passing buffers, strings, arrays; code that raises or propagates Python exceptions from C. Pilot uses 10.
2. **Generation.** 3–4 current models, *n* samples per prompt. Log everything. The frozen corpus is a released artifact.
3. **Automated tier.**
   - ASan/UBSan and Valgrind with fuzzed and edge-case inputs (`None`, empty, huge, wrong type, exception-raising callbacks)
   - Static analysis: cppcheck, clang-tidy, CodeQL
   - LLM review: a general LLM, plus `cext-review-toolkit` if usable
   - Everything scripted and runnable from the command line
4. **Ground truth.** Manual audit with the codebook. Second coder on ~20%, report κ. A defect counts only if reproduced or both coders agree.
5. **Residue (RQ1).** Defects missed by every automated tier.
6. **Literacy coding (RQ2).** Lowest level (L1/L2/L3) at which each residue defect is recognizable. Double-coded, κ reported.

### Part 2 — Review pilot (IRB required; thesis only)

- **Participants:** 30–60 undergraduates, CS1 through seniors. Not recruited from any class the author teaches or grades; advisor or another instructor announces it; anonymous.
- **Screening:** Danilova et al. C-proficiency questions (as in Khalid et al.); recorded as a covariate.
- **Instrument:** L1/L2/L3 subscales built from existing work — L1 from SPLASH-E 2017 aliasing quizzes and Kaczmarczyk et al. [SIGCSE 2010]; L2 from Almansoori et al. [SIGCSE 2023] / Lam et al. [SIGCSE 2022] "knowledge of memory" SOLO rubric; L3 new (from Hu & Zhang and Yang & Cai patterns).
- **Task:** Read-and-review, not write [Fulton et al., SOUPS 2024]. ~12 real defective snippets from Part 1 plus clean controls.
- **Instructions:** every participant told to review for security [Braz et al., ICSE 2022: ~8× detection effect].
- **No AI review shown** [Tufano et al., ICSE 2025: anchoring]. Possible future arm.
- **Confidence** rating per verdict (calibration vs. Perry et al. and Khalid et al.).
- **Background items:** courses taken; community-college/transfer pathway; where memory management was learned (coursework, job/internship, self-taught).
- **Analysis:** Poisson regression on defects missed (L1/L2/L3 scores + years of experience, participant random effect); per-defect logistic regression by literacy level; calibration. Reported as a pilot with effect sizes and CIs.

### Defeat conditions (stated in the paper)

- Automation catches almost everything → little residue; case for L2/L3 literacy weakens.
- L1 predicts detection as well as L3 → GC-level literacy suffices.
- LLM reviewer alone matches the full tier → human role becomes verifying the verifier.
- No predictor works → replicates Edmundson et al. and Khalid et al. at the boundary; still reportable.

---

## 5. Novelty claim (worded precisely)

The methods are standard. The contribution is the question: connecting what survives automated review to a specific, teachable level of memory-model literacy, at the boundary where most of the scientific and ML Python stack runs.

Say: *"We found no prior evaluation of the security of LLM-generated Python/C API code."* Cite the OMPL bindings study (no benchmark exists for binding generation). Run an ACM DL / IEEE Xplore check before submission.

---

## 6. HUGS abstract outline (3 pages incl. refs)

| Section | Budget | Content |
|---|---|---|
| Problem | ~0.4 p | AI writes boundary code; review is the human's job; experience doesn't predict detection; the junior apprenticeship is shrinking |
| Construct | ~0.4 p | L1/L2/L3 table; refcounting is the GC's contract |
| Pilot | ~0.9 p | ~10 prompts × 2 models; residue after the automated tier; literacy profile; one table |
| Agenda | ~0.5 p | Full corpus; student review study; defeat conditions; breakout questions |
| References | ~0.8 p | 12–15 entries |

---

## 7. Threats to validity

- **Prompt realism** — phrase prompts from real Stack Overflow / GitHub-issue requests; release them.
- **Model drift** — freeze and release the corpus; report versions and dates.
- **Ground truth** — triangulated labels can still miss defects; report κ; treat the residue as a lower bound.
- **Literacy coding is a judgment** — double-code; publish the codebook with examples.
- **Pilot generalization** — single institution, small n; reported as a pilot.
- **Measurement differences** — Yang & Cai report NumPy as 38% native; own measurement found 55.7%. State the counting rule wherever cited.

---

## 8. Admin and open items

- [ ] Advisor: scope, co-authorship, IRB path, Part 2 recruiter, travel funding
- [ ] Decide on ICSE SRC (check one-SRC-per-year rule)
- [ ] ACM student membership (if SRC)
- [ ] IRB protocol (after HUGS submission)
- [ ] Travel funding plan if accepted: SIGSOFT CAPS (partial; excludes registration), student volunteering, Niagara funds; passport for Dublin
- [ ] Library check for prior work before claiming novelty

---

## 9. Must-cite core

1. Khalid et al., S&P 2027 — closest prior art; differentiate explicitly
2. Yang & Cai, arXiv 2026 — boundary bug taxonomy; codebook
3. Almansoori et al., SIGCSE 2023 (+ Lam et al. 2022) — closest education work; L2 rubric
4. Hu & Zhang, SANER 2020 / JSEP 2023 — bug patterns
5. Sandoval et al., USENIX Security 2023 — counter-finding; reusable C corpus
6. Perry et al., CCS 2023 — overconfidence baseline
7. Edmundson et al., ESSoS 2013 — experience doesn't predict review effectiveness
8. Li, Li & Cai, FSE 2022 — interfacing mechanism drives vulnerability
9. Braz et al., ICSE 2022; Fulton et al., SOUPS 2024; Tufano et al., ICSE 2025 — Part 2 design choices
10. CISA 2023 / ONCD 2024 — policy framing
11. Lichtinger & Hosseini Maasoum 2025; Brynjolfsson et al. 2025 — junior pipeline

Full references: see `proposal.md` and `prior-art-review.md`.
