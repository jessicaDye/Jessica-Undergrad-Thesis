# The AI Question — Does It Break the Thesis?

Drafted 28 Aug 2026.

## Cancel the interlibrary loan

JSEP 2023 is the extended version of a SANER 2020 conference paper by the same authors (Hu & Zhang, USTC): *The Python/C API: Evolution, Usage Statistics, and Bug Patterns*. **Full PDF is free in their replication repo** — `S4Plus/pyceac` on GitHub — along with corpus, checkers, and data. Get the journal version eventually via ILL (extended versions add RQs and corpus), but you're unblocked now.

**Quote this sentence.** Explaining a memory bug in Pillow's C extension, the authors write the required cleanup is *"often missed by developers because they need not do this in pure Python code."* That is a peer-reviewed statement that Python-trained developers introduce memory-safety defects at the boundary *because their training didn't build the habit* — written by SE researchers not trying to make an education argument. Closest thing to a direct statement of the thesis in the literature.

## Is 2023 stale?

For this citation, no. The Python/C API is slow-moving — reference counting, `Py_DECREF` discipline, the exception contract at the boundary are stable. The 10 bug-pattern taxonomy describes a structural property of a boundary that still exists. Not citing it for an AI claim.

Apply the instinct selectively: industry/tooling claims need recent sources; developer-practice claims from before ~2023 describe a different world. Repository data solves this for composition — measuring HEAD directly.

## The strong objection (steelman)

*The skill is being unbundled. AI already finds and patches memory-safety bugs in C at meaningful rates. If verification becomes machine work too, "humans must understand the native core" is a transitional need, not a permanent one — and curricula shouldn't be rebuilt around transitional needs. Plus AI tutoring lowers the cost of learning this on demand, so even a persistent need doesn't imply required coursework.*

## Evidence AI WEAKENS the case — do not bury this

**DARPA AIxCC finals, Aug 2025:** 54/63 synthetic vulns discovered (86%), 43 patched (68%). **18 real non-synthetic vulns found in real OSS, 11 patched.** 45 min avg to patch, $152 avg per task. All 7 finalists found ≥1 real vuln. Up from 37%/25% in the 2024 semifinals — steep trajectory.

**Systems did BETTER on C than Java:** 30/40 fuzzable C vulns vs 4/23 Java. Memory-safety bugs in C are the *most* automatable class — exactly what fuzzers and sanitizers target. This complicates any claim that native code uniquely needs scarce human attention.

## Evidence AI STRENGTHENS the case

- **Half of AIxCC needed no AI:** 34/63 PoVs and 31/63 patches solvable by parallel fuzzing under ideal lab conditions. Genuine AI contribution was narrower — 22 vulns fuzzing couldn't reach.
- **Human verification stayed necessary:** patches passing automated checks still needed manual review for semantic incorrectness; deciding factor between teams was engineering stability, not algorithms. DARPA's framing: an "edge," not a replacement.
- **AI-generated C has its own security problem:** *LLM-CSEC* (arXiv 2511.18966, Nov 2025, **preprint — verify**) — 10 models, CWE-classified, CVE-mapped; authors call the weakness volume concerning. More machine-written native code → *more* human review needed, not less.
- **The key education finding — *Mitigating "Epistemic Debt"*** (ACM L@S June 2026, arXiv 2602.20206, **preprint**), 78 novices, 3 conditions, phase 2 removed AI and required fixing an injected race condition:

| Condition | Phase 1 functionality | Phase 2 repair success |
|---|---|---|
| Manual (control) | 65% | **69%** |
| AI + explanation gate | ~90% | **61%** |
| Unrestricted AI | ~90% | **23%** |

The unrestricted group produced the most working software and retained the least ability to repair it. *Epistemic debt* = "functional software artifacts the user 'owns' legally but does not 'own' cognitively."

- **Supporting:** *Beginners Struggle to Understand LLM-Generated Code* (FSE Companion 2025) — 32 CS1 students, 160 tasks: 59.3% prompt comprehension vs **32.5% code comprehension**, automation bias named as a barrier. **Conducted in Python.** Prospects for auditing LLM-generated C are not better.

## Where this leaves the thesis — it relocates, and sharpens

**Old claim:** students should learn C because someone has to write the native core.

**Evidence-supported claim:** as generation moves to machines, the scarce human capability shifts from *writing* native code to *verifying* it. Verification of memory-unsafe code requires a mental model AI assistance demonstrably does not install — and may suppress, since the students who produced the most working code retained the least ability to repair it. Curricula that dropped low-level programming because students "would never write C" optimized for the task that automated first and neglected the one that didn't.

Better because: it's about 2027 not 2005; it converts the AI objection into the motivating tension; it targets a decision programs are making now.

Jessica's own framing — *how will future engineers maintain these libraries without knowing what's under the hood* — sharpens to: **they'll be able to produce changes to these libraries without understanding them, and that's the risk.**

## Be honest about what can't be settled

Do not claim the AI counterargument is defeated. Defensible position: open empirical question on a timeline nobody can resolve today, while curricular decisions are being made *now* on assumptions current evidence doesn't support. **Name the defeat conditions** — if autonomous patching reaches high reliability on real codebases without human verification, the case for universal low-level literacy weakens considerably. Naming them reads as confident, not weak.

## Risk to manage

AI-in-CS-ed is the most crowded topic at SIGCSE/ITiCSE right now. Danger of being sorted into a pile with forty others.

**Protection: lead with the repository data** (native core +46% while Python took over teaching), let AI enter as the tension that makes those numbers matter. Lead with AI → competing in the crowd. Lead with data, AI in the discussion → the paper with evidence.

## Study 5 (optional, ITiCSE not SRC)

Where does AI assistance land in the stack? Sample recent merged PRs touching native vs Python files; record AI-assistance disclosure (co-author trailers, PR checkboxes, bot labels). Projects vary in disclosure requirements — treat as exploratory, report the limitation prominently. Null/messy result still informative. **Don't let it eat the five weeks.**
