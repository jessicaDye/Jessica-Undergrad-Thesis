# CLAUDE.md — Assembly Required? (Jessica Dye, Niagara University honors thesis)

## What this project is
Honors thesis, aimed at **HCI / computing education**. Working title: **"Reviewing What You Never Wrote: Memory-Model Literacy and the Human Review of AI-Generated Code at the Python/C Boundary."** (The title may change to fit the literature-review format.)

**Format (updated 13 Nov 2026): a literature review, not an empirical study.** No pilot prompts, corpus study or student pilot will be run for the thesis. Those become a *proposed research agenda*. The thesis is also a pitch: "there is something worth researching here, and I'm the person to do it."

**Central argument (refined 13 Nov):** Software built with high-level languages and AI tools still depends on C and C++. Not every developer needs to understand that layer, but the ecosystem needs enough specialists who do, because someone must be able to check and fix what the tools produce. Education and AI tool design should keep that specialist pipeline alive. **Pro-AI stance:** AI can build understanding, not just replace it, depending on how it's used.

## Files
- `notes/lit-review-outline-2026-11-12.md` — **start here.** Thesis statement, structure, Rust/GC/AI-tool counterarguments, central claim, proposed research agenda, sources by section.
- `notes/hugs-3page-outline-2026-11-12.md` — short-abstract outline and trimmed source list. Basis for the CHI SRC submission.
- `paper/refs.bib` — all references, including those added 12 Nov (some flagged to confirm).
- `paper/main.tex` — the earlier HUGS draft. **Out of date:** still describes the corpus study and student pilot as planned work.
- `thesis-plan.md`, `proposal.md` — **out of date** (empirical design). Useful for the research-agenda section and the defeat conditions.
- `prior-art-review.md` — literature review, closest prior art, intro scaffold.
- Other `notes/` files — earlier background docs (Aug 2026): native-core studies, transfer pathway, theoretical grounding (notional machines), Hu & Zhang digest, lit searches.
- `pipeline/`, `prompts/` — from the dropped empirical plan. Keep for the research agenda; don't extend them.

## Current phase and deadlines
- **Priority: a decent full thesis draft by December 2026.**
- **Likely venue: CHI 2027 Student Research Competition (SRC), Pittsburgh, May 10–14, 2027.** Submission due **21 Jan 2027** (check the exact time on the official site), notification 18 Feb. Extended abstract up to 5 pages, references not counted. If selected: attend in person, register for CHI, active ACM student membership. Not yet decided; decide after the December draft.
- HUGS 2027 @ ICSE (Dublin, due 13 Nov 2026) is **not being pursued**. Attending in person isn't feasible.

## Settled decisions (don't relitigate without asking)
- **Scale: undergraduate honors thesis, not a dissertation.** Depth comes from the idea, not volume. Ask before building tooling or launching big research sweeps.
- **Literature review format.** Don't propose running studies for the thesis. Studies go in the proposed research agenda.
- **Citation style: APA** for the thesis (confirm with the honors program). A CHI/ACM submission uses that venue's template.
- **Guiding question:** "As AI becomes increasingly capable of writing and debugging software, what happens when both the developer and the AI are working with abstractions built on lower-level systems that the developer doesn't understand?"
- **Framework:** **L1** managed model / **L2** manual model / **L3** boundary contract (new/borrowed/stolen refs, exception state, allocator families). Most developers can work at L1 with AI help; the ecosystem needs specialists at L2/L3. Framing: refcounting *is* CPython's GC.
- **Structure of the argument:** give each abstraction full credit first, then its limits (garbage collection, Rust, AI security tools).
- **Proposed research agenda:** main study = can AI tools that explain the memory model build L2/L3 understanding (pro-AI hypothesis, with the skeptical view and how to detect it built in). Supporting: does L1/L2/L3 level predict catching boundary bugs; interviews with CPython/NumPy maintainers on how specialists form; optional corpus study as a technical baseline.
- **Closing section:** pro-AI discussion of transhumanism using *Magnifica Humanitas*. Thesis only, not the short abstract. Keep normative claims clearly separate from what the literature shows.
- Don't cite chatbots as sources.
- **Don't criticize or single out Niagara University.** Present the scarcity of C/C++ expertise as a general trend backed by sources, not as a claim about the school.
- Ethics (if any study is ever run): **never recruit from classes Jessica teaches or TAs/grades**; an advisor or another instructor announces the study; responses anonymous.

## Writing rules
- Novelty wording: "We found no prior evaluation of the security of LLM-generated Python/C API code." Don't claim more than that. Do an ACM DL / IEEE Xplore check before submitting anywhere.
- Differentiate explicitly from Khalid et al. (S&P 2027), the closest prior art.
- State defeat conditions for the proposed studies (see thesis-plan.md §4).
- NumPy native-code share: Yang & Cai say 38%, our own count was 55.7%. State the counting rule wherever either number is cited.
- Verify every figure and citation against the original source. Several `refs.bib` entries added 12 Nov are flagged to confirm.
- Personal experience (e.g., using AI daily to learn) is motivation, never evidence.

## Conventions for code (only if the research agenda is ever run)
- Pin every tool version; everything runnable from the command line.
- Log model name, version, date and temperature for every generated sample. Treat a generated corpus as frozen; never edit samples in place.
- Prompts are realistic developer requests and never hint at security.
