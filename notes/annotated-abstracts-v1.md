# Assembly Required?

## Annotated abstract collection: the relevance of low\-level languages in software engineering practice and computer science education

*Compiled 26 August 2026 · 17 papers · 2017–2025*

* * *

## Scope and method

**Thesis question.** What is the relevance of low\-level programming languages — C, C\+\+, Assembly, FORTRAN — in the contemporary software engineering industry and in computer science education, given that these are the languages in which AI tooling and the major Python libraries are actually written?

**Selection criteria.** Peer\-reviewed papers in reputable venues (Science, *Communications of the ACM*, ACM TOSEM, ACM TOCE, *Empirical Software Engineering*, *IEEE Software*, USENIX Security, SIGCSE/ITiCSE, ASEE, SLE, ICSME, *SN Computer Science*), published 2017–2025, weighted roughly evenly between industry evidence and education research. Two arXiv preprints from national\-lab and university groups are included where no peer\-reviewed equivalent exists on that specific question; both are flagged.

**Abstracts below are reproduced verbatim** from the publisher or author\-deposited copy. Every entry carries a DOI or stable link so you can pull the full text through the Niagara library.

* * *

## Part A — Industry and software engineering practice

### A1. There's plenty of room at the Top: What will drive computer performance after Moore's law?

Charles E. Leiserson, Neil C. Thompson, Joel S. Emer, Bradley C. Kuszmaul, Butler W. Lampson, Daniel Sanchez, Tao B. Schardl · **Science**, vol. 368, issue 6495, eaam9744 (2020) · DOI: [10\.1126/science.aam9744](https://doi.org/10.1126/science.aam9744)

> The miniaturization of semiconductor transistors has driven the growth in computer performance for more than 50 years. As miniaturization approaches its limits, bringing an end to Moore's law, performance gains will need to come from software, algorithms, and hardware. We refer to these technologies as the "Top" of the computing stack to distinguish them from the traditional technologies at the "Bottom": semiconductor physics and silicon\-fabrication technology. In the post\-Moore era, the Top will provide substantial performance gains, but these gains will be opportunistic, uneven, and sporadic, and they will suffer from the law of diminishing returns. Big system components offer a promising context for tackling the challenges of working at the Top.

**Why it matters.** The anchor citation for the whole thesis. Leiserson et al. argue that future performance must come from software rather than hardware, and their worked example — a matrix\-multiply rewritten from Python into tuned C, gaining roughly four orders of magnitude — is the single most quotable piece of evidence that low\-level competence has economic value.

* * *

### A2. Energy efficiency across programming languages: how do energy, time, and memory relate?

Rui Pereira, Marco Couto, Francisco Ribeiro, Rui Rua, Jácome Cunha, João Paulo Fernandes, João Saraiva · **SLE 2017** (10th ACM SIGPLAN International Conference on Software Language Engineering) · DOI: [10\.1145/3136014.3136031](https://doi.org/10.1145/3136014.3136031)

> This paper presents a study of the runtime, memory usage and energy consumption of twenty seven well\-known software languages. We monitor the performance of such languages using ten different programming problems, expressed in each of the languages. Our results show interesting findings, such as, slower/faster languages consuming less/more energy, and how memory usage influences energy consumption. We show how to use our results to provide software engineers support to decide which language to use when energy efficiency is a concern.

**Why it matters.** The most\-cited empirical ranking placing C at the top for both speed and energy and Python far down it. Useful as the sustainability argument for low\-level languages — and worth treating critically, since the benchmark methodology has been contested.

* * *

### A3. An Empirical Study on the Performance and Energy Usage of Compiled Python Code

Vincenzo Stoico, Andrei Calin Dragomir, Patricia Lago · **arXiv preprint** arXiv:2505.02346 (2025), Vrije Universiteit Amsterdam · DOI: [10\.48550/arXiv.2505.02346](https://doi.org/10.48550/arXiv.2505.02346)

> Python is a popular programming language known for its ease of learning and extensive libraries. However, concerns about performance and energy consumption have led to the development of compilers to enhance Python code efficiency. Despite the proven benefits of existing compilers on the efficiency of Python code, there is limited analysis comparing their performance and energy efficiency, particularly considering code characteristics and factors like CPU frequency and core count. Our study investigates how compilation impacts the performance and energy consumption of Python code, using seven benchmarks compiled with eight different tools: PyPy, Numba, Nuitka, Mypyc, Codon, Cython, Pyston\-lite, and the experimental Python 3.13 version, compared to CPython. The benchmarks are single\-threaded and executed on an NUC and a server, measuring energy usage, execution time, memory usage, and Last\-Level Cache (LLC) miss rates at a fixed frequency and on a single core. The results show that compilation can significantly enhance execution time, energy and memory usage, with Codon, PyPy, and Numba achieving over 90% speed and energy improvements. Nuitka optimizes memory usage consistently on both testbeds. The impact of compilation on LLC miss rate is not clear since it varies considerably across benchmarks for each compiler. Our study is important for researchers and practitioners focused on improving Python code performance and energy efficiency. We outline future research directions, such as exploring caching effects on energy usage. Our findings help practitioners choose the best compiler based on their efficiency benefits and accessibility.

**Why it matters.** Direct evidence for the mechanism at the heart of your question: Python's usable performance comes from compilation and native code underneath, not from Python itself. *Preprint — verify peer\-review status before citing as settled.*

* * *

### A4. Bilingual Problems: Studying the Security Risks Incurred by Native Extensions in Scripting Languages

Cristian\-Alexandru Staicu (CISPA), Sazzadur Rahaman (University of Arizona), Ágnes Kiss (CISPA), Michael Backes (CISPA) · **32nd USENIX Security Symposium (USENIX Security '23)**, August 2023 · [usenix.org/conference/usenixsecurity23/presentation/staicu](https://www.usenix.org/conference/usenixsecurity23/presentation/staicu)

> Scripting languages are continuously gaining popularity due to their ease of use and the flourishing software ecosystems surrounding them. These languages offer crash and memory safety by design. Thus, developers do not need to understand and prevent low\-level security issues like the ones plaguing the C code. However, scripting languages often allow native extensions, a way for custom C/C\+\+ code to be invoked directly from the high\-level language. While this feature promises several benefits, such as increased performance or the reuse of legacy code, it can also break the language's guarantees, e.g., crash safety. In this work, we first provide a comparative analysis of the security risks of native extension APIs in three popular scripting languages. Additionally, we discuss a novel methodology for studying the misuse of the native extension API. We then perform an in\-depth study of npm, an ecosystem that is most exposed to threats introduced by native extensions. We show that vulnerabilities in extensions can be exploited in their embedding library by producing reads of uninitialized memory, hard crashes, or memory leaks in 33 npm packages simply by invoking their API with well\-crafted inputs. Moreover, we identify six open\-source web applications in which a weak adversary can deploy such exploits remotely. Finally, we were assigned seven security advisories for the work presented in this paper, most labeled as high severity.

**Why it matters.** The strongest security\-side argument in the collection. The memory\-safety guarantees a Python or JavaScript developer relies on are void at the C boundary — which is exactly where the numeric and ML stack lives. A developer who cannot read C cannot audit that boundary.

* * *

### A5. Bridging the Language Gap: An Empirical Study of Bindings for Open Source Machine Learning Libraries Across Software Package Ecosystems

Hao Li, Cor\-Paul Bezemer · **Empirical Software Engineering** (2024) · DOI: [10\.1007/s10664\-024\-10570\-5](https://doi.org/10.1007/s10664-024-10570-5)

> Open source machine learning (ML) libraries enable developers to integrate advanced ML functionality into their own applications. However, popular ML libraries, such as TensorFlow, are not available natively in all programming languages and software package ecosystems. Hence, developers who wish to use an ML library which is not available in their programming language or ecosystem of choice, may need to resort to using a so\-called binding library (or binding). Bindings provide support across programming languages and package ecosystems for reusing a host library. For example, the Keras .NET binding provides support for the Keras library in the NuGet (.NET) ecosystem even though the Keras library was written in Python. In this paper, we collect 2,436 cross\-ecosystem bindings for 546 ML libraries across 13 software package ecosystems by using an approach called BindFind, which can automatically identify bindings and link them to their host libraries. Furthermore, we conduct an in\-depth study of 133 cross\-ecosystem bindings and their development for 40 popular open source ML libraries. Our findings reveal that the majority of ML library bindings are maintained by the community, with npm being the most popular ecosystem for these bindings. Our study also indicates that most bindings cover only a limited range of the host library's releases, often experience considerable delays in supporting new releases, and have widespread technical lag.

**Why it matters.** Quantifies the layer that your thesis is about — the glue between a high\-level surface language and a native implementation — and shows it is under\-maintained and lagging. Evidence that cross\-language competence is a real and scarce industrial skill.

* * *

### A6. Studying the Impact of TensorFlow and PyTorch Bindings on Machine Learning Software Quality

Hao Li, Gopi Krishnan Rajbahadur, Cor\-Paul Bezemer · **ACM Transactions on Software Engineering and Methodology (TOSEM)**, vol. 33, no. 7 (2024) · DOI: [10\.1145/3678168](https://doi.org/10.1145/3678168)

> Bindings for machine learning frameworks (such as TensorFlow and PyTorch) allow developers to integrate a framework's functionality using a programming language different from the framework's default language (usually Python). In this paper, we study the impact of using TensorFlow and PyTorch bindings in C\#, Rust, Python and JavaScript on the software quality in terms of correctness (training and test accuracy) and time cost (training and inference time) when training and performing inference on five widely used deep learning models. Our experiments show that a model can be trained in one binding and used for inference in another binding for the same framework without losing accuracy. Our study is the first to show that using a non\-default binding can help improve machine learning software quality from the time cost perspective compared to the default Python binding while still achieving the same level of correctness.

**Why it matters.** Measures what leaving Python actually buys you in a production ML pipeline. A rare quantitative result on the cost side of the "just use Python" default.

* * *

### A7. Toward Understanding Deep Learning Framework Bugs

Junjie Chen, Yihua Liang, Qingchao Shen, Jiajun Jiang, Shuochuan Li · **ACM Transactions on Software Engineering and Methodology (TOSEM)**, vol. 32, no. 6 (2023) · DOI: [10\.1145/3587155](https://doi.org/10.1145/3587155)

> DL frameworks are the basis of constructing all DL programs and models, and thus their bugs could lead to the unexpected behaviors of any DL program or model relying on them. Such a wide effect demonstrates the necessity and importance of guaranteeing DL frameworks' quality. Understanding the characteristics of DL framework bugs is a fundamental step for this quality assurance task, facilitating designing effective bug detection and debugging approaches. Hence, in this work we conduct the most large\-scale study on 1,000 bugs from four popular and diverse DL frameworks (i.e., TensorFlow, PyTorch, MXNet, and DL4J). By analyzing the root causes and symptoms of DL framework bugs associated with 5 components decomposed from DL frameworks, as well as measuring test coverage achieved by three state\-of\-the\-art testing techniques, we obtain 12 major findings for the comprehensive understanding of DL framework bugs and the current status of existing DL framework testing practice, and then provide a series of actionable guidelines for better DL framework bug detection and debugging. Finally, based on the guidelines, we design and implement a prototype DL\-framework testing tool, called TenFuzz, which is evaluated to be effective and finds 3 unknown bugs on the latest TensorFlow framework in a preliminary study, indicating the significance of our guidelines.

**Why it matters.** A 1,000\-bug study of the C\+\+/CUDA machinery under the AI stack. Establishes both that these frameworks are buggy at the native layer and that fixing them requires people who work at that layer.

* * *

### A8. An Empirical Study on Bugs Inside PyTorch: A Replication Study

Sharon Chee Yin Ho, Vahid Majdinasab, Mohayeminul Islam, Diego Elias Costa, Emad Shihab, Foutse Khomh, Sarah Nadi, Muhammad Raza · **ICSME 2023** (IEEE International Conference on Software Maintenance and Evolution) · [ieeexplore.ieee.org/document/10336350](https://ieeexplore.ieee.org/document/10336350) · preprint [arXiv:2307.13777](https://arxiv.org/abs/2307.13777)

> Software systems are increasingly relying on deep learning components, due to their remarkable capability of identifying complex data patterns and powering intelligent behaviour. A core enabler of this change in software development is the availability of easy\-to\-use deep learning libraries. Libraries like PyTorch and TensorFlow empower a large variety of intelligent systems, offering a multitude of algorithms and configuration options, applicable to numerous domains of systems. However, bugs in those popular deep learning libraries also may have dire consequences for the quality of systems they enable; thus, it is important to understand how bugs are identified and fixed in those libraries. Inspired by a study of Jia et al., which investigates the bug identification and fixing process at TensorFlow, we characterize bugs in the PyTorch library, a very popular deep learning framework. We investigate the causes and symptoms of bugs identified during PyTorch's development, and assess their locality within the project, and extract patterns of bug fixes. Our results highlight that PyTorch bugs are more like traditional software projects bugs, than related to deep learning characteristics. Finally, we also compare our results with the study on TensorFlow, highlighting similarities and differences across the bug identification and fixing process.

**Why it matters.** The finding that PyTorch's bugs look like *ordinary systems\-software bugs* rather than ML\-specific ones is a gift to your argument: maintaining AI infrastructure is conventional low\-level software engineering.

* * *

### A9. Silent bugs in deep learning frameworks: an empirical study of Keras and TensorFlow

Florian Tambon, Amin Nikanjam, Le An, Foutse Khomh, Giuliano Antoniol · **Empirical Software Engineering**, vol. 29 (2024) · DOI: [10\.1007/s10664\-023\-10389\-6](https://doi.org/10.1007/s10664-023-10389-6)

> Deep Learning (DL) frameworks are now widely used, simplifying the creation of complex models as well as their integration into various applications even among non\-DL experts. However, like any other programs, they are prone to bugs. This paper deals with the subcategory of bugs named silent bugs: they lead to wrong behavior but they do not cause system crashes or hangs, nor show an error message to the user. Such bugs are even more dangerous in DL applications and frameworks due to the "black\-box" and stochastic nature of the DL systems (i.e., the end user can not understand how the model makes decisions). This paper presents the first empirical study of the silent bugs in Tensorflow, specifically its high\-level API Keras, and their impact on users' programs. We extracted closed issues related to Keras API from the TensorFlow GitHub repository. Out of the 1,168 issues that we gathered, 77 were reproducible silent bugs affecting users' programs. We categorized the bugs based on the effects on the users' programs and the components where the issues occurred, using information from the issue reports. We then derived a threat level for each of the issues, based on the impact they had on the users' programs. To assess the relevance of identified categories and the impact scale, we conducted an online survey with 103 DL developers. The participants generally agreed with the significant impact of silent bugs in DL frameworks and how they impact users and acknowledged our findings.

**Why it matters.** "Simplifying... even among non\-DL experts" is the abstraction bargain your thesis interrogates. Silent bugs are the failure mode that only surfaces for someone willing to look beneath the API.

* * *

### A10. Memory\-Safety Challenge Considered Solved? An In\-Depth Study with All Rust CVEs

Hui Xu, Zhuangbin Chen, Mingshen Sun, Yangfan Zhou, Michael R. Lyu · **ACM Transactions on Software Engineering and Methodology (TOSEM)**, vol. 31, no. 1 (2021) · DOI: [10\.1145/3466642](https://doi.org/10.1145/3466642)

> Rust is an emerging programing language that aims at preventing memory\-safety bugs without sacrificing much efficiency. The claimed property is very attractive to developers, and many projects start using the language. However, can Rust achieve the memory\-safety promise? This paper studies the question by surveying 186 real\-world bug reports collected from several origins which contain all existing Rust CVEs (common vulnerability and exposures) of memory\-safety issues by 2020\-12\-31. We manually analyze each bug and extract their culprit patterns. Our analysis result shows that Rust can keep its promise that all memory\-safety bugs require unsafe code, and many memory\-safety bugs in our dataset are mild soundness issues that only leave a possibility to write memory\-safety bugs without unsafe code. Furthermore, we summarize three typical categories of memory\-safety bugs, including automatic memory reclaim, unsound function, and unsound generic or trait. While automatic memory claim bugs are related to the side effect of Rust newly\-adopted ownership\-based resource management scheme, unsound function reveals the essential challenge of Rust development for avoiding unsound code, and unsound generic or trait intensifies the risk of introducing unsoundness. Based on these findings, we propose two promising directions towards improving the security of Rust development, including several best practices of using specific APIs and methods to detect particular bugs involving unsafe code.

**Why it matters.** The counterargument, taken seriously: if memory\-safe languages solve the problem, low\-level skill is obsolete. The paper's answer — safety holds only outside `unsafe`, and reasoning about `unsafe` requires exactly the mental model C teaches — turns the counterargument back into support.

* * *

### A11. LLM\-Assisted Translation of Legacy FORTRAN Codes to C\+\+: A Cross\-Platform Study

Nishath Rajiv Ranasinghe, Shawn M. Jones, Michal Kucer, Ayan Biswas, Daniel O'Malley, Alexander Buschmann Most, Selma Liliane Wanna, Ajay Sreekumar · Los Alamos National Laboratory (LA\-UR\-25\-22376) · **arXiv:2504.15424** (2025); also in *Proceedings of the Workshop on AI for Scientific Discovery* · DOI: [10\.48550/arXiv.2504.15424](https://doi.org/10.48550/arXiv.2504.15424)

> Large Language Models (LLMs) are increasingly being leveraged for generating and translating scientific computer codes by both domain\-experts and non\-domain experts. Fortran has served as one of the go to programming languages in legacy high\-performance computing (HPC) for scientific discoveries. Despite growing adoption, LLM\-based code translation of legacy code\-bases has not been thoroughly assessed or quantified for its usability. Here, we studied the applicability of LLM\-based translation of Fortran to C\+\+ as a step towards building an agentic\-workflow using open\-weight LLMs on two different computational platforms. We statistically quantified the compilation accuracy of the translated C\+\+ codes, measured the similarity of the LLM translated code to the human translated C\+\+ code, and statistically quantified the output similarity of the Fortran to C\+\+ translation.

**Why it matters.** Covers the FORTRAN leg of your scope and the AI angle simultaneously: a national lab trying to automate away its Fortran dependency, and finding that verification still requires people who read both languages. *Preprint plus workshop paper — check the archival version before citing.*

* * *

## Part B — Computer science education

### B1. Computing Education in the Era of Generative AI

Paul Denny, James Prather, Brett A. Becker, James Finnie\-Ansley, Arto Hellas, Juho Leinonen, Andrew Luxton\-Reilly, Brent N. Reeves, Eddie Antonio Santos, Sami Sarsa · **Communications of the ACM**, vol. 67, no. 2 (February 2024), pp. 56–67 · DOI: [10\.1145/3624720](https://doi.org/10.1145/3624720)

> The computing education community has a rich history of pedagogical innovation designed to support students in introductory courses, and to support teachers in facilitating student learning. Very recent advances in artificial intelligence have resulted in code generation models that can produce source code from natural language problem descriptions — with impressive accuracy in many cases. The wide availability of these models and their ease of use has raised concerns about potential impacts on many aspects of society, including the future of computing education. In this paper, we discuss the challenges and opportunities such models present to computing educators, with a focus on introductory programming classrooms. We summarize the results of two recent articles, the first evaluating the performance of code generation models on typical introductory\-level programming problems, and the second exploring the quality and novelty of learning resources generated by these models. We consider likely impacts of such models upon pedagogical practice in the context of the most recent advances at the time of writing.

**Why it matters.** Sets the stakes for the education half. If AI writes the high\-level code, the residual human value shifts toward the things models are worst at — reasoning about machine behavior, performance, and correctness beneath the abstraction.

* * *

### B2. Nand to Tetris: Building a Modern Computer System from First Principles

Shimon Schocken · **Communications of the ACM**, vol. 67, no. 5 (May 2024) · DOI: [10\.1145/3626513](https://doi.org/10.1145/3626513)

> Starting from Nand gates only, students build a hardware platform comprising a CPU, RAM, datapath, and a software hierarchy consisting of an assembler, a virtual machine, a basic OS, and a compiler for a simple, Java\-like object\-based language. The course synthesizes traditionally separate topics — computer architecture, compilation, and operating systems — into one integrated, hands\-on learning experience spanning 12 projects completed in a single semester. The approach emphasizes abstraction and modularity as cornerstones of sound system engineering.

**Why it matters.** The flagship pedagogical answer to "why teach this at all": low\-level work justified not as vocational training but as the only way to make abstraction itself legible. Note that the passage above is assembled from the article's key\-insights framing rather than a formal abstract — quote from the full text.

*Full text via the ACM Digital Library; also summarized at [nand2tetris.org](https://www.nand2tetris.org/).*

* * *

### B3. Variations on "From Nand to Tetris" with Logisim and ARM

Ivaylo Ilinkin · **ITiCSE 2023** (Proceedings of the 2023 Conference on Innovation and Technology in Computer Science Education, vol. 1), Turku, Finland · DOI: [10\.1145/3587102.3588858](https://doi.org/10.1145/3587102.3588858)

> This paper shares experience with using Logisim to complement the hardware specification approach and accompanying simulator for the projects in "From Nand to Tetris" (N2T; Shocken et al., SIGCSE'09). Student feedback indicates that Logisim enhances the visualization of the main concepts and can be used effectively in parallel with the framework developed in N2T. This is achieved via an external Logisim library implemented by the authors that extends the rich set of components available in Logisim with the specialized circuits required in N2T (e.g. ALU, CPU, Screen, Keyboard). Upon completing the projects the students are able to execute the same machine code for a Pong\-like game on their Logisim and N2T computers.

**Why it matters.** Evidence that the Nand\-to\-Tetris model is actively being adapted and taught, not merely admired — and a concrete data point on what tooling makes low\-level material tractable for undergraduates.

* * *

### B4. Enhancing High\-Level Language Concept Comprehension through a Notional Machine Approach of Assembly Language Education

Sagnik Nath (University of California, Santa Cruz) · **2024 ASEE Annual Conference & Exposition**, Portland, Oregon · DOI: [10\.18260/1\-2\-\-47307](https://doi.org/10.18260/1-2--47307)

> In computer science curricula, the inclusion of assembly language programming is commonplace regardless of students' focus on computer science (CS) or computer engineering (CE) majors. The key objective within our university's (University of California, Santa Cruz) foundational "Computer Systems and Organization" (CSE12) course is dual\-fold: to cultivate a deep understanding of machine architecture's programmer model and to seamlessly prepare both CS and CE undergraduates for the advanced concepts in the subsequent "Computer Architecture" (CSE120) course. Current literature also highlights the merits of teaching assembly language, positing that it enables proficiency in higher\-level programming languages. However, transitioning from an introductory high\-level language\-based programming to assembly language can be jarring due to the stark contrast in instruction paradigms. In response, we have reimagined assembly language assignments within CSE12. Leveraging the open\-source RARS assembly language runtime emulator, we have reshaped lab exercises to better emulate scenarios akin to those encountered in high\-level language programming. This transforms RARS into a Notional Machine that bridges the gap between high\-level language abstractions and low\-level assembly implementation. Gathering quantitative and qualitative feedback from course surveys, our study reaffirms the effectiveness of this pedagogical strategy. Preliminary data suggest that students not only gain a deeper comprehension of machine architecture but also exhibit improved readiness for subsequent courses, underscoring the notional machine's role in facilitating a smoother transition between programming paradigms.

**Why it matters.** The most on\-point education paper in the set. It states the pedagogical claim your thesis tests — that assembly makes you better at high\-level languages — and reports survey evidence for it. Note the honest limitation: self\-reported, single\-institution, "preliminary data."

* * *

### B5. Main Memory in Program Execution: Threshold Concept in CS

Christina Kyriakou, Agoritsa Gogoulou, Maria Grigoriadou · **SN Computer Science**, vol. 6 (2025) · DOI: [10\.1007/s42979\-025\-03971\-w](https://doi.org/10.1007/s42979-025-03971-w)

> Recent studies have shed light on the challenges students face in grasping certain aspects of computer science (CS) curricula. According to the threshold concepts theory, specific foundational ideas, if not thoroughly understood, can serve as cognitive barriers that hinder the comprehension of subsequent topics. Within this theoretical framework, the organization of main memory in program execution is suggested as a potential threshold concept in understanding computer operations. The present study aims to examine students' understanding of topics related to main memory organization, operation, and its role in program execution. It seeks to categorize and elucidate students' conceptions and misconceptions through an analysis of their written responses to open\-ended questions as well as through small\-group discussions crafted to deepen insights. The development of questions grounded in Kintsch's text comprehension model theory proved beneficial for uncovering students' conceptualizations. The findings highlight a prevalent challenge among students in articulating the importance of main memory for computer operations and in establishing a conceptual link between main memory organization and the execution of program instructions. These findings underscore the significance of the proposed threshold concept. In response to the emerging misconceptions, CS educators should provide insight into students' comprehension and devise a comprehensive, integrated instructional approach to tackle the fundamental interrelated CS concepts.

**Why it matters.** Gives you a learning\-sciences vocabulary — *threshold concept* — for arguing that memory and machine model are not optional curriculum decoration but gateways whose absence blocks later understanding.

* * *

### B6. Closing the Gap Between Software Engineering Education and Industrial Needs

Vahid Garousi, Görkem Giray, Eray Tüzün, Cagatay Catal, Michael Felderer · **IEEE Software**, vol. 37, no. 2 (2020), pp. 68–77 · DOI: [10\.1109/MS.2018.2880823](https://doi.org/10.1109/MS.2018.2880823)

> According to different reports, many recent software engineering graduates often face difficulties when beginning their professional careers, due to misalignment of the skills learnt in their university education with what is needed in industry. To address that need, many studies have been conducted to align software engineering education with industry needs. To synthesize that body of knowledge, we present in this paper a systematic literature review (SLR) which summarizes the findings of 33 studies in this area. By doing a meta\-analysis of all those studies and using data from 12 countries and over 4,000 data points, this study will enable educators and hiring managers to adapt their education / hiring efforts to best prepare the software engineering workforce.

**Why it matters.** The methodological backbone for the education\-meets\-industry half: a 33\-study systematic review with over 4,000 data points on which skills industry actually reports missing. Mine its skill taxonomy for where low\-level topics rank.

* * *

## Part C — How the set supports the argument

The seventeen papers fall into four moves you can make in sequence.

**1\. The abstraction is not free.** Leiserson et al. (A1) and Pereira et al. (A2) establish that the performance and energy gap between high\-level and low\-level implementations is large and, in the post\-Moore era, economically consequential. Stoico et al. (A3) show that Python's practical performance is borrowed from compiled code, not native to the language.

**2\. The AI stack runs on this code.** Li & Bezemer (A5, A6), Chen et al. (A7), Ho et al. (A8), and Tambon et al. (A9) collectively document that the frameworks powering modern AI are large native\-code systems with conventional systems bugs, under\-maintained language bindings, and failure modes invisible from the Python surface.

**3\. Abstraction failures are security failures.** Staicu et al. (A4) show the memory\-safety guarantee ends at the native boundary; Xu et al. (A10) show that even Rust relocates rather than eliminates the need to reason about unsafe low\-level code. Ranasinghe et al. (A11) show that AI\-assisted migration off legacy Fortran still requires humans who can verify both sides.

**4\. So the curriculum question is live.** Denny et al. (B1) frame what generative AI leaves for humans to know; Schocken (B2) and Ilinkin (B3) offer the pedagogical model; Nath (B4) supplies direct evidence for the transfer claim; Kyriakou et al. (B5) supply the theoretical grounding for treating memory as a gateway concept; Garousi et al. (B6) supply the industry\-alignment methodology.

* * *

## Known gaps to fill next

- **No study directly measures whether low\-level coursework predicts industrial performance.** The transfer claim in B4 is self\-reported and single\-institution. This gap is arguably your thesis's contribution.
- **The education half is thinner than the industry half** — partly a real feature of the literature (assembly pedagogy is published sporadically), partly a search limitation. A targeted sweep of SIGCSE TS 2024–2026 and ACM TOCE through the Niagara library would firm this up.
- **No labor\-market evidence.** A job\-postings or developer\-survey study quantifying demand for C/C\+\+/Fortran skills would strengthen Part A; the reputable peer\-reviewed versions are hard to find through open search.
- **Two preprints (A3, A11)** need their archival versions confirmed.
- **A2 has methodological critics.** If you lean on the energy ranking, engage the rebuttal literature.
