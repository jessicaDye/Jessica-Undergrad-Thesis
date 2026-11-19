# Chapter 8: Proposed Research Agenda (scaffold)

*Scaffold drafted 19 Nov 2026. Target: about 1,200 words. Each block below is one paragraph: a suggested topic sentence, the evidence that goes in it, and what still needs checking. The prose is yours to write; replace each block with your paragraph as you go.*

**Chapter claim:** The framework from chapter 7 is testable, and here is how. These studies are *proposed* for future research; none is run in this thesis.

**Rule for the whole chapter:** this chapter is the pitch: "there is something worth researching here, and I'm the person to do it." Write it confidently, and state the defeat conditions plainly. Saying what would prove you wrong reads as strength.

**Legend:** ✅ in `refs.bib` · ➕ add to `refs.bib` · ⚠️ verify against the original

---

## 8.1 From framework to questions (≈150 words)

**¶1. Open the agenda.**
- *Topic sentence idea:* "The argument so far rests on the literature; the framework it produces makes claims that can be checked."
- Three questions, one per study: Can AI build L2/L3 understanding? Does L2/L3 understanding predict catching boundary bugs? How do specialists form today?
- Say once, clearly, that these are proposed, not run.

---

## 8.2 Study A (main): can AI tools build understanding? (≈400 words)

**¶2. Design.**
- Two AI assistants for the same boundary tasks: one explains what is happening in memory (reference counts, ownership, which allocator owns what) before or alongside its code; the other only writes the code.
- Measure L2/L3 understanding afterward *and* on a delayed test, with the AI taken away (borrow the phase-2 idea from the epistemic-debt study ➕).
- Also measure confidence, so overconfidence can be detected.

**¶3. Hypothesis (pro-AI) and its support.**
- AI designed to explain the memory model builds L2/L3 understanding.
- Support: ✅ shentamkin2026 (explanation-seeking kept understanding); ➕ Epistemic Debt (the explanation gate kept most repair ability).

**¶4. The skeptical view, built in.**
- AI help produces dependence and overconfidence. ✅ prather2024, ✅ lee2025
- How the design detects it: if the explaining assistant doesn't beat the code-only one on the delayed test, or both groups overestimate their understanding, the skeptics are right for this setting.

---

## 8.3 Study B: does understanding predict catching bugs? (≈250 words)

**¶5. Design.**
- Reviewers at different L1/L2/L3 levels review the same boundary code, mixed with clean controls.
- Design choices from prior work: everyone is told to look for security problems (✅ braz2022); the task is reading, not writing (✅ fulton2024); no AI review is shown, because it narrows where people look (➕ Tufano 2025).
- **Key comparison:** does L1/L2/L3 level predict detection better than years of experience, which prior work found wanting (✅ edmundson2013, ✅ khalid2027)?

**¶6. Why it matters.**
- This is the direct test of chapter 7's claim that L3 is what boundary review requires.
- Note: no validated L3 instrument exists. Building even a short one is itself a contribution. L2 items can borrow from Almansoori et al.'s rubric (✅ almansoori2023).

---

## 8.4 Study C: how do specialists form today? (≈150 words)

**¶7. Design.**
- Semi-structured interviews with CPython, NumPy or similar maintainers: how they learned the C layer, what made it stick, whether AI tools now help or get in the way.
- *So what:* answers ch. 6's pipeline question with first-hand accounts instead of employment statistics.

---

## 8.5 Study D (optional): what does AI leave behind at the boundary? (≈150 words)

**¶8. Design, briefly.**
- The original corpus study as a technical baseline: realistic developer requests with no security hints, the generated code run through sanitizers, a debug CPython, static analyzers and an LLM reviewer; ground truth triangulated because tools disagree with human labels (✅ firouzi2026).
- The 10 pilot prompts in `prompts/pilot/` can go in an appendix as an example.

---

## 8.6 What would prove this wrong (≈150 words)

**¶9. Defeat conditions** (from `thesis-plan.md` §3 and `notes/the-ai-question.md`):
- Automated tools catch almost every boundary defect → the case for L2/L3 specialists weakens.
- L1 predicts bug-catching as well as L3 → understanding at the garbage-collector level is enough.
- An LLM reviewer alone matches the full tool set → the human role becomes "verifying the verifier."
- Autonomous patching becomes reliable on real codebases without human verification → the case weakens considerably.
- No measure predicts detection → replicates Edmundson and Khalid at the boundary; still worth reporting.
- Each outcome would still inform curriculum and tool design.

---

## 8.7 Ethics and hand-off (≈100 words)

**¶10. Close.**
- Ethics, if any study is ever run: never recruit from classes Jessica teaches, TAs or grades; an advisor or another instructor announces the study; responses are anonymous; IRB approval first.
- Hand-off sentence to ch. 9: *the studies ask what is true; the next chapter asks what we should want.*

---

## Checklist before this chapter counts as drafted

- [ ] Every study says "proposed," and none is described as planned or underway for the thesis
- [ ] Study A has both the pro-AI hypothesis and the skeptical view, with how to tell them apart
- [ ] Defeat conditions are stated plainly
- [ ] Add to `refs.bib`: Tufano 2025, Epistemic Debt (shared with ch. 5–6)
