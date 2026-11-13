# Thesis Plan — Reviewing What You Never Wrote

**Memory-Model Literacy and the Human Review of AI-Generated Code at the Python/C Boundary**

Jessica Dye · Niagara University · Honors thesis, defense Spring 2027
Last updated: 5 November 2026 (scope trimmed to undergraduate-honors scale; the earlier version is in git history)

Related files: `proposal.md` (full proposal, written for the earlier, larger design), `prior-art-review.md` (literature and introduction scaffold), `paper/main.tex` (HUGS draft)

---

## 1. Research question

### Guiding question

> **As AI becomes increasingly capable of writing and debugging software, what happens when both the developer and the AI are working with abstractions built on lower-level systems that the developer doesn't understand?**

**Stance.** The thesis takes a pro-AI position. The question isn't whether to use AI tools or Python. It's what human understanding is needed to oversee them when something goes wrong beneath the abstraction. The risk is a hypothesis to test, not a conclusion.

### Sub-questions (how the thesis answers it)

| | Sub-question | Method | Status |
|---|---|---|---|
| **SQ1** | How much of the Python AI and scientific stack is built on native code? | Repository line counts by file extension, vendored code excluded | **Done** (Aug 2026): NumPy 55.7%, CPython 47.4%, PyTorch 34.5% |
| **SQ2** | Which defects in AI-generated Python/C code do automated tools, AI reviewers included, miss? What level of literacy does each missed defect need? | Study 1: small corpus | Prompts written; tools installed |
| **SQ3** | Does a developer's understanding of the memory model predict whether they catch what the tools miss? Does their confidence match their accuracy? | Study 2: small student pilot | After IRB |

### Core construct: three levels of memory-model literacy

| Level | What the reader understands | Example question |
|---|---|---|
| **L1 — Managed model** | References, aliasing, mutation, and object lifetime in a garbage-collected language | "After `b = a; b.append(1)`, what is `a`?" |
| **L2 — Manual model** | Allocation and release, ownership, dangling and null pointers, matching free to allocator | "Who frees this buffer, and with which function?" |
| **L3 — Boundary contract** | The collector's guarantees and the obligations C code takes on to keep them: new, borrowed, and stolen references; exception state; allocator families | "This call returns a borrowed reference. What happens if a callback runs before it's used?" |

**Key framing:** reference counting *is* CPython's garbage collector. At the boundary, the GC's bookkeeping becomes the programmer's job.

**Garbage collection doesn't eliminate memory-related vulnerabilities; it relocates them.** This is the misconception the L1 → L3 gap captures: "Python has a GC, so memory isn't my problem." Ways the guarantee runs out:
1. **Native code sits outside it.** C extensions, ctypes/cffi, and the buffer protocol all bypass the collector. This is the core of the thesis [Staicu et al., USENIX Security 2023, "Bilingual Problems"].
2. **The runtime itself is C.** CPython, and the collector itself, are written in an unsafe language, so a bug there is a memory bug.
3. **Leaks still happen in managed code.** References kept alive by mistake (caches, globals, closures) cause unbounded memory growth, which is a reliability and denial-of-service risk.
4. **Collector edge cases.** Reference cycles, finalizers (`__del__`) that resurrect objects, and callbacks that run mid-operation (the P03/P07 hazards).
5. **Concurrency.** Free-threaded CPython (PEP 703, 3.13+) changes how reference counting works under threads. Extensions written for the GIL era can break there.

*TODO: find a citable source for each of 2–5 before using them in the thesis. Only Staicu et al. is verified in our files.*

**Theory link:** *notional machines* [Sorva 2013]. Students can't review what they can't picture, and the abstraction hides the machine. The thesis asks which parts of the hidden machine (L1, L2, L3) a reviewer actually needs.

**Hypothesis.** The defects that survive automated review are mostly L3. L3 depends on L2 and can't be inferred from L1 alone.

**The real question underneath:** if an agent makes a mistake, who catches it? There are three candidate catchers: tests and sanitizers, another AI, or a human who understands the machine. Fixing a bug is often easy once it's found. The hard parts are *noticing* it and *judging* whether a proposed fix is right.

---

## 2. Scope: what "exceptionally good undergraduate" means here

The depth comes from the idea, not the volume. That means one sharp question, two small, well-run studies, clear writing, and honest limits. Everything else becomes future work.

| Keep (the depth) | Kept small | Future work (grad school) |
|---|---|---|
| L1/L2/L3 construct | Corpus: 10–15 prompts × 2 models × 3 samples | 30–40 prompts × 3–4 models |
| Dependency-stack argument (SQ1) | Tools: sanitizers + debug CPython + 2 static analyzers + 1 LLM reviewer | CodeQL, Valgrind (Linux), more LLM reviewers |
| Motivating example (the hand-written stolen-reference bug) | Student pilot: ~15–30 participants, simple statistics | Regression models with random effects; larger samples |
| One careful audit with a codebook | Second coder on ~20% if available | Full double-coding of every sample |
| | | Write/optimize-task arm (participants use AI to speed up Python in C), unless the advisor prefers it *instead of* the read task |
| | | Other boundaries: JNI, cgo, Rust FFI |

Not in scope: building a new library, extension, or security-testing framework. The study uses existing tools on existing AI output. Code examples only illustrate.

---

## 3. Study design

### Study 1 — Corpus (SQ2; no IRB)

1. **Prompts.** 10 pilot prompts exist (`prompts/pilot/`). They're realistic developer requests in Stack Overflow style, with no security hints, across three strata: C-API extensions, ctypes/cffi wrappers, and exception propagation. Add up to 5 more for the thesis.
2. **Generation.** Two models, Claude and GPT, with 3 samples per prompt (≈60 for 10 prompts). Log the model, version, date and settings. The corpus is frozen and released.
   - *Collection route, still open:* the API (`pipeline/generate.py`, needs keys) or by hand in the chat apps (Temporary Chat, recording the model name and date). By hand is free but less reproducible; say so in the methods.
3. **Automated tier**, with versions pinned in `pipeline/requirements.lock`:
   - AddressSanitizer + UBSan (Apple clang 17) and a **debug CPython 3.12.16** (refcount assertions), run on edge-case inputs from `manifest.json`.
   - Static analysis: cppcheck 2.22.0, clang-tidy 23.1.4.
   - LLM review: **Gemini**, from a vendor that didn't generate the code, so no model reviews its own output.
   - Valgrind is dropped because it doesn't run on Apple Silicon; ASan covers the same classes. Leaks are checked with refcount deltas and macOS `leaks`. CodeQL is future work.
4. **Ground truth.** Jessica audits every sample with a codebook (Yang & Cai 2026 taxonomy + Hu & Zhang 2020 patterns). A defect counts if it's **reproduced** (a sanitizer or assertion fires) or if two coders agree.
   - *Second coder:* ask the advisor to code ~12 samples. If no one is available, report single-coder labels backed by reproduction, and defer κ to future work. Do **not** use an LLM as the second coder, since it's part of the tool tier.
5. **Residue.** Defects that every tool missed. Code each one L1/L2/L3.

### Study 2 — Student pilot (SQ3; IRB required)

- **Participants:** ~15–30 undergraduates, CS1 through seniors. Never recruited from a class Jessica teaches, TAs or grades. The advisor or another instructor announces the study, and responses are anonymous.
- **Literacy test:** a short L1/L2/L3 test built from existing items. L1 comes from aliasing quizzes and Kaczmarczyk et al. 2010; L2 from Almansoori et al. 2023 / Lam et al. 2022; L3 is new, drawn from the Study 1 defects.
- **Task:** read and review about 8–12 real defective snippets from the Study 1 residue, plus clean controls [Fulton et al. 2024]. Everyone is told to look for security problems [Braz et al. 2022]. No AI review is shown [Tufano et al. 2025].
- **Confidence:** one rating per verdict.
- **Background:** courses taken, years of programming, and where memory management was learned.
- **Analysis (kept simple):** detection rate by literacy level; correlation of L1/L2/L3 scores and of years of experience with detection; a confidence-vs-accuracy (calibration) plot. Report it as a pilot with effect sizes and confidence intervals.

### Context, not a study: curriculum snapshot

Briefly describe where Niagara and 3–5 peer programs teach memory management (which courses, which language). This takes one or two pages and needs no new data collection. It supports the education argument without becoming a curriculum study.

### Defeat conditions (stated in the paper)

- Automation catches almost everything → little residue; the case for L2/L3 weakens.
- L1 predicts detection as well as L3 → GC-level literacy is enough.
- The LLM reviewer alone matches the full tier → the human role becomes "verifying the verifier."
- No predictor works → replicates Edmundson et al. and Khalid et al. at the boundary; still reportable.

**Counterargument to address:** "Only a few specialists need L3, like mechanics vs. drivers." The answer comes from the data: if AI writes boundary bugs often and tools miss them, a few specialists won't scale.

---

## 4. Targets and deadlines

| Venue | What | Deadline | Notes |
|---|---|---|---|
| **HUGS 2027** @ ICSE, Dublin | 3-page extended abstract, IEEE, refs included | **Fri 13 Nov 2026, 23:59 AoE** (= Sat 14 Nov, 6:59 AM ET) | Draft in `paper/`. Notification 11 Dec; camera-ready 29 Jan; workshop 27 Apr. icse2027-hugs.hotcrp.com |
| ICSE 2027 SRC *(optional)* | 800 words, single-authored | Fri 13 Nov 2026 | Probably skip this year; scope is already full |
| CHI 2027 workshops, Pittsburgh | Varies | ~11 Feb 2027 | Good fit for the human-oversight (HCI) side. Calls posted 17 Dec |
| Thesis defense | Full thesis | Spring 2027 | |

---

## 5. Schedule

### Now → HUGS (13 Nov)

The HUGS abstract is a **research plan plus the motivating example**. It doesn't need pilot data. If time allows, a mini-pilot (10 samples, one per prompt) adds a small preliminary table.

- [x] 10 pilot prompts — `prompts/pilot/`
- [x] Toolchain installed and pinned; ASan and the debug CPython tested on a known bug
- [x] Motivating example run (cppcheck and clang-tidy miss it; release CPython crashes silently)
- [x] First full HUGS draft — `paper/main.tex` (3 pages)
- [ ] **Fri 6 Nov — advisor:** co-authorship; draft read on 11 Nov; second coder; trimmed scope; read task vs. write task; whether plan-only is right for HUGS
- [ ] Check the HUGS CFP: anonymity rules, AI-disclosure policy
- [ ] Verify preprint status: Khalid et al., Yang & Cai, OMPL, Firouzi & Ghafari
- [ ] Novelty check: ACM DL / IEEE Xplore / Google Scholar, logging the queries
- [ ] *(Optional)* mini-pilot: 10 samples
- [ ] Wed 11 Nov — advisor read; revise
- [ ] Thu 12 Nov — submit

### After HUGS

| When | Work |
|---|---|
| Mid–late Nov | Submit the IRB protocol for Study 2 |
| Nov – Jan | Study 1: generate the ≈60–90-sample corpus, run the tool tier, audit, code the residue |
| 11 Dec | HUGS notification. If accepted: SIGSOFT CAPS, ICSE student volunteering, Niagara travel funds, passport |
| Late Jan | HUGS camera-ready (29 Jan); build the L3 test items from the Study 1 residue |
| Feb | CHI 2027 workshop submission (optional) |
| Feb – Mar | Run Study 2 after IRB approval |
| Mar – Apr | Write and defend |

---

## 6. Thesis outline (planned)

1. **Introduction.** The guiding question; pro-AI stance; origin (classmates fluent in libraries but unable to picture what's underneath, told as a story about the system, not the people).
2. **Background.** Dependency stack (SQ1); memory safety and policy; the Python/C boundary; notional machines; human review of AI code.
3. **Construct.** L1/L2/L3.
4. **Study 1.** Corpus, tools, residue.
5. **Study 2.** Student pilot.
6. **Discussion.** Who catches the agent's mistakes; the specialists counterargument; curriculum implications (curriculum snapshot).
7. **Closing reflection.** "You will need AI to compete," dependence vs. augmentation, and transhumanism, drawing on *Magnifica Humanitas* (cite by paragraph number from the printed copy). Keep normative claims clearly separate from findings.
8. **Limitations and future work.** Everything in the right-hand column of §2.

---

## 7. Threats to validity

- **Prompt realism.** Phrase prompts like real Stack Overflow / GitHub-issue requests; release them.
- **Model drift.** Freeze and release the corpus; report versions and dates. (Hand collection: the exact version isn't visible, so say so.)
- **Ground truth.** Labels can still miss defects; treat the residue as a lower bound; rely on reproduction where there's only one coder.
- **Literacy coding is a judgment.** Publish the codebook with examples; double-code where possible.
- **Small pilot.** Single institution, small n; report effect sizes and intervals, not significance claims.
- **Platform.** macOS/arm64 only (no Valgrind); note it.
- **Measurement differences.** Yang & Cai report NumPy at 38% native; our count is 55.7%. State the counting rule wherever either number is cited.

---

## 8. Evidence rules

- Cite papers, standards and published data. **Don't cite chatbots** (Google AI, ChatGPT, Claude) as sources for claims. Use them for brainstorming only.
- Novelty wording: "We found no prior evaluation of the security of LLM-generated Python/C API code." Nothing stronger.
- Differentiate explicitly from Khalid et al. (S&P 2027).
- Disclose AI assistance as the venue and Niagara require. The AI-generated corpus is labeled as AI-generated, by design.

---

## 9. Must-cite core

1. Khalid et al., S&P 2027 — closest prior art; differentiate explicitly
2. Yang & Cai, arXiv 2026 — boundary bug taxonomy; codebook
3. Hu & Zhang, SANER 2020 / JSEP 2023 — bug patterns
4. Almansoori et al., SIGCSE 2023 (+ Lam et al. 2022) — closest education work; L2 items
5. Sorva, TOCE 2013 — notional machines
6. Edmundson et al., ESSoS 2013 — experience doesn't predict review effectiveness
7. Perry et al., CCS 2023; Sandoval et al., USENIX Security 2023 — AI assistants and security
8. Li, Li & Cai, FSE 2022 — the interfacing mechanism drives vulnerability
9. Braz et al., ICSE 2022; Fulton et al., SOUPS 2024; Tufano et al., ICSE 2025 — Study 2 design choices
10. CISA 2023 / ONCD 2024 — policy framing
11. Brynjolfsson et al. 2025; Lichtinger & Hosseini Maasoum 2025 — junior pipeline (correlational; state the caveat)
12. Firouzi & Ghafari 2026 — why ground truth is triangulated

Full references: see `proposal.md` and `prior-art-review.md`.
