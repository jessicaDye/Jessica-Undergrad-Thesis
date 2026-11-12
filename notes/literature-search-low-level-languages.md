# Literature Search: Computer Science Education and the Relevance of Low-Level / Foundational Programming Languages

**Question addressed:** In contemporary computer science education, what is the value of teaching low-level and foundational programming languages (C, assembly, and the Lisp/Scheme family) rather than teaching exclusively at higher levels of abstraction?

**Compiled:** 26 August 2026
**Papers:** 20 (17 open access, 3 paywalled — marked below)
**Date range:** 2022–2026, with the bulk from 2024–2026

---

## How to read this collection

The papers cluster into five arguments, which is also roughly how they divide up as evidence:

1. **Pointers and memory are the documented bottleneck** (Donyina, Petula, Guerzhoy, Bastian) — several independent groups treat C pointers as *the* hard concept in the curriculum and build interventions around it. The recurring premise is that the difficulty is worth pushing through, not designing around.
2. **Low-level work as a "notional machine"** (Nath, Abad, Vasconcelos) — the strongest pedagogical case for low-level languages is not the languages themselves but the concrete execution model they force students to build. Note that Abad and Vasconcelos make the *same* argument from the Lisp/functional side, which is why Lisp belongs in this question alongside C.
3. **What the curriculum should contain** (CS2023, Lee, Beale, Ebling, Siek) — the formal guidelines and the AI-era reform debate. The tension here is live and unresolved.
4. **Hardware and systems context** (Schoeberl, McDougall, Pasricha, Zhang) — courses where low-level competence is not optional.
5. **The memory-safety counter-current** (Siek, Rehman, Sharma) — the case that C's pedagogical role can be filled by Rust, plus evidence on where that substitution is and isn't yet practical.

**A caveat worth carrying into the thesis:** almost none of this literature is a controlled test of the actual question. There is a great deal on *how to teach* low-level material and very little on *whether learning it* measurably improves outcomes elsewhere. Nath (2024) is the closest to a direct transfer claim, and it rests on survey data from a single institution. If the thesis wants an empirical answer rather than a synthesis of positions, that gap is itself the finding.

---

## Summary table

| # | File | Title | First author | Venue | Year |
|---|------|-------|--------------|-------|------|
| 1 | `Abad2024.pdf` | Beyond SICP — Design and Implementation of a Notional Machine for Scheme | Abad | arXiv preprint (cs.PL) | 2024 |
| 2 | `Bastian2025.pdf` 🔒 | Misconceptions in Programming: Intuitive Reasoning and Tracing Task Performance Across Experience Levels | Bastian | ACM ICER | 2025 |
| 3 | `Beale2025.pdf` | Computer Science Education in the Age of Generative AI | Beale | arXiv preprint (cs.CY) | 2025 |
| 4 | `Donyina2025.pdf` | Pedagogy of Teaching Pointers in the C Programming Language using Graph Transformations | Donyina | arXiv preprint (cs.SE) | 2025 |
| 5 | `Ebling2024.pdf` 🔒 | Resources for Teaching Operating Systems: A Survey of Instructors and a Literature Review | Ebling | ACM Trans. Computing Education | 2024 |
| 6 | `Guerzhoy2025.pdf` 🔒 | Getting Used to Pointers with Pointer Drills | Guerzhoy | ACM ITiCSE | 2025 |
| 7 | `Kumar2024.pdf` | Computer Science Curricula 2023 (CS2023) — Final Report | Kumar (Joint Task Force) | ACM / IEEE-CS / AAAI | 2024 |
| 8 | `Lee2026.pdf` | Reshaping Undergraduate Computer Science Education in the Generative AI Era | Lee | arXiv preprint (workshop report) | 2026 |
| 9 | `Lokkila2023.pdf` | A Data-Driven Approach to Compare the Syntactic Difficulty of Programming Languages | Lokkila | Journal of Information Systems Education | 2023 |
| 10 | `McDougall2025.pdf` | Pedagogically Motivated and Composable Open-Source RISC-V Processors for Computer Science Education | McDougall | arXiv preprint (cs.AR) | 2025 |
| 11 | `Nath2024.pdf` | Enhancing High-Level Language Concept Comprehension through a Notional Machine Approach of Assembly Language Education | Nath | ASEE Annual Conference | 2024 |
| 12 | `Pasricha2022.pdf` | Embedded Systems Education in the 2020s: Challenges, Reflections, and Future Directions | Pasricha | arXiv preprint (cs.CY) | 2022 |
| 13 | `Petula2025.pdf` | DeliverC: Teaching Pointers through GenAI-Powered Game-Based Learning | Petula | arXiv preprint (cs.CY) | 2025 |
| 14 | `Rehman2025.pdf` | Not-So-Bitter Pill to Swallow: Slipstreaming Memory Safe Programming via Rust as part of a Database Systems Course | Rehman | ACM DataEd Workshop | 2025 |
| 15 | `Schoeberl2025.pdf` | Wildcat: Educational RISC-V Microprocessors | Schoeberl | arXiv preprint (cs.AR) | 2025 |
| 16 | `Sharma2024.pdf` | Rust for Embedded Systems: Current State, Challenges and Open Problems | Sharma | ACM CCS (extended report on arXiv) | 2024 |
| 17 | `Siek2025.pdf` | An Undergraduate Computer Systems Curriculum Using Rust | Siek | MS thesis, Virginia Tech | 2025 |
| 18 | `Vasconcelos2025.pdf` | Teaching Introductory Functional Programming Using Haskelite | Vasconcelos | TFPiE / EPTCS 424 | 2025 |
| 19 | `Zhang2025.pdf` | SortingHat: Redefining Operating Systems Education with a Tailored Digital Teaching Assistant | Zhang | ACM Web Conference Companion | 2025 |
| 20 | `Zi2025.pdf` | "I Would Have Written My Code Differently": Beginners Struggle to Understand LLM-Generated Code | Zi | ACM FSE | 2025 |

🔒 = paywalled; no open-access copy located. See "Access notes" at the end.

---

## Detailed entries

### 1. Beyond SICP — Design and Implementation of a Notional Machine for Scheme
- **Primary author:** Kyriel Mortel Abad (with Martin Henz), National University of Singapore
- **Venue / year:** arXiv preprint 2412.01545, December 2024
- **Link:** https://arxiv.org/abs/2412.01545

**Primary findings.** The authors extend the environment model of *Structure and Interpretation of Computer Programs* into a full "notional machine" — the CSE machine — covering the whole of SICP Scheme rather than the fragment SICP itself formalises. They show that `call/cc`, normally treated as an advanced topic, falls out of the model naturally and so becomes teachable to beginners. The machine drives computer-generated visualisations of program state and underpins a web-based Scheme implementation in development at NUS.

**Relevance.** This is the core citation for why *Lisp* belongs in a question otherwise about low-level languages. The argument is not that Scheme is close to the machine but that it is small enough to have a fully specified execution model students can hold in their heads — the same pedagogical goal that C's proximity to memory is meant to serve, reached from the opposite direction. Useful for arguing that "low-level" in CS education means *explicit about mechanism*, not *near the hardware*.

---

### 2. Misconceptions in Programming: Intuitive Reasoning and Tracing Task Performance Across Experience Levels 🔒
- **Primary author:** Morten Bastian (with Andreas Mühling), Kiel University
- **Venue / year:** Proceedings of the 2025 ACM Conference on International Computing Education Research (ICER) V.1, 2025
- **Link:** https://dl.acm.org/doi/10.1145/3702652.3744209

**Primary findings.** Examines programming misconceptions as products of intuitive reasoning rather than simple knowledge gaps, and measures how tracing-task performance varies across experience levels. The persistence of misconceptions among more experienced students is the notable result: exposure alone does not dislodge intuitive but wrong models of execution.

**Relevance.** Supplies the mechanism-level argument that explicit instruction in how execution actually works is necessary, because students' default intuitions are wrong and stay wrong. Tracing — following program state step by step — is exactly the skill low-level languages force. Pair with Nath (2024) and Abad (2024).

---

### 3. Computer Science Education in the Age of Generative AI
- **Primary author:** Russell Beale, University of Birmingham
- **Venue / year:** arXiv preprint 2507.02183, July 2025
- **Link:** https://arxiv.org/abs/2507.02183

**Primary findings.** Surveys how LLM code generation is reshaping programming instruction — opportunities in coding assistance and assessment, risks in academic integrity and over-reliance. Concludes with policy recommendations, and directly poses the question of *what* CS educators should now teach when code production is cheap.

**Relevance.** The "what should we still teach" framing is the pivot on which the low-level question now turns. If AI writes the code, the remaining human skill is verification and understanding of what the code does at the machine level — an argument that raises rather than lowers the value of foundational language work. Beale states the problem; he does not settle it.

---

### 4. Pedagogy of Teaching Pointers in the C Programming Language using Graph Transformations
- **Primary author:** Adwoa Donyina (with Reiko Heckel), University of Leicester
- **Venue / year:** arXiv preprint 2503.20469, March 2025
- **Link:** https://arxiv.org/abs/2503.20469

**Primary findings.** Proposes teaching C pointers through graph transformation systems that visually simulate pointer manipulation, using the GROOVE tool to model and animate dynamic pointer structures. Includes an evaluation study and a comparison against other pointer-teaching methods. The framing premise, stated plainly: in an introduction to C, pointers are the topic students find most difficult.

**Relevance.** Direct evidence for both halves of the thesis question — that low-level material is genuinely hard, and that the field's response is to build better scaffolding rather than to remove it from the curriculum. The visual-learner angle also gives a concrete pedagogical recommendation to cite.

---

### 5. Resources for Teaching Operating Systems: A Survey of Instructors and a Literature Review 🔒
- **Primary author:** Maria R. Ebling
- **Venue / year:** ACM Transactions on Computing Education, 2024
- **Link:** https://dl.acm.org/doi/10.1145/3688853

**Primary findings.** Combines a survey of OS instructors (pedagogy, textbooks, software platforms) with a review of 51 papers spanning two decades of OS education research. Finds instructors balanced but slightly favouring "internal" (implementation-level) perspectives, while the research literature shows overwhelming support for internal, concrete approaches. Core topics receiving sustained attention: processes, concurrency, scheduling, virtual memory, file systems.

**Relevance.** A rare systematic look at what an entire systems-course community actually does. The gap between what instructors practise and what researchers advocate is a usable finding: the research consensus favours the concrete, hands-on, close-to-the-machine approach more strongly than teaching practice does.

---

### 6. Getting Used to Pointers with Pointer Drills 🔒
- **Primary author:** Michael Guerzhoy, University of Toronto (Division of Engineering Science)
- **Venue / year:** Proceedings of the 30th ACM ITiCSE V.2, 2025
- **Link:** https://dl.acm.org/doi/10.1145/3724389.3731268

**Primary findings.** Reports a drill-based approach to pointer fluency — repeated short exercises rather than extended projects — on the premise that pointer competence is a matter of practised familiarity, not conceptual insight alone.

**Relevance.** A useful methodological contrast with Donyina (visualisation) and Petula (game-based scaffolding): three 2025 papers, three different interventions, one shared assumption that pointers must be taught rather than avoided. That convergence is itself an argument.

---

### 7. Computer Science Curricula 2023 (CS2023) — Final Report
- **Primary author:** ACM/IEEE-CS/AAAI Joint Task Force (co-chairs Amruth N. Kumar and Rajendra K. Raj)
- **Venue / year:** ACM / IEEE Computer Society / AAAI, January 2024
- **Link:** https://ieeecs-media.computer.org/media/education/reports/CS2023.pdf (open access)

**Primary findings.** The current international curriculum guidelines for undergraduate CS, superseding CS2013. Defines knowledge areas including Systems Fundamentals, Architecture and Organization, Operating Systems, and Programming Languages, with competency specifications for each.

**Relevance.** The authoritative statement of what the field says a CS graduate should know. Any thesis claim about whether low-level material belongs in the curriculum should be anchored against what CS2023 actually requires versus what programs actually deliver. Treat this as a primary source, not a research finding.

---

### 8. Reshaping Undergraduate Computer Science Education in the Generative AI Era
- **Primary author:** Yi-Chieh Lee, and 22 co-authors (NUS–Google Workshops, Singapore)
- **Venue / year:** arXiv preprint 2606.07545, submitted May 2026, revised June 2026
- **Link:** https://arxiv.org/abs/2606.07545

**Primary findings.** A large multi-institution workshop report arguing that generative AI requires fundamental curricular change. Contends that traditional emphases on implementation-level programming, debugging, testing and software design are becoming outdated as AI automates them, and proposes curricula centred on understanding and verifying AI-generated artifacts, system design, abstraction and critical evaluation. Five reform priorities, one of which is explicitly "re-centering foundational knowledge."

**Relevance.** The single most important paper here for the *against* case — and note that it partially argues both ways. "Implementation-level programming is becoming outdated" is a direct challenge to the value of C; "re-centering foundational knowledge" pulls the other way. The internal tension in a 23-author consensus document is worth quoting directly rather than paraphrasing.

---

### 9. A Data-Driven Approach to Compare the Syntactic Difficulty of Programming Languages
- **Primary author:** Erno Lokkila (with Athanasios Christopoulos, Mikko-Jussi Laakso), University of Turku
- **Venue / year:** Journal of Information Systems Education, 34(1), 84–93, Winter 2023
- **Link:** https://jise.org/volume34/n1/JISE2023v34n1pp84-93.pdf (open access)

**Primary findings.** Analyses 219,454 code submissions from 715 first-year students across 259 exercises, categorising error patterns via a transition probability matrix, to compare Python and Java as first languages. Concludes Python is easier to grasp and recommends it as the introductory steppingstone.

**Relevance.** The best-evidenced *counter*-argument in the collection, and the largest dataset. If syntactic difficulty measurably impedes beginners with Java, the case against starting in C is stronger still. The honest use of this paper is as the opposing position — and its limit is that it measures early-course error rates, not eventual depth of understanding, which is precisely what low-level advocates claim to be buying.

---

### 10. Pedagogically Motivated and Composable Open-Source RISC-V Processors for Computer Science Education
- **Primary author:** Ian McDougall (with Michael Davies, Harish Batchu, Karthikeyan Sankaralingam), University of Wisconsin–Madison / NVIDIA Research
- **Venue / year:** arXiv preprint 2509.20514, September 2025
- **Link:** https://arxiv.org/abs/2509.20514

**Primary findings.** Proposes criteria for evaluating RISC-V implementations for teaching, analyses existing open-source designs against them, and presents WISCV, a composable framework instructors can customise per course. Includes student feedback results.

**Relevance.** Evidence that the open ISA has removed a practical barrier to teaching at the hardware level. Supports the argument that low-level instruction is becoming *more* feasible, not less, even as high-level tooling improves.

---

### 11. Enhancing High-Level Language Concept Comprehension through a Notional Machine Approach of Assembly Language Education
- **Primary author:** Sagnik Nath, University of California, Santa Cruz
- **Venue / year:** 2024 ASEE Annual Conference & Exposition
- **Link:** https://nemo.asee.org/public/conferences/344/papers/41059/view (open access)

**Primary findings.** Redesigns lab exercises in UCSC's Computer Systems and Organization course, using the RARS emulator as a notional machine bridging high-level abstractions and low-level implementation. Making assembly exercises analogous to high-level scenarios improved students' machine-architecture comprehension and their preparation for later coursework; survey data support the approach.

**Relevance.** **This is the closest paper in the collection to a direct answer to the thesis question** — it claims that assembly instruction improves comprehension of *high-level* language concepts, i.e. genuine transfer. Weight it accordingly, but note the limits: single institution, survey-based evidence, no control group. If the thesis needs a stronger transfer claim than this, the literature may not currently supply one.

---

### 12. Embedded Systems Education in the 2020s: Challenges, Reflections, and Future Directions
- **Primary author:** Sudeep Pasricha, Colorado State University
- **Venue / year:** arXiv preprint 2206.03263, 2022
- **Link:** https://arxiv.org/abs/2206.03263

**Primary findings.** Traces two decades of embedded systems education and the challenges facing curriculum designers in the 2020s, drawing on the author's decade-plus of teaching. Argues the need to train designers with skills spanning hardware, software and their co-design remains pressing, and identifies strategies and future directions.

**Relevance.** Establishes a domain where low-level competence is non-negotiable, and provides the "industry still needs this" argument with a named, credible source. The oldest paper in the set — include it for the longitudinal framing, and lean on newer sources for current claims.

---

### 13. DeliverC: Teaching Pointers through GenAI-Powered Game-Based Learning
- **Primary author:** Wyatt Petula (with Anushcka Joshi, Peggy Tu, Amrutha Somasundar, Suman Saha), Penn State
- **Venue / year:** arXiv preprint 2509.14496, September 2025
- **Link:** https://arxiv.org/abs/2509.14496

**Primary findings.** A game integrating GPT-4-mini to generate pointer challenges and personalised hints on the fly. Pilot with 25 undergraduates using gameplay data and a 15-item survey: most students reported greater confidence and reflection, and error rates fell across scaffolded levels. Participation dropped as difficulty rose, and some students found the AI feedback vague.

**Relevance.** Shows the two threads of this literature converging — AI tooling deployed *in service of* teaching low-level concepts rather than replacing them. The negative results matter as much as the positive: engagement fell exactly where the material got hard, which is the perennial problem with C. Small n, pilot study; treat as suggestive.

---

### 14. Not-So-Bitter Pill to Swallow: Slipstreaming Memory Safe Programming via Rust as part of a Database Systems Course
- **Primary author:** Mohammed Suhail Rehman (with Aaron Elmore, Raul Castro Fernandez), University of Chicago
- **Venue / year:** 4th International Workshop on Data Systems Education (DataEd), 2025
- **Link:** https://knowledge.uchicago.edu/record/16004/files/Not-So-Bitter-Pill-to-Swallow.pdf (open access)

**Primary findings.** Reports introducing Rust as the implementation language for a database systems course, "slipstreaming" memory-safe systems programming into a course whose primary subject is something else, and documents how students fared.

**Relevance.** A concrete instance of the substitution argument: students get systems-level, memory-aware programming without C. Read against Siek (2025), which attempts the same substitution at whole-curriculum scale.

---

### 15. Wildcat: Educational RISC-V Microprocessors
- **Primary author:** Martin Schoeberl, Technical University of Denmark
- **Venue / year:** arXiv preprint 2502.20197, February 2025
- **Link:** https://arxiv.org/abs/2502.20197

**Primary findings.** Argues that the conventional five-stage pipeline is the wrong teaching vehicle and that a 3-stage organisation is more adequate for teaching pipelining. Demonstrates, counter-intuitively, that 4- and 5-stage pipelines can yield *lower* maximum clock frequency than the 3-stage design, because forwarding multiplexers land on the critical path.

**Relevance.** Peripheral to the language question but valuable as an example of pedagogical simplification done rigorously: the teaching model is chosen for explanatory power and turns out to be defensible on engineering grounds too. Cite if the thesis addresses how much machine detail to expose.

---

### 16. Rust for Embedded Systems: Current State, Challenges and Open Problems
- **Primary author:** Ayushi Sharma (with Shashank Sharma, Sai Ritvik Tanksalkar, Santiago Torres-Arias, Aravind Machiry), Purdue University
- **Venue / year:** ACM CCS 2024; extended report arXiv 2311.05063
- **Link:** https://arxiv.org/abs/2311.05063

**Primary findings.** Empirical study of 2,836 Rust embedded projects, 5 static-analysis tools, and 225 developers. Identifies insufficient tooling support for Rust in embedded contexts, static-analysis failures on Rust-specific constructs, and difficulty writing interoperable code because of the type system's sophistication.

**Relevance.** Not an education paper, and should be labelled as such — but it is the evidence that the "teach Rust instead of C" substitution is not yet complete in practice. C interoperability remains a working requirement in embedded development, which bears directly on whether graduates can skip C.

---

### 17. An Undergraduate Computer Systems Curriculum Using Rust
- **Primary author:** Kieran Rong Chen Siek, Virginia Tech
- **Venue / year:** MS thesis, Virginia Tech, October 2025
- **Link:** https://vtechworks.lib.vt.edu/items/92c15f1f-32c6-4822-b9fe-64f2a62358c1 (open access)

**Primary findings.** Designs and evaluates a systems curriculum taught in Rust rather than the traditional C, documenting integration challenges and pedagogical strategies. Over a single semester at Virginia Tech, students completed systems-level Rust projects and reported improved understanding of the associated systems theory; ownership and borrowing rules required additional instruction time.

**Relevance.** The most direct test available of whether C is *necessary* for systems education or merely conventional. Note what the finding actually supports: Rust can carry systems concepts, at the cost of teaching ownership. It does not show students understood memory *better* than a C cohort — there is no comparison group. A careful thesis should say so.

---

### 18. Teaching Introductory Functional Programming Using Haskelite
- **Primary author:** Pedro Vasconcelos, University of Porto
- **Venue / year:** Trends in Functional Programming in Education (TFPiE) 2025; EPTCS 424, pp. 49–66
- **Link:** https://arxiv.org/abs/2508.03640 (open access)

**Primary findings.** Reports classroom use of a step-by-step tracing interpreter for a Haskell subset, motivated by students' difficulty applying substitution to unfamiliar contexts such as recursion and higher-order functions. Documents student feedback, instructional outcomes, and development recommendations.

**Relevance.** The functional-side companion to Abad (2024) and the direct parallel to the C-side visualisation work of Donyina and Petula. Same intervention shape — make execution visible step by step — arrived at independently in a different language family. Good evidence that the pedagogical problem is about *models of execution*, not about any particular language being low-level.

---

### 19. SortingHat: Redefining Operating Systems Education with a Tailored Digital Teaching Assistant
- **Primary author:** Yifan Zhang (with Xinkui Zhao, Zuxin Wang, Zhengyi Zhou, Guanjie Cheng, Shuiguang Deng, Jianwei Yin), Zhejiang University
- **Venue / year:** Companion Proceedings of the ACM Web Conference 2025; arXiv 2606.00015
- **Link:** https://arxiv.org/abs/2606.00015

**Primary findings.** Presents an LLM-based teaching assistant tailored to operating systems coursework, addressing the gap between generic AI assistants and the specific demands of systems material.

**Relevance.** Evidence that systems courses — where C and kernel-level work live — are receiving purpose-built AI support rather than being displaced by it. Supporting, not central; use it alongside Ebling (2024) on the state of OS teaching.

---

### 20. "I Would Have Written My Code Differently": Beginners Struggle to Understand LLM-Generated Code
- **Primary author:** Yangtian Zi (with Luisa Li, Arjun Guha, Carolyn Anderson, Molly Q Feldman), Northeastern University / Wellesley / Oberlin
- **Venue / year:** Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering (FSE), 2025
- **Link:** https://arxiv.org/abs/2504.19037

**Primary findings.** Studies how beginning programmers comprehend LLM-generated code, finding they struggle to understand code they did not write themselves — with the difficulty tied to unfamiliar constructs and idioms rather than to code quality.

**Relevance.** The empirical hinge of the AI-era argument. If students cannot read code they did not write, then the ability to reason about what code actually does becomes the scarce skill — which is the strongest available modern justification for teaching at the level where mechanism is explicit. This paper does not itself make that argument; the thesis can.

---

## Access notes

17 of the 20 are open access and are fetched by `download_papers.sh` in this folder.

Three are behind the ACM Digital Library paywall and are **not** downloaded by the script:

- `Bastian2025` — https://dl.acm.org/doi/10.1145/3702652.3744209
- `Ebling2024` — https://dl.acm.org/doi/10.1145/3688853
- `Guerzhoy2025` — https://dl.acm.org/doi/10.1145/3724389.3731268

All three should be reachable through an institutional ACM subscription; if there is an ACM Open agreement in place they may open directly. Guerzhoy posts preprints at the University of Toronto, so an author copy may exist.

## Verification note

Bibliographic details were confirmed against Crossref, arXiv, or the publisher record rather than search-result snippets. Two items warrant a second look before citing:

- **Kumar2024** — CS2023 is a task-force report, not a single-author paper. It is filed under the co-chair's name for consistency with the naming scheme; cite it as *ACM/IEEE-CS/AAAI Joint Task Force on Computer Science Curricula*.
- **Zhang2025** and **Lee2026** — both carry 2026 arXiv identifiers while the underlying venues are 2025 and 2026 respectively. Filenames follow the venue year. Check the version you cite.
