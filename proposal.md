# Reviewing What You Never Wrote

## Memory-Model Literacy and the Human Review of AI-Generated Code at the Python/C Boundary

**Project proposal — undergraduate honors thesis and HUGS 2027 workshop submission**
Jessica Dye · Niagara University · Drafted 22 October 2026

| | |
|---|---|
| **Primary venue** | HUGS 2027 — 1st International Workshop on Human-First Generative Software Engineering, ICSE 2027, Dublin. **3-page extended abstract, due Fri 13 Nov 2026 (AoE).** Notification 11 Dec 2026. |
| **Secondary venue** | ICSE 2027 ACM Student Research Competition (800 words, 2 pp., same deadline). Single-authored; must differ from the HUGS submission by ≥30% in substance. Check SRC one-per-year eligibility first. |
| **Later venue** | CHI 2027 workshops (Pittsburgh), calls released 17 Dec 2026, submissions ~11 Feb 2027 |
| **Thesis defense** | Spring 2027 |

---

## 1. What the background search changed

A quick sweep of the 2022–2026 literature was run before finalizing this design. It changed the proposal in five ways.

1. **"AI writes insecure C" is settled, not novel.** Many studies already document memory-safety defects in LLM-generated C/C++ [Pearce 2022; WildCode Revisited 2025; Liu et al., via SLR 2412.15004]. The paper must not claim this as a finding. It uses this literature as its premise.

2. **The boundary is the real gap.** Firouzi & Ghafari [2026] surveyed 2025 top-tier SE venues. They found that secure-code-generation benchmarks concentrate on Python, and vulnerability-detection benchmarks concentrate on C/C++. They call the result a significant gap in understanding multilingual secure coding. Code that sits *between* Python and C, such as CPython extensions, ctypes, and cffi, falls into that gap. **Scope is narrowed to the Python/C boundary only**; JNI, cgo, and Rust FFI move to future work.

3. **Boundary bugs are mostly ownership-contract bugs, not just memory corruption.** Yang & Cai [2026] studied 216 real native-code bugs in Python projects. Reference counting was involved in 41.7%, foreign-object manipulation in 31.5%, and cross-language exception handling in 31.5%. Reference-count misuse was the largest single memory-safety root cause. Practitioner evidence agrees: a 2026 LLM-agent sweep of C extensions reported 575+ confirmed bugs, and its author estimated only about 20–35% were memory-safety bugs in the strict sense. The rest were Python/C API protocol errors (refcounts, exceptions, GIL) [Diniz 2026]. **This sharpens the original question.** Reference counting *is* CPython's garbage collector. At the boundary, the GC's bookkeeping becomes the programmer's job. So "does a reviewer need GC literacy?" becomes a precise question: *does the reviewer understand the collector's contract well enough to see when C code breaks it?*

4. **AI reviewers are now part of the baseline.** That same LLM-agent toolkit found hundreds of real C-extension bugs, with false positives reported at about 10–15% after review. Any claim that "humans must catch what tools miss" has to include a strong LLM reviewer in the tool tier. If it doesn't, reviewers will dismiss the result.

5. **Static analyzers can't serve as ground truth.** Firouzi & Ghafari [2026] manually labeled 1,080 LLM-generated samples. Only 61% of CodeQL's and 65% of Semgrep's per-sample verdicts matched the human labels. Memory-safety sanitizers also miss bug classes because of incomplete implementations [MSET, S&P 2025]. **Ground truth must be triangulated** (sanitizers, static analysis, LLM review, and a two-coder manual audit), not assumed from any single tool.

The education side also shifted. Two recent studies already train students to distrust insecure LLM output: Bifröst [Park et al. 2025] and CodeWars [Chaudhary et al. 2026]. Both measure *awareness and skepticism* on general vulnerabilities. **Neither measures the underlying mental model of memory.** That is the education-side gap this project targets.

A follow-up prior-art search (see `prior-art-review.md`) found the closest human study. Khalid et al. [S&P 2027] had 100 C-proficient developers evaluate real AI-generated C. They could not tell secure suggestions from insecure ones. Developers with more than 3 years of programming experience submitted *more* vulnerabilities, and security experience had no significant effect. Edmundson et al. [2013] likewise found experience and education did not predict security-review effectiveness. **Prior work measured the wrong variable.** RQ3 tests whether a specific, teachable construct predicts detection where experience does not. The closest education work, Almansoori et al. [SIGCSE 2023], linked students' "knowledge of memory" to *writing* secure C. This project extends that link to *reviewing* AI-generated code at the boundary.

---

## 2. Research question

**Main RQ.** When AI generates code that crosses the Python/C memory-management boundary, which defects survive automated review? What kind of memory-model literacy does a human reviewer need to catch them?

| | Sub-question | Part |
|---|---|---|
| **RQ1** | Which defects in LLM-generated Python/C boundary code survive the combined automated tier (sanitizers, static analysis, LLM review)? | 1 |
| **RQ2** | For each surviving defect, which level of literacy is required to recognize it? Managed-model only, manual-memory, or boundary-contract? | 1 |
| **RQ3** | Among undergraduates, does performance on a three-level literacy instrument predict detection of those surviving defects, and how well calibrated is their confidence? | 2 (pilot) |

### Three levels of memory-model literacy (the core construct)

| Level | What the reader understands | Example question they can answer |
|---|---|---|
| **L1 — Managed model** | References, aliasing, mutation, and object lifetime inside a garbage-collected language | "After `b = a; b.append(1)`, what is `a`?" |
| **L2 — Manual model** | Allocation and release, ownership, dangling and null pointers, and matching free to allocator | "Who frees this buffer, and with which function?" |
| **L3 — Boundary contract** | What the collector guarantees, and the obligations C code takes on to keep those guarantees: new, borrowed, and stolen references; exception state; allocator families | "This call returns a borrowed reference. What happens if a callback runs before it's used?" |

**Hypothesis.** The residue from RQ1 will be dominated by L3 defects. L3 depends on L2 and cannot be inferred from L1 alone. If so, "Python developers don't need low-level literacy" fails exactly where AI-generated code is hardest to verify.

**Framing RQ3 against prior work.** Khalid et al. [S&P 2027] and Edmundson et al. [2013] found that years of experience do not predict detection. RQ3 asks whether a specific, teachable construct (L1/L2/L3 literacy) does. Years of experience are still collected, so the two predictors can be compared directly.

---

## 3. Motivation: the missing rung

Reviewing AI output is becoming the human's main job just as the traditional route to that skill narrows. Brynjolfsson, Chandar & Chen [2025] report a 16% relative employment decline for 22–25-year-olds in AI-exposed occupations. Software developers in that age band fell nearly 20% from their late-2022 peak. Historically, junior developers built memory-model literacy on the job by fixing small, low-stakes bugs under review. If that apprenticeship shrinks, the literacy must be installed before employment, or not at all.

On the learning side, Perry et al. [2023] found that developers using an AI assistant wrote less secure code *and* were more confident it was secure. The epistemic-debt study [2026, preprint] found that novices with unrestricted AI produced the most working code and retained the least ability to repair it.

**Caveat carried into the paper:** the labor data are correlational, and the cause is contested. Hiring slowdowns and interest rates are competing explanations. The paper frames the apprenticeship pathway as under pressure from several causes, AI among them. It makes no stronger claim than that.

---

## 4. Study design

### Part 1 — Corpus study (no IRB, the core of the thesis and the HUGS paper)

**1. Prompts.** Write 30–40 realistic developer requests that force boundary code. Phrase them as a developer would, without hinting at security. Strata:
- CPython C-API extension functions: argument parsing, building and returning containers, calling back into Python
- ctypes and cffi wrappers that pass buffers, strings, and arrays
- Code that must raise or propagate Python exceptions from C

**2. Generation.** Use 3–4 current models with *n* samples per prompt, for a few hundred samples total. Log model, version string, temperature, date, and full prompt. LLM output drifts, so the frozen corpus is itself a released artifact.

**3. Automated tier.** Every sample passes through all of the following:
- Build and run under **ASan/UBSan** and **Valgrind**, using fuzzed and edge-case inputs (`None`, empty, huge, wrong type, exception-raising callbacks)
- **Static analysis:** cppcheck, clang-tidy, and CodeQL
- **LLM review:** a general LLM asked to review the code for safety, plus a boundary-specialized reviewer such as the open-source `cext-review-toolkit` if it is usable for this purpose
- Tool versions and flags pinned in a reproducible script, runnable entirely from the command line

**4. Ground truth.** A manual audit uses a codebook built from Yang & Cai's [2026] root-cause and manifestation taxonomy plus Hu & Zhang's [2020] ten Python/C API bug patterns. A second coder independently audits about 20% of samples, and Cohen's κ is reported. A defect counts as real only if it is reproduced or the two coders agree.

**5. Residue analysis (RQ1).** For each confirmed defect, record which tiers caught it. The **residue** is the set of defects every automated tier missed.

**6. Literacy coding (RQ2).** Code each residue defect by the lowest literacy level at which a reviewer could recognize it (L1 / L2 / L3). Double-code and report κ.

**Outputs:** residue size and composition, a literacy profile of the residue, and the released corpus and scripts.

### Part 2 — Review pilot (IRB required, honors thesis only)

- **Materials:** about 12 snippets drawn from Part 1 (real AI-generated defects, not hand-seeded), plus clean controls
- **Screening:** the validated C-proficiency screening questions (Danilova et al.) used by Khalid et al., so the sample is comparable. Students who fail the screen still take the literacy test, and the screen result is recorded as a covariate.
- **Instrument:** a short literacy test with L1/L2/L3 subscales, built from existing instruments rather than written from scratch:
  - L1 items: adapted from the SPLASH-E 2017 aliasing quizzes and the memory-model misconceptions in Kaczmarczyk et al. [SIGCSE 2010]
  - L2 items: built on the "knowledge of memory" theme and modified SOLO rubric from Almansoori et al. [SIGCSE 2023] and Lam et al. [SIGCSE 2022]
  - L3 items: derived from the Hu & Zhang and Yang & Cai patterns. No validated L3 instrument was found, so building and piloting one is itself a contribution.
- **Task design — Read, not Write.** Participants review provided code and flag defects. They do not write code. Fulton et al. [SOUPS 2024] recommend Read tasks for measuring what developers know, and Read tasks are shorter and less frustrating for participants.
- **Instructions — security focus for everyone.** Every participant is told explicitly to review for security problems. Braz et al. [ICSE 2022] found this instruction alone made detection about 8× more likely, so it must not vary between participants.
- **No AI review shown.** Participants do not see an LLM's review of the snippet. Tufano et al. [ICSE 2025] found reviewers given an automated review focused on its flagged locations rather than searching elsewhere. An "AI review shown" condition is possible future work as a separate arm, not part of this pilot.
- **Confidence:** a confidence rating per verdict, to measure calibration. Perry et al. [CCS 2023] found AI users overconfident; Khalid et al. found confidence tracked actual security. This pilot adds a third data point.
- **Background items:** courses taken; community-college or transfer pathway; where the participant learned memory management (coursework, job or internship, self-taught). This last item is the student-level link to the missing-rung argument.
- **Participants:** 30–60 undergraduates from CS1 through seniors. **Not recruited from any class the author teaches or grades.** The advisor or another instructor announces the study; participation is anonymous. Expected to qualify as exempt (educational test, minimal risk), but the IRB decides.
- **Analysis** (following Khalid et al. so results can be compared):
  - Poisson regression on the number of defects missed per participant, with L1/L2/L3 subscale scores and years of experience as predictors and a random effect for participant
  - Logistic regression on detecting each individual defect, broken down by the defect's literacy level
  - Calibration: the relationship between confidence ratings and correct verdicts
  - Reported as a pilot, with effect sizes and confidence intervals rather than claims of significance

### Defeat conditions (stated in the paper)

- **Automation catches almost everything.** If the combined tier leaves little residue, the case for universal L2/L3 literacy weakens substantially. The paper reports that plainly.
- **L1 predicts detection as well as L3.** Then GC-level literacy is sufficient, and the "you need C" claim fails.
- **The LLM reviewer alone matches the full tier.** The human role shifts from finding defects to verifying the verifier, which is a narrower claim.
- **No predictor works.** If literacy predicts detection no better than experience does, this replicates Edmundson et al. and Khalid et al. at the boundary. That is still a reportable result: the literacy the curriculum teaches would not be what makes a reviewer effective.

---

## 5. Positioning against related work

| Strand | Representative work | What it leaves open |
|---|---|---|
| Security of LLM-generated code | Pearce et al. 2022; WildCode 2025; SLR 2412.15004; CHERI study (Glasgow) | Mostly standalone C or web code, not cross-language boundary code |
| Native and boundary bugs in Python | Hu & Zhang 2020/2023; Yang & Cai 2026; Ma et al. ASE 2023 | Human-written bugs. Never asks what reviewers need to know. |
| LLMs as bug finders | `cext-review-toolkit` (Diniz 2026); SecureMind (ISMM 2025); Revelio (2026) | Measure tools, not the human residue |
| Human use and review of AI code | Khalid et al. S&P 2027; Sandoval et al. USENIX Sec 2023; Perry et al. CCS 2023; Oh et al. S&P 2024 | Plain C or general vulnerabilities; predictors are years of experience, not a memory-model construct |
| Human security code review | Edmundson et al. ESSoS 2013; Braz et al. ICSE 2021/2022; Tufano et al. ICSE 2025 | Experience doesn't predict effectiveness; nobody tests a specific literacy |
| Secure-programming education | Almansoori et al. SIGCSE 2023; Lam et al. SIGCSE 2022; Votipka et al. USENIX Sec 2020 | Knowledge of memory linked to *writing* secure C, not reviewing AI code at the boundary |
| Teaching security with LLM code | Bifröst (Park et al. 2025); CodeWars (Chaudhary et al. 2026) | Measure awareness and skepticism, not literacy in the memory model |
| Notional machines and misconceptions | Sorva 2013; SPLASH-E 2017 aliasing study; Kaczmarczyk et al. SIGCSE 2010 | Not connected to security review or AI-generated code |
| LLM-generated binding code | OMPL nanobind study (2026) | States no benchmark exists for binding generation; does not measure security |

**Novelty claim (kept modest and worded precisely):** the methods are standard. The contribution is the question: connecting the residue that survives automated review to a specific, teachable level of memory-model literacy, at the boundary where most of the scientific and ML Python stack actually runs. The paper says *"we found no prior evaluation of the security of LLM-generated Python/C API code"*, citing the OMPL study's statement that no benchmark exists for binding generation. It does not claim no such work exists. A library check of ACM DL and IEEE Xplore is done before submission.

---

## 6. HUGS extended abstract (3 pages including references)

HUGS invites early ideas, position papers, and research agendas, with interest in human-in-the-loop verification and independent review. The abstract is pitched as **early results plus research agenda**.

| Section | Budget | Content |
|---|---|---|
| Problem | ~0.4 p | AI generates boundary code; review is the human's remaining job; prior human studies found experience doesn't predict detection (Khalid et al., Edmundson et al.); the junior apprenticeship that taught the needed literacy is shrinking |
| The construct | ~0.4 p | The L1/L2/L3 table, and the point that refcounting *is* the GC's contract |
| Pilot | ~0.9 p | ~10 prompts × 2 models; residue after sanitizers, static analysis, and LLM review; literacy profile of the residue; one small table |
| Agenda | ~0.5 p | Full corpus; student review study; defeat conditions; questions for breakout discussion |
| References | ~0.8 p | 12–15 entries |

### Three weeks to 13 November

| Dates | Work |
|---|---|
| 22–28 Oct | Advisor sign-off on scope. Write 10 pilot prompts. Build the generate → compile → sanitize → analyze pipeline. Start ACM membership if pursuing the SRC. |
| 29 Oct – 4 Nov | Generate the pilot corpus (~10 prompts × 2 models × 3 samples). Run the automated tier. Manually audit with the codebook. |
| 5–10 Nov | Literacy-code the residue. Second-coder pass on a subset. Draft the abstract in the IEEE template. |
| 11–13 Nov | Advisor read, revise, submit to HUGS (and the SRC if eligible) |

## 7. Thesis timeline after submission

| When | Work |
|---|---|
| Nov | Submit IRB protocol for Part 2 |
| Nov–Jan | Scale Part 1 to the full 30–40 prompts × 3–4 models; complete audit and κ |
| 11 Dec | HUGS notification. If accepted: apply for SIGSOFT CAPS, ICSE student volunteering, and Niagara travel funds |
| Feb | CHI 2027 workshop submission with full Part 1 results (drivable venue) |
| Feb–Mar | Run Part 2 after IRB approval |
| Mar–Apr | Write and defend the thesis |
| Late Apr | Present at HUGS, Dublin (if accepted) |

## 8. Threats to validity

- **Prompt realism.** Results depend on prompt wording. Mitigation: phrase prompts from real Stack Overflow and GitHub-issue requests, and release them.
- **Model drift.** Freeze and release the corpus, and report versions and dates.
- **Ground truth.** Even triangulated labels can miss defects. Report the second-coder κ and treat the residue as a lower bound.
- **Literacy coding is a judgment.** Double-code and publish the codebook with examples.
- **Pilot generalization.** Part 2 is single-institution with a small n, so it is reported as a pilot.
- **Measurement differences.** Yang & Cai report NumPy as 38% native code; the author's own repository measurement found 55.7%, with the difference likely due to file classification and vendored-code rules. State the measurement rule whenever these figures are cited.

---

## References

**AI-generated code security**
- Pearce, H. et al. "Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions." IEEE S&P 2022.
- Perry, N., Srivastava, M., Kumar, D., Boneh, D. "Do Users Write More Insecure Code with AI Assistants?" ACM CCS 2023. https://doi.org/10.1145/3576915.3623157
- "WildCode Revisited: A Comprehensive Empirical Study on the Security of LLM-Generated Code." arXiv:2512.04259 (2025). *Preprint.*
- "From Vulnerabilities to Remediation: A Systematic Literature Review of LLMs in Code Security." arXiv:2412.15004.
- Firouzi, E., Ghafari, M. "Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection." arXiv:2602.05868 (2026). *Preprint.*
- "Evaluating and Enhancing Memory Safety in LLM-Generated Code on CHERI." University of Glasgow. https://eprints.gla.ac.uk/381094/

**Python/C boundary bugs**
- Hu, M., Zhang, Y. "The Python/C API: Evolution, Usage Statistics, and Bug Patterns." SANER 2020; extended in J. Softw. Evol. Process 35(2), 2023. Replication package: github.com/S4Plus/pyceac
- Yang, H., Cai, H. "A Comprehensive Study of Native Code Bugs in Python Applications." arXiv:2608.29851 (2026). *Preprint, manuscript submitted to ACM.*
- Ma, X. et al. "Detecting Memory Errors in Python Native Code by Tracking Object Lifecycle with Reference Count." ASE 2023.
- Li, S., Tan, G. "Finding Reference-Counting Errors in Python/C Programs with Affine Analysis." ECOOP 2014.
- Diniz, D. "Systematically finding bugs in Python C extensions (575+ confirmed so far)." discuss.python.org (2026); summarized in LWN.net, "Using LLMs to find Python C-extension bugs." *Practitioner source.*

**Tools and oracles**
- MSET: "Evaluating the Effectiveness of Memory Safety Sanitizers." IEEE S&P 2025. doi:10.1109/SP61157.2025.00088
- Wang, H. et al. "SecureMind: A Framework for Benchmarking LLMs in Memory Bug Detection and Repair." ISMM 2025. doi:10.1145/3735950.3735954
- "OSS-Bench: Benchmark Generator for Coding LLMs." arXiv:2505.12331.

**Human review of code (added after the prior-art search)**
- Khalid, H., Thompson, R. E., Sabater, A., Mussiba, P., Fulton, K. R., Votipka, D. "(Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code." IEEE S&P 2027 (to appear). arXiv:2609.21020
- Sandoval, G., Pearce, H., Nys, T., Karri, R., Garg, S., Dolan-Gavitt, B. "Lost at C: A User Study on the Security Implications of Large Language Model Code Assistants." USENIX Security 2023.
- Oh, S., Lee, K., Park, S., Kim, D., Kim, H. "Poisoned ChatGPT Finds Work for Idle Hands." IEEE S&P 2024.
- Edmundson, A., et al. "An Empirical Study on the Effectiveness of Security Code Review." ESSoS 2013.
- Braz, L., Aeberhard, C., Çalikli, G., Bacchelli, A. "Less is More: Supporting Developers in Vulnerability Detection during Code Review." ICSE 2022.
- Fulton, K. R., Lewis, J., Malkin, N., Mazurek, M. L. "Write, Read, or Fix? Exploring Alternative Methods for Secure Development Studies." SOUPS 2024.
- Tufano, R., et al. "Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?" ICSE 2025.
- Li, W., Li, L., Cai, H. "On the Vulnerability Proneness of Multilingual Code." ESEC/FSE 2022.
- "Python Bindings for a Large C++ Robotics Library: The Case of OMPL." arXiv:2603.04668 (2026). *Preprint.*

**Education**
- Almansoori, M., Lam, J., Fang, E., Soosai Raj, A. G., Chatterjee, R. "Towards Finding the Missing Pieces to Teach Secure Programming Skills to Students." SIGCSE 2023.
- Lam, J., Fang, E., Almansoori, M., Chatterjee, R., Soosai Raj, A. G. "Identifying Gaps in the Secure Programming Knowledge and Skills of Students." SIGCSE 2022.
- Kaczmarczyk, L. C., Petrick, E. R., East, J. P., Herman, G. L. "Identifying Student Misconceptions of Programming." SIGCSE 2010.
- Votipka, D., et al. "Understanding Security Mistakes Developers Make: Qualitative Analysis from Build It, Break It, Fix It." USENIX Security 2020.
- Park, J., Lim, K., Park, S., Kim, D. "Supporting Students in Navigating LLM-Generated Insecure Code" (Bifröst). arXiv:2511.20878 (2025). *Preprint.*
- Chaudhary, A. et al. "CodeWars: Using LLMs for Vulnerability Analysis in Cybersecurity Education." J. Colloquium for Information Systems Security Education 13(1), 2026.
- Sorva, J. "Notional Machines and Introductory Programming Education." ACM TOCE, 2013.
- "Student Understanding of Aliasing and Procedure Calls." SPLASH-E 2017.
- "Mitigating 'Epistemic Debt'…" ACM L@S 2026; arXiv:2602.20206. *Preprint.*

**Workforce**
- Lichtinger, G., Hosseini Maasoum, S. M. "Generative AI as Seniority-Biased Technological Change: Evidence from U.S. Résumé and Job Posting Data." SSRN 5425555 (2025).
- Brynjolfsson, E., Chandar, B., Chen, R. "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence." Stanford Digital Economy Lab, 2025.

*Before submission: confirm every preprint's current status, and fill in full author lists where marked.*
