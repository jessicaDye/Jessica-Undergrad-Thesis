# CLAUDE.md — Assembly Required? (Jessica Dye, Niagara University honors thesis)

## What this project is
Honors thesis + workshop paper: **"Reviewing What You Never Wrote: Memory-Model Literacy and the Human Review of AI-Generated Code at the Python/C Boundary."**
Main question: which defects in LLM-generated Python/C boundary code (C-API extensions, ctypes/cffi, exception propagation) survive automated review, and what level of memory-model literacy a human reviewer needs to catch them. Motivation includes the shrinking junior-developer apprenticeship as AI takes over entry-level work.

## Files
- `thesis-plan.md` — schedule, RQs, week-by-week checklist, deadlines. **Start here.**
- `proposal.md` — full proposal (design changes from the prior-art review already applied); full reference list.
- `prior-art-review.md` — literature review, closest prior art, intro scaffold.
- `notes/` — earlier project docs (Aug 2026): the native-core repository studies, the transfer-pathway angle, theoretical grounding (notional machines), the Hu & Zhang digest, lit searches. **Background only — the current design is in thesis-plan.md and proposal.md.** Useful for related work and motivation (e.g., NumPy native share, the Hu & Zhang quote).

## Current phase and deadline
Phase 1: **HUGS 2027 @ ICSE (Dublin)** — 3-page extended abstract, IEEE template, refs count toward the page limit.
**Due Fri 13 Nov 2026, 23:59 AoE (= Sat 14 Nov, 6:59 AM ET).** Aim to submit 12 Nov. Submit at icse2027-hugs.hotcrp.com.
Draft is in `paper/main.tex` (3 pages). The corpus study runs Nov–Jan, after HUGS.
Fallback/follow-on venue: CHI 2027 workshops (Pittsburgh, ~11 Feb 2027). No venue pays travel; SIGSOFT CAPS is partial and doesn't cover registration.

## Settled decisions (don't relitigate without asking)
- **Scale: undergraduate honors thesis, not a dissertation.** Depth comes from the idea; keep studies small, and put extras in future work (see thesis-plan.md §2). Ask before building tooling.
- **Guiding question:** "As AI becomes increasingly capable of writing and debugging software, what happens when both the developer and the AI are working with abstractions built on lower-level systems that the developer doesn't understand?" It's answered through SQ1 (native share, done), SQ2 (corpus), and SQ3 (student pilot). Pro-AI stance.
- HUGS abstract = research plan + motivating example; pilot data optional.
- Construct: **L1** managed model / **L2** manual model / **L3** boundary contract (new/borrowed/stolen refs, exception state, allocator families). Framing: refcounting *is* CPython's GC.
- Part 1 = corpus study, no IRB, the core of the HUGS paper. Pilot: 10 prompts × 2 models × 3 samples ≈ 60.
- Generators: Claude + GPT. LLM reviewer: Gemini (never a generating model).
- Automated tier: ASan/UBSan + debug CPython 3.12.16, cppcheck, clang-tidy, Gemini review. Valgrind is dropped (no Apple Silicon support); CodeQL is future work. Versions are pinned in `pipeline/requirements.lock`.
- Codebook from Yang & Cai 2026 taxonomy + Hu & Zhang 2020 bug patterns. Second coder (advisor?) on ~20% if available; otherwise use reproduction-confirmed defects and a single coder. Never an LLM as second coder.
- Part 2 = IRB student review pilot (~15–30 students), thesis only, after HUGS. Read-and-review task, security instruction for everyone, no AI review shown, confidence ratings, simple stats. The write/optimize-with-AI task is future work.
- Don't cite chatbots as sources.
- Ethics: **never recruit from classes Jessica teaches or TAs/grades**; an advisor or another instructor announces the study; responses anonymous.

## Conventions for code in this repo
- Pin every tool version in the scripts; everything runnable from the command line.
- Log model name, version, date and temperature for every generated sample. Treat the generated corpus as frozen and releasable — never edit samples in place.
- Record which tool flagged what, per sample, in a machine-readable file (CSV/JSON).
- Prompts are written as realistic developer requests (Stack Overflow / GitHub-issue style) and never hint at security.
- Suggested layout: `prompts/`, `corpus/` (generated samples + metadata), `pipeline/` (generation + analysis scripts), `audit/` (codebook, coder labels, κ), `paper/` (HUGS LaTeX).

## Writing rules
- Novelty wording: "We found no prior evaluation of the security of LLM-generated Python/C API code." Don't claim more than that. Do an ACM DL / IEEE Xplore check before submitting.
- Differentiate explicitly from Khalid et al. (S&P 2027), the closest prior art.
- State the defeat conditions (see thesis-plan.md §4).
- NumPy native-code share: Yang & Cai say 38%, our own count was 55.7%. State the counting rule wherever either number is cited.
