# Chapter 6: Expertise and How It Forms (or Erodes) (scaffold)

*Scaffold drafted 19 Nov 2026. Target: about 2,000 words. Each block below is one paragraph: a suggested topic sentence, the evidence that goes in it, and what still needs checking. The prose is yours to write; replace each block with your paragraph as you go.*

**Chapter claim:** Automation depends on rare human skill for the cases it misses. The routes into that skill are narrowing. AI can build that skill or erode it, depending on how it's used.

**Rule for the whole chapter:** this is where the pro-AI stance has to earn its place. Give the skeptical evidence its full weight, then show that the same studies point to a kind of AI use that preserves understanding. Keep the job-market evidence modest: it's correlational.

**Legend:** ✅ in `refs.bib` · ➕ add to `refs.bib` · ⚠️ verify the figure against the original before keeping it

---

## 6.1 The ironies of automation (≈350 words)

**¶1. Open with Bainbridge.**
- *Topic sentence idea:* "Forty years before code assistants, Lisanne Bainbridge described the trap this thesis is about: the more a system is automated, the more it depends on human skill for the rare cases the automation cannot handle, and the less chance people have to practice that skill."
- ✅ bainbridge1983. Her setting was industrial process control; say so, then say why it transfers.

**¶2. Map it onto software.**
- The automation: AI that writes code, and tools that find and patch bugs (ch. 4–5).
- The rare cases: boundary bugs that tools miss (the refcount example, ch. 7), patches that pass tests but are wrong (AIxCC, ch. 4 ¶12).
- The skill that erodes: reading native code and reasoning about memory (L2/L3).
- *So what:* this is the mechanism behind the spine. It's about the ecosystem's supply of specialists, not any one programmer.

---

## 6.2 The pipeline is narrowing (≈450 words)

**¶3. Junior roles are shrinking where AI adoption is high.**
- Brynjolfsson et al.: a 16% relative employment decline for 22–25-year-olds in the most AI-exposed occupations. ✅ brynjolfsson2025 ⚠️
- Lichtinger & Hosseini Maasoum: in firms adopting generative AI, junior employment fell relative to non-adopters, mainly through slower hiring, while senior employment held. ➕ SSRN 5425555, 2025 ⚠️ (not yet read in full; get the effect size)
- **Say plainly:** both are correlational and the causes are contested. The claim is only that this pathway is under pressure.

**¶4. Why junior roles matter for this skill.**
- Junior work under review is where people traditionally learned the C layer: fixing small bugs, having patches reviewed by maintainers.
- Optional supporting quote from ch. 2: Hu & Zhang's line that the cleanup is "often missed by developers because they need not do this in pure Python code." ✅ huzhang2023 (the skill doesn't come from Python experience on its own)
- *So what:* fewer junior roles means fewer places where L2/L3 understanding forms on the job.

**¶5. What curricula say and what students show.**
- CS2023, the current ACM/IEEE-CS/AAAI curriculum guidelines: **check what it actually says about memory management and memory safety before citing.** ➕ ACM/IEEE-CS/AAAI Joint Task Force, *Computer Science Curricula 2023*, 2024 (open access)
- Students show gaps in secure-programming knowledge, including *knowledge of memory*. ✅ almansoori2023; ➕ Lam et al., SIGCSE 2022
- **Don't single out Niagara.** Present this as a general trend backed by sources.
- Optional: maintainer burnout and the xz-utils incident (2024), only if "maintainability" stays in the thesis statement (open decision).

---

## 6.3 You can't review what you can't picture (≈450 words)

**¶6. Notional machines.**
- A *notional machine* is the model of execution a learner uses to reason about code. ➕ Sorva, *Notional Machines and Introductory Programming Education*, ACM TOCE 2013 (**missing from `refs.bib` and needed**)
- The abstraction hides the machine: a Python developer's notional machine has no allocator, no ownership and no reference counts.

**¶7. Memory as a threshold concept.**
- Main memory in program execution behaves like a *threshold concept*: if it isn't understood, later topics are blocked. ➕ Kyriakou, Gogoulou & Grigoriadou, *SN Computer Science* 6 (2025), doi:10.1007/s42979-025-03971-w
- *So what:* memory isn't optional curriculum decoration; it's a gateway.

**¶8. Even L1 is hard.**
- Aliasing study: about 30% of upper-level students answered aliasing questions incorrectly, and explicit vocabulary teaching didn't stick. ➕ *Student Understanding of Aliasing and Procedure Calls*, SPLASH-E 2017 ⚠️ (get the authors; see `notes/theoretical-grounding-two-transfers.md`)
- If L1 (references and aliasing) is this hard to build, L2/L3 won't appear on its own.
- Key line from your notes: **AI assistance can supply code, but it doesn't install a notional machine.**

---

## 6.4 AI can build understanding or replace it (≈650 words)

**¶9. The skeptical evidence first.**
- In an introductory C++ course, generative AI helped students with strong metacognition and compounded the difficulties of those who struggled; struggling students overestimated their understanding. ✅ prather2024 (complete the author list in `refs.bib`)
- Educators were warning about this as soon as code generation arrived. ✅ becker2023
- Tie back to ch. 5 ¶6–7: over-trust, and beginners understanding AI code poorly (✅ lee2025, ➕ Zi 2025).

**¶10. The strongest single finding: epistemic debt.**
- *Mitigating "Epistemic Debt"* (ACM L@S 2026): 78 novices in three conditions. In phase 2 the AI was taken away and participants had to fix an injected race condition. ➕ arXiv 2602.20206, preprint ⚠️

| Condition | Phase 1 working software | Phase 2 repair success |
|---|---|---|
| Manual (no AI) | 65% | 69% |
| AI with an explanation gate | ~90% | 61% |
| Unrestricted AI | ~90% | 23% |

- The authors define epistemic debt as software the user "owns" legally but not cognitively. ⚠️ (quote exactly from the paper)
- **Read the table carefully:** unrestricted AI produced the most working code and the least ability to repair it. AI that required explanation kept most of the repair ability *and* most of the productivity.

**¶11. The pro-AI evidence.**
- In a randomized study, developers who asked the AI for explanations kept more of their understanding than those who delegated the work. ✅ shentamkin2026 (**title still TODO in `refs.bib`**; confirm the design and result)
- Together with ¶10: the explanation-gate condition and the explanation-seeking developers point the same way.

**¶12. The synthesis of 6.4.**
- The question isn't AI or no AI. It's which kind of use builds understanding and which kind replaces it.
- This is the pro-AI stance stated precisely: AI that explains can be a way *into* L2/L3, not just a way around it.
- Name what would weaken it: if explanation-style AI turns out not to beat code-only AI on later understanding, the skeptics are right for this setting (this becomes Study A in ch. 8).

---

## 6.5 So what (≈100 words)

**¶13. Chapter close and hand-off.**
- Pattern: automation raises the stakes on rare skill (Bainbridge); the routes into it are narrowing; AI can widen or close them depending on design.
- Hand-off sentence to ch. 7: *to talk about which understanding needs protecting, we need a precise name for it.*

---

## Checklist before this chapter counts as drafted

- [ ] Add to `refs.bib`: Sorva 2013, Kyriakou 2025, the aliasing study (SPLASH-E 2017), Lam 2022, Lichtinger & Hosseini Maasoum 2025, CS2023, Epistemic Debt (L@S 2026)
- [ ] Fix the Shen & Tamkin title in `refs.bib`
- [ ] Read CS2023's memory-related sections before citing it
- [ ] Check Epistemic Debt for an archival version and the exact quote
- [ ] Correlational job-market evidence is labeled as correlational
- [ ] Skeptical evidence comes before the pro-AI evidence in 6.4
