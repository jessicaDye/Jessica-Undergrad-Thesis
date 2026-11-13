# Publication Feasibility — Assembly Required?

Assessed 26 Aug 2026. Paper type evaluated: literature review / position paper, no original data. Undergraduate thesis. Target window 3–6 months.

## Verdict

Publishable, but not as a general "is C still relevant?" survey — that genre is saturated and would be summarily rejected at a research track. Publishable as a narrow, timely position paper at venues that explicitly accept non-empirical argument.

## Why the broad framing fails

Three existing bodies of work cover most of what a broad review would say:
- CS1/CS2 language-choice studies (incl. direct evaluations of C as a first language)
- Systems/architecture pedagogy — CS2023 already codifies Systems Fundamentals and Architecture & Organization as knowledge areas
- The decades-old abstraction debate in CACM / ACM Inroads

Reviewer's rejection writes itself: no new data, no new argument.

## The gap (pick one)

**1. Memory-safety mandates reframe the question.** NSA/CISA guidance (2023–2025) pushed industry toward memory-safe migration. Surface reading: stop teaching C. The contestable claim: the transition *raises* the value of C literacy — migration requires auditing legacy C, Rust's ownership model is unintelligible without the pointer semantics it constrains, and every safe runtime bottoms out in unsafe code. CS-education literature has not metabolized this. Nobody owns this argument yet.

**2. The dependency-stack argument in the AI era.** NumPy, PyTorch, CPython, CUDA kernels — the stack students learn on is C/C++/assembly wearing a Python interface. "What your tools are actually written in" has not been systematically examined as a curricular justification. Matches the thesis's existing scope.

## Venues

| Venue | Deadline | Notes |
|---|---|---|
| **SIGCSE TS 2027 — ACM SRC (undergrad)** | **30 Sept 2026** | 2 pages max incl. refs. Needs ACM Student Membership + ORCiD. Notification 10 Nov. Best near-term shot. |
| SIGCSE TS 2027 — Posters | 30 Sept 2026 | Same Round Two deadline |
| **ITiCSE 2027, Glasgow** | Abstract 11 Jan, paper 18 Jan 2027 (provisional) | Primary target; fits the window |
| CCSC regionals | Rolling through fall | Journal of Computing Sciences in Colleges; student paper tracks; accessible fallback |
| SIGCSE TS 2028 — PCI track | ~July 2027 | PCI call explicitly states position papers "need not present original data." The real home for this paper. 6 pages + 1 refs, double-anonymous. |

SIGCSE requires in-person presentation of accepted work — budget for travel.

## Required changes

- Cut FORTRAN — reads as nostalgia, weakens the paper
- Narrow to ONE claim; the thesis becomes source material, not the paper
- Get a faculty co-author (note: SRC *graduate* category forbids supervisor co-authorship; undergrad category permits teams)
- Add cheap original data — this is the highest-leverage change:
  - **Curriculum audit**: 40–60 CS programs' public catalogs coded for required/elective/absent low-level course. No IRB, ~2–3 weeks.
  - **Job-posting analysis**: C/C++/Rust/assembly requirements by sector. Public data, no IRB.

## Plan

- **Now → 30 Sept 2026** — draft 2-page SRC submission; sort ACM membership + ORCiD early
- **Sept–Nov** — run the curriculum audit
- **Nov** — SRC notification; confirm ITiCSE dates
- **Nov–Jan** — write the 6-page ITiCSE paper around one claim
- **11/18 Jan 2027** — submit to ITiCSE 2027
- **Rolling** — CCSC regional as parallel/fallback
- **~July 2027** — SIGCSE TS 2028 PCI

## Odds

Pure lit review, no data: poor at ITiCSE, moderate at CCSC, reasonable at SIGCSE SRC.
Position paper with one sharp claim + curriculum audit: competitive at ITiCSE, credible SIGCSE PCI submission.

The gap between those is ~3 weeks of catalog coding and the discipline to discard four-fifths of the thesis.
