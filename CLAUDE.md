# CLAUDE.md — Assembly Required? (Jessica Dye, Niagara University honors thesis)

## What this project is
Honors thesis + workshop paper: **"Reviewing What You Never Wrote: Memory-Model Literacy and the Human Review of AI-Generated Code at the Python/C Boundary."**
Main question: which defects in LLM-generated Python/C boundary code (C-API extensions, ctypes/cffi, exception propagation) survive automated review, and what level of memory-model literacy a human reviewer needs to catch them. Motivation includes the shrinking junior-developer apprenticeship as AI takes over entry-level work.

## Files
- `thesis-plan.md` — schedule, RQs, week-by-week checklist, deadlines. **Start here.**
- `proposal.md` — full proposal (design changes from the prior-art review already applied); full reference list.
- `prior-art-review.md` — literature review, closest prior art, intro scaffold.

## Current phase and deadline
Phase 1: **HUGS 2027 @ ICSE (Dublin)** — 3-page extended abstract, IEEE template, refs count toward the page limit.
**Due Fri 13 Nov 2026, 23:59 AoE (= Sat 14 Nov, 6:59 AM ET).** Aim to submit 12 Nov. Submit at icse2027-hugs.hotcrp.com.
Bottleneck: manual audit + second coder. The pipeline must be producing samples by the weekend of 31 Oct.
Fallback/follow-on venue: CHI 2027 workshops (Pittsburgh, ~11 Feb 2027). No venue pays travel; SIGSOFT CAPS is partial and doesn't cover registration.

## Settled decisions (don't relitigate without asking)
- Construct: **L1** managed model / **L2** manual model / **L3** boundary contract (new/borrowed/stolen refs, exception state, allocator families). Framing: refcounting *is* CPython's GC.
- Part 1 = corpus study, no IRB, the core of the HUGS paper. Pilot: 10 prompts × 2 models × 3 samples ≈ 60.
- Automated tier: ASan/UBSan, Valgrind, cppcheck, clang-tidy, CodeQL, LLM review (+ cext-review-toolkit if usable).
- Codebook from Yang & Cai 2026 taxonomy + Hu & Zhang 2020 bug patterns; second coder on ~20%, report Cohen's κ.
- Part 2 = IRB student review pilot, thesis only, after HUGS. Read-and-review task, security instruction for everyone, no AI review shown, confidence ratings.
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
