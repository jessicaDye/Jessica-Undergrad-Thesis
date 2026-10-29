# Prior-Art Review: *Reviewing What You Never Wrote*

**Companion to proposal.md** · Compiled 22 October 2026
**Question checked:** Has anyone already shown which memory-model literacy a human needs to catch the security defects that AI leaves in Python/C boundary code? And what literature should the introduction stand on?

---

## 1. Bottom line

**No paper found answers the research question.** The question sits where three literatures meet, and each one stops short of it:

| Literature | What it has established | Where it stops |
|---|---|---|
| Human review of AI-generated code | Developers struggle to tell secure AI suggestions from insecure ones, including in C | Measures *years of experience*, not what the reviewer understands about memory |
| Python/C boundary bugs | Real native-code bugs are dominated by reference counting, foreign-object handling, and exception handling | All human-written bugs. Nobody asks what a reviewer must know to catch them. |
| Secure-programming education | Students' "knowledge of memory" correlates with writing secure C | Writing, not reviewing. Plain C, not the GC boundary. No AI. |

**The closest single paper** is Khalid et al., *(Don't) Trust, but (Don't) Verify* (to appear at IEEE S&P 2027). In it, 100 developers evaluated real AI-generated C linked-list code. They could not reliably tell secure suggestions from insecure ones. It is the study yours most needs to cite and differentiate from (§3.1).

**Two findings that complicate the hypothesis.** Address both directly:

1. In Khalid et al., developers with more than 3 years of programming experience submitted *more* vulnerabilities, not fewer. Security experience had no significant effect.
2. Edmundson et al. (2013) found that experience and education did not predict effectiveness at security code review.

These cut both ways. They show the obvious proxy (experience) doesn't work, which is an argument for measuring literacy directly, as your instrument does. They also warn that a null result is entirely possible. Put this in the paper as the motivation for RQ3: *prior work measured the wrong variable.*

---

## 2. Changes this search suggests for proposal.md

1. **Position RQ3 against Khalid et al.** explicitly: "Prior work found experience does not predict detection; we test whether a specific, teachable construct does."
2. **Borrow their measurement design.** Use validated C screening questions (Danilova et al., cited by Khalid et al.), a Poisson regression on vulnerability counts, and a per-verdict confidence measure. Khalid et al. found confidence *was* calibrated, which contradicts Perry et al. Your calibration result now has two priors to compare against.
3. **Use a "Read" task, and cite it as a method.** Fulton et al. (SOUPS 2024) compared Write, Read, and Fix study designs. They recommend Read for measuring what developers know. That is exactly what Part 2 does.
4. **Tell every participant to look for security problems.** Braz et al. (ICSE 2022) found that simply asking reviewers to focus on security made them about 8× more likely to detect a vulnerability. If instructions vary, that effect would swamp any literacy effect.
5. **Do not show participants an LLM review.** Tufano et al. (ICSE 2025) found reviewers given an automated review tended to focus only on the locations it flagged. If you want this as a condition, make it a separate arm.
6. **Build the L2 items from existing instruments.** Use Almansoori et al.'s "knowledge of memory" theme and SOLO-based rubric (SIGCSE 2023), plus Kaczmarczyk et al.'s memory-model misconceptions (SIGCSE 2010). Don't write them from scratch.
7. **Word the novelty claim carefully.** A 2026 study of LLM-generated nanobind bindings states that no benchmark exists for binding generation. Combine that with the absence of security studies of LLM-written CPython-API code: "We found no prior evaluation of the security of LLM-generated Python/C API code."

---

## 3. Closest prior art, by research question

### 3.1 RQ3 — Can humans catch defects in AI-generated low-level code?

**Khalid, Thompson, Sabater, Mussiba, Fulton & Votipka. "(Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code." IEEE S&P 2027 (to appear); arXiv:2609.21020.**

- *What they did:* 100 participants, about 88% freelancers and 12% university-recruited. All were screened for C proficiency. Each completed four C linked-list tasks, cycling through five real AI suggestions per task, drawn from the Sandoval et al. corpus. Logs, a survey, and 23 interviews.
- *Findings:*
  - No difference in how often participants picked the most-secure versus least-secure suggestions.
  - Only 22% of submissions were fully secure.
  - Participants who edited more produced fewer vulnerabilities.
  - More than 3 years of programming experience was associated with *more* vulnerabilities; security experience had no significant effect.
  - Confidence tracked actual security.
  - Most interviewees took no explicit security step. Many judged security by whether the code had a visible edge-case-handling block.
  - Memory safety was the cue participants mentioned most when they did think about security.
  - The authors conclude the burden should shift to tools.
- *Relation to your study:* Same question family in plain C with real AI code. Their predictors are years of experience; **yours is a literacy construct**. They studied plain C linked lists; **you study the GC boundary**. Their participant pool is mostly freelancers; **yours is students across the curriculum**. Their conclusion ("shift the burden to tools") is exactly what Part 1 tests: what is left after the tools run?

**Sandoval, Pearce, Nys, Karri, Garg & Dolan-Gavitt. "Lost at C: A User Study on the Security Implications of LLM Code Assistants." USENIX Security 2023.**

- 58 student programmers implemented a singly linked list in C, with or without an LLM assistant.
- The AI-assisted group produced critical security bugs at a rate no more than about 10% above the control group.
- *Relation:* the counter-finding. In low-level C, AI assistance did not clearly make student code less secure. Cite it to show you are not assuming AI makes things worse. Your question is about review, not authorship. Its released corpus is the one Khalid et al. reused, and you could reuse it too.

**Perry, Srivastava, Kumar & Boneh. "Do Users Write More Insecure Code with AI Assistants?" ACM CCS 2023.**

- Participants with AI access wrote less secure code *and* were more likely to believe it was secure.
- *Relation:* the canonical overconfidence result. Read it alongside Khalid et al., who found calibration. Your confidence measure helps reconcile the two.

**Asare, Nagappan & Asokan. "Is GitHub's Copilot as Bad as Humans at Introducing Vulnerabilities in Code?" Empirical Software Engineering, 2023;** plus their user-centered follow-up at ICSE 2024.

- Copilot reproduced the original vulnerable C/C++ code about 33% of the time and the fixed code about 25% of the time.
- The follow-up user study found no significant security difference with Copilot access.
- *Relation:* evidence that AI-generated code is not uniformly worse than human code. That supports framing your study around review, not around "AI code is bad."

**Oh, Lee, Park, Kim & Kim. "Poisoned ChatGPT Finds Work for Idle Hands." IEEE S&P 2024.**

- 30 professional developers. Those using a poisoned chat-style assistant included insecure code more often than those using a completion-style tool or no tool.
- *Relation:* chat-style generation makes uncritical adoption more likely. Your corpus uses chat-style generation.

**Edmundson et al. "An Empirical Study on the Effectiveness of Security Code Review." ESSoS 2013.**

- 30 hired developers reviewed a small web app with known vulnerabilities. None found all of them.
- Experience and education did not correlate with effectiveness.
- *Relation:* the classic baseline that human security review is weak and uneven. It is also the strongest prior warning against expecting a clean predictor.

**Braz, Fregnan, Çalikli & Bacchelli. "Why Don't Developers Detect Improper Input Validation?" ICSE 2021** (146 participants); **Braz, Aeberhard, Çalikli & Bacchelli. "Less is More." ICSE 2022** (150 participants).

- Many developers miss easy vulnerabilities but find them once warned.
- An explicit security-focus instruction raised detection about eightfold. A checklist added nothing significant beyond that.
- *Relation:* sets your instructions (all participants told to review for security), and it is a reminder that a checklist alone is not a curriculum.

**Fulton, Lewis, Malkin & Mazurek. "Write, Read, or Fix? Exploring Alternative Methods for Secure Development Studies." SOUPS 2024.**

- Compared writing code, reading code to find issues, and fixing provided code. Read and Fix revealed fewer API problems than Write but still gave useful insights, and participants found them less frustrating.
- *Relation:* methodological justification for the review-task design in Part 2.

**Tufano, Martin-Lopez, Tayeb, Dabić, Haiduc & Bavota. "Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?" ICSE 2025.**

- 29 experts reviewed code with or without an LLM-generated review. Those with one concentrated on the flagged locations rather than searching elsewhere.
- *Relation:* the anchoring risk if your pipeline hands humans an AI review. Also intro evidence that an AI in the review loop does not simply add coverage.

**Education-specific human studies.** Each is related, but none uses memory-model literacy as a predictor.

- **Park, Lim, Park & Kim. "Supporting Students in Navigating LLM-Generated Insecure Code" (Bifröst). arXiv:2511.20878, 2025.** A classroom framework using deliberately insecure LLMs. Deployments with 61 students; a survey of 21 showed increased skepticism afterward.
- **Chaudhary et al. "CodeWars." J. Colloquium for Information Systems Security Education 13(1), 2026.** 32 students analyzed flawed, secure, and mixed-origin code.
- **Zi et al. "I Would Have Written My Code Differently." FSE 2025.** Beginners struggle to understand LLM-generated code they did not write.
- **Prather et al. "The Widening Gap." ICER 2024.** 21 novices in an introductory C++ course. GenAI helped students who already had strong metacognition and compounded difficulties for those who struggled.

### 3.2 RQ1 — What survives automated review at the Python/C boundary?

**Yang & Cai. "A Comprehensive Study of Native Code Bugs in Python Applications." arXiv:2608.29851 (2026; manuscript submitted to ACM).**

- 1,039 confirmed native-bug-fixing commits from 200 Python-C projects; 216 analyzed in depth.
- How the bugs showed up: reference counting in 41.7%, foreign-object manipulation in 31.5%, cross-language exception handling in 31.5%.
- Root causes: memory safety in 29.2%, mostly reference-count misuse and null dereference.
- The main obstacle to automated detection, in 52.8% of cases, was semantic differences between the two languages.
- *Relation:* your primary codebook source for real bugs. Its "detection challenges" finding is an a-priori reason to expect a non-empty residue after automated tools.

**Hu & Zhang. "The Python/C API: Evolution, Usage Statistics, and Bug Patterns." SANER 2020;** extended in *J. Softw. Evol. Process* 35(2), 2023. Already in your files. Ten bug patterns, plus a public replication package.

**Li, Li & Cai. "On the Vulnerability Proneness of Multilingual Code." ESEC/FSE 2022.**

- Large-scale GitHub study. Vulnerability proneness was significantly associated with language selection, and the association tracked the *interfacing mechanism*, not the individual languages.
- *Relation:* the empirical basis for the claim that the boundary itself is the risk.

**Staicu et al. "Bilingual Problems." USENIX Security 2023.** Already in your files. Native extensions break the scripting language's safety guarantees.

**LLMs and binding/boundary code.** This is the gap:

- **"Python Bindings for a Large C++ Robotics Library: The Case of OMPL." arXiv:2603.04668 (2026).** States that no benchmark covers LLM generation of language bindings. LLMs frequently mishandled shared-pointer ownership in generated nanobind code.
- **Diniz, `cext-review-toolkit` (2026).** Practitioner source (discuss.python.org; summarized in LWN.net). An LLM-agent reviewer found 575+ confirmed bugs in C extensions, with about 10–15% false positives after review. The author notes that conventional tools struggle with Python C-API semantics. Use it as your strongest automated tier and cite it as grey literature.
- **No peer-reviewed study was found that measures the security of LLM-*generated* CPython-API or ctypes code.** This is the specific gap Part 1 fills.

**Automated-tier reliability (why ground truth must be triangulated):**

- **Firouzi & Ghafari. arXiv:2602.05868 (2026).** On 1,080 human-labeled LLM samples, only about 61–65% of CodeQL and Semgrep per-sample verdicts matched ground truth. They also note benchmarks split by language: Python for generation, C/C++ for detection.
- **MSET. "Evaluating the Effectiveness of Memory Safety Sanitizers." IEEE S&P 2025.** Sanitizers fall short of their conceptual coverage because of incomplete or faulty implementations.

### 3.3 RQ2 — Which literacy level does the residue require?

**Almansoori, Lam, Fang, Soosai Raj & Chatterjee. "Towards Finding the Missing Pieces to Teach Secure Programming Skills to Students." SIGCSE 2023;** preceded by **Lam et al., "Identifying Gaps in the Secure Programming Knowledge and Skills of Students," SIGCSE 2022.**

- Coding interviews with 21 students at two R1 universities.
- Six themes, including *knowledge of memory*, each assessed with a modified SOLO rubric.
- Students at the lowest SOLO levels generally failed to write secure code.
- *Relation:* **the closest education prior art to RQ2/RQ3.** Knowledge of memory is linked to secure *writing*; you extend that to *reviewing* AI code at the boundary. Reuse their rubric for your L2 items.

**Votipka, Fulton, Parker, Hou, Mazurek & Hicks. "Understanding Security Mistakes Developers Make." USENIX Security 2020** (Distinguished Paper).

- 94 Build-It-Break-It-Fix-It submissions. Vulnerabilities from misunderstanding security concepts appeared in 78% of projects, versus 21% for simple mistakes.
- *Relation:* security failures are mostly conceptual, not careless. That is the theoretical case for measuring a *conceptual* literacy rather than diligence.

**Kaczmarczyk, Petrick, East & Herman. "Identifying Student Misconceptions of Programming." SIGCSE 2010.**

- Memory model, references, and pointers formed a major misconception theme in CS1 interviews, including students' misunderstanding of how language constructs relate to memory use.
- *Relation:* item sources for L1 and L2, and a long-standing citation that memory-model misconceptions are widespread.

**Also in your files:** Sorva (TOCE 2013) on notional machines, the SPLASH-E 2017 aliasing study, Hu & Zhang (2020) on Python-trained developers missing `Py_DECREF`, and the epistemic-debt study.

**No validated instrument for L3 (boundary-contract literacy) was found.** Building and piloting even a short one is itself a contribution. Say so.

---

## 4. Introduction scaffold

One paragraph per move, with the sources that carry it.

**¶1 — Memory safety is the dominant vulnerability class, and policy has noticed.**
CISA/NSA/FBI and partners, *The Case for Memory Safe Roadmaps* (Dec 2023): memory-safety bugs are the most prevalent disclosed vulnerability type, and about two-thirds of vulnerabilities in memory-unsafe languages still relate to memory. ONCD, *Back to the Building Blocks* (Feb 2024): calls for memory-safe languages. The guidance targets manufacturers, not training. That is your policy hook.

**¶2 — "Memory-safe" Python runs on a memory-unsafe core, and the seam is where it breaks.**
Your own repository measurements (NumPy ~56% native). Li, Li & Cai (FSE 2022): the interfacing mechanism, not the language, tracks vulnerability proneness. Yang & Cai (2026): boundary bugs are dominated by reference counting and exception contracts. Staicu et al. (2023): native extensions void the host language's guarantees.

**¶3 — Increasingly, that code is written by AI.**
Pearce et al. (S&P 2022), Asare et al. (EMSE 2023), and WildCode Revisited (2025) on the security of AI-generated code, with honest mixed results (Sandoval et al. 2023). No benchmark yet covers boundary or binding code (OMPL 2026), and no study measures its security.

**¶4 — Human review is the stated safeguard, and it is weak.**
Edmundson et al. (2013): low effectiveness, not predicted by experience. Braz et al. (2021, 2022): easy vulnerabilities missed without a security prompt. Khalid et al. (2027): developers can't distinguish secure from insecure AI-generated C, and experience doesn't help. Tufano et al. (2025): AI reviews narrow where humans look.

**¶5 — The apprenticeship that built reviewers is shrinking.**
Lichtinger & Hosseini Maasoum (2025): in firms adopting GenAI, junior employment fell relative to non-adopters through slower hiring, while senior employment held. Brynjolfsson, Chandar & Chen (2025): a relative decline for 22–25-year-olds in AI-exposed jobs. Prather et al. (ICER 2024) and the epistemic-debt study: AI can compound novices' difficulties and erode repair ability. *Keep the causal caveat from proposal §3.*

**¶6 — Gap and contribution.**
Prior human studies measured experience and found it wanting. Prior education work linked memory knowledge to secure *writing*. Nobody has (a) characterized what survives automated review in AI-generated boundary code, or (b) tested whether a specific, teachable memory-model literacy predicts catching it.

---

## 5. Must-cite list, ranked

| # | Paper | Why it is essential |
|---|---|---|
| 1 | Khalid et al., S&P 2027 | Closest prior art; differentiate explicitly |
| 2 | Yang & Cai, arXiv 2026 | Boundary bug taxonomy; codebook |
| 3 | Almansoori et al., SIGCSE 2023 (+ Lam et al. 2022) | Closest education work; L2 rubric |
| 4 | Hu & Zhang, SANER 2020 / JSEP 2023 | Bug patterns; a direct statement of the training gap |
| 5 | Sandoval et al., USENIX Sec 2023 | Counter-finding; reusable C corpus |
| 6 | Perry et al., CCS 2023 | Overconfidence baseline |
| 7 | Edmundson et al., ESSoS 2013 | Experience doesn't predict review effectiveness |
| 8 | Li, Li & Cai, FSE 2022 | Interfacing mechanism drives vulnerability |
| 9 | Braz et al., ICSE 2022 | Controls your instructions |
| 10 | Fulton et al., SOUPS 2024 | Justifies the Read-task design |
| 11 | Tufano et al., ICSE 2025 | Anchoring on AI review |
| 12 | Votipka et al., USENIX Sec 2020 | Conceptual, not careless, errors |
| 13 | CISA 2023 / ONCD 2024 | Policy framing |
| 14 | Lichtinger & Hosseini Maasoum 2025; Brynjolfsson et al. 2025 | Pipeline argument |
| 15 | Firouzi & Ghafari 2026; MSET 2025 | Why ground truth is triangulated |

---

## 6. A note for PhD applications

Haipeng Cai, the senior author of both the multilingual vulnerability-proneness study (FSE 2022) and the 2026 native-code-bug study, is now a tenured Associate Professor in Computer Science and Engineering at the **University at Buffalo**. His group's work underpins Part 1 of this project. That is directly relevant to the UB application: cite his work prominently, and consider asking your advisor about an introduction once you have pilot results.

---

## 7. Gaps in this search and things to verify

- **Preprints:** Khalid et al. (accepted at S&P 2027, preprint text), Yang & Cai, Bifröst, Firouzi & Ghafari, OMPL bindings, WildCode Revisited, and the epistemic-debt study. Check for archival versions before final submission.
- **Not found:** any peer-reviewed security evaluation of LLM-generated CPython-API or ctypes code; any validated boundary-contract (L3) literacy instrument; any study using memory-model literacy as a predictor of reviewing AI code. One extended search per gap was run, and absence of evidence is not proof. Ask your advisor to run a quick ACM DL / IEEE Xplore check through the library.
- **Not yet read in full:** Almansoori et al. 2023 (for the exact rubric), Lichtinger & Hosseini Maasoum (for the effect size you quote), and Serafini et al. (the security-warning AI study cited by Khalid et al.; title and venue not confirmed here).

---

## References

- Almansoori, M., Lam, J., Fang, E., Soosai Raj, A. G., Chatterjee, R. "Towards Finding the Missing Pieces to Teach Secure Programming Skills to Students." SIGCSE 2023. https://pages.cs.wisc.edu/~chatterjee/papers/sigcse23-missingpieces.pdf
- Asare, O., Nagappan, M., Asokan, N. "Is GitHub's Copilot as Bad as Humans at Introducing Vulnerabilities in Code?" Empirical Software Engineering, 2023. https://arxiv.org/abs/2204.04741
- Braz, L., Fregnan, E., Çalikli, G., Bacchelli, A. "Why Don't Developers Detect Improper Input Validation?" ICSE 2021. https://arxiv.org/abs/2102.06251
- Braz, L., Aeberhard, C., Çalikli, G., Bacchelli, A. "Less is More: Supporting Developers in Vulnerability Detection during Code Review." ICSE 2022. https://arxiv.org/abs/2202.04586
- Brynjolfsson, E., Chandar, B., Chen, R. "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence." Stanford Digital Economy Lab, 2025.
- Chaudhary, A., et al. "CodeWars: Using LLMs for Vulnerability Analysis in Cybersecurity Education." JCISSE 13(1), 2026. https://orca.cardiff.ac.uk/id/eprint/184816
- CISA, NSA, FBI, et al. "The Case for Memory Safe Roadmaps." December 2023. https://cisa.gov/case-memory-safe-roadmaps
- Diniz, D. "Systematically finding bugs in Python C extensions (575+ confirmed so far)." discuss.python.org, 2026; LWN.net summary: https://lwn.net/Articles/1067234/
- Edmundson, A., et al. "An Empirical Study on the Effectiveness of Security Code Review." ESSoS 2013. https://people.eecs.berkeley.edu/~daw/papers/coderev-essos13.pdf
- Firouzi, E., Ghafari, M. "Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection." arXiv:2602.05868, 2026.
- Fulton, K. R., Lewis, J., Malkin, N., Mazurek, M. L. "Write, Read, or Fix? Exploring Alternative Methods for Secure Development Studies." SOUPS 2024. https://www.usenix.org/conference/soups2024/presentation/fulton
- Hu, M., Zhang, Y. "The Python/C API: Evolution, Usage Statistics, and Bug Patterns." SANER 2020; JSEP 35(2), 2023.
- Kaczmarczyk, L. C., Petrick, E. R., East, J. P., Herman, G. L. "Identifying Student Misconceptions of Programming." SIGCSE 2010.
- Khalid, H., Thompson, R. E., Sabater, A., Mussiba, P., Fulton, K. R., Votipka, D. "(Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code." IEEE S&P 2027 (to appear). arXiv:2609.21020
- Lam, J., Fang, E., Almansoori, M., Chatterjee, R., Soosai Raj, A. G. "Identifying Gaps in the Secure Programming Knowledge and Skills of Students." SIGCSE 2022.
- Li, W., Li, L., Cai, H. "On the Vulnerability Proneness of Multilingual Code." ESEC/FSE 2022, pp. 847–859.
- Lichtinger, G., Hosseini Maasoum, S. M. "Generative AI as Seniority-Biased Technological Change: Evidence from U.S. Résumé and Job Posting Data." SSRN 5425555, 2025.
- MSET: "Evaluating the Effectiveness of Memory Safety Sanitizers." IEEE S&P 2025. doi:10.1109/SP61157.2025.00088
- Office of the National Cyber Director. "Back to the Building Blocks: A Path Toward Secure and Measurable Software." February 2024.
- Oh, S., Lee, K., Park, S., Kim, D., Kim, H. "Poisoned ChatGPT Finds Work for Idle Hands." IEEE S&P 2024. https://arxiv.org/abs/2312.06227
- Park, J., Lim, K., Park, S., Kim, D. "Supporting Students in Navigating LLM-Generated Insecure Code." arXiv:2511.20878, 2025.
- Perry, N., Srivastava, M., Kumar, D., Boneh, D. "Do Users Write More Insecure Code with AI Assistants?" ACM CCS 2023. doi:10.1145/3576915.3623157
- Prather, J., et al. "The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers." ICER 2024. https://arxiv.org/abs/2405.17739
- "Python Bindings for a Large C++ Robotics Library: The Case of OMPL." arXiv:2603.04668, 2026.
- Sandoval, G., Pearce, H., Nys, T., Karri, R., Garg, S., Dolan-Gavitt, B. "Lost at C: A User Study on the Security Implications of Large Language Model Code Assistants." USENIX Security 2023. https://www.usenix.org/conference/usenixsecurity23/presentation/sandoval
- Staicu, C.-A., et al. "Bilingual Problems." USENIX Security 2023.
- Tufano, R., Martin-Lopez, A., Tayeb, A., Dabić, O., Haiduc, S., Bavota, G. "Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?" ICSE 2025. https://arxiv.org/abs/2411.11401
- Votipka, D., Fulton, K. R., Parker, J., Hou, M., Mazurek, M. L., Hicks, M. "Understanding Security Mistakes Developers Make: Qualitative Analysis from Build It, Break It, Fix It." USENIX Security 2020.
- Yang, H., Cai, H. "A Comprehensive Study of Native Code Bugs in Python Applications." arXiv:2608.29851, 2026.
- Zi, Y., et al. "'I Would Have Written My Code Differently': Beginners Struggle to Understand LLM-Generated Code." FSE 2025. https://arxiv.org/abs/2504.19037
