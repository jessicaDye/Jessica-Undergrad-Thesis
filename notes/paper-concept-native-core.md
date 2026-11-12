# Paper Concept — The Native Core of the Python Stack

Working title: *The Native Core: Memory Safety, the Scientific Python Stack, and the Case for Low-Level Literacy*
Target: SIGCSE TS 2027 SRC (2 pp., 30 Sept 2026) → ITiCSE 2027 (6 pp., Jan 2027)
Drafted 26 Aug 2026.

## Decision: fuse the two angles

Memory safety alone is a crowded conversation; the dependency-stack argument alone is the abstraction debate again. Together they make a claim nobody has made.

**Thesis:** The scientific/ML Python stack is a large, growing body of memory-unsafe C/C++ reached almost exclusively through Python entry points, maintained and extended by a workforce increasingly trained only in Python. Memory-safety guidance addresses software manufacturers; it is silent on the education pipeline. Curricula treating low-level languages as optional train fluent consumers of a substrate they cannot inspect, at the moment the field has declared that substrate a liability.

## Correction — do not claim policy exempts ML

Initial hypothesis was that memory-safety policy explicitly exempts scientific/ML software. **It does not.** The CISA/NSA/FBI *Case for Memory Safe Roadmaps* is directed broadly at "software manufacturers," no category carve-outs. Claiming otherwise is a paper-killing error.

Defensible version instead:
1. Guidance targets manufacturers and SDLCs; says nothing about training, curriculum, or workforce. **That silence is the gap.** ← policy hook
2. The scientific/ML stack is largely community-maintained open source, not a "manufacturer" with roadmap obligations — compliance pressure lands unuevenly regardless of nominal scope.
3. The native core is extended disproportionately by domain scientists / ML researchers, trained Python-first. ← softest link, needs a citation or own data

## Evidence spine

- **Mechanism:** *Python Fuzzing for Trustworthy ML Frameworks* (arXiv 2403.12723, J. Math. Sci.) — 3 new bugs, all memory-safety defects in C/C++, all found *through Python APIs* (2× null-deref/SEGV in PyTorch flatbuffers, 1× OOB read in h5py's HDF5 C core). Existence proof, not a rate — don't lean on it for magnitude.
- **Severity:** CVE-2024-31580 — heap buffer overflow in PyTorch `runtime/vararg_functions.cpp`, fixed v2.2.0, CVSS v4 8.7 High.
- **TO GET:** *Software vulnerabilities in TensorFlow-based deep learning applications* (Computers & Security, 2022) — ScienceDirect blocked automated access. The memory-safety proportion in native code is the single most valuable number for the argument. Get it through the library before writing.
- **Gap by citation:** *What Are Cybersecurity Education Papers About?* (SLR of SIGCSE + ITiCSE) lets the gap be demonstrated rather than asserted. Related: SIGCSE 2023 *Towards Finding the Missing Pieces to Teach Secure Programming Skills*; SIGCSE 2018 *Evaluating Two Methods for Integrating Secure Programming Education*.
- **Standards leverage:** CS2023 already codifies Systems Fundamentals + Architecture & Organization. Argument becomes "guidelines already require this and programs are drifting," not "add something new."

## Curriculum audit — now the test of a stated claim

40–60 undergrad CS programs, public catalogs. Code for:
- C/C++/assembly course: required / elective / absent
- Systems requirement: *writing* low-level code vs only studying it
- Any coursework on native extensions, FFI, bindings (expect near-zero — a null result is a finding; SIGCSE welcomes null results)

No IRB, 2–3 weeks. Sample deliberately (R1s, PUIs, known Python-first curricula) and state the sampling frame — arbitrary convenience samples are the usual criticism.

## SRC structure (2 pp.)

Problem (~150w) → Background: guidance targets manufacturers not curricula, CS2023 already asks for these outcomes (~200w) → Approach: audit, sampling, coding scheme (~250w) → Results + one figure (~300w) → Contribution and next steps (~150w).

Five weeks is enough **if the audit starts within a week.** The audit is the long pole, not the writing.

## Counterargument to pre-empt

*"If industry is migrating away from memory-unsafe languages, isn't teaching C training for a shrinking domain?"*

Answer: migration requires reading the code being migrated (a C-comprehension skill); Rust's ownership model is taught against the failure modes it prevents, making C literacy a prerequisite for safe-language fluency rather than an alternative; and the scientific stack's native core is growing, driven by performance demands safe abstractions don't yet meet.

**Concede the CS1 point** — the case for C as a *first* language is weaker than it was. Costs nothing, buys credibility.

## This week

1. Get the Computers & Security 2022 TensorFlow paper via library
2. Lock the audit sampling frame and coding scheme *before* coding any catalogs
3. Start ACM Student Membership + ORCiD (both gate submission)
4. Send this framing to the advisor now, not after a draft exists
