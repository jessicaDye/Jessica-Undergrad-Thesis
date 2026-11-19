# Chapter 5: AI-Assisted Development and Security (scaffold)

*Scaffold drafted 19 Nov 2026. Target: about 1,800 words. Each block below is one paragraph: a suggested topic sentence, the evidence that goes in it, and what still needs checking. The prose is yours to write; replace each block with your paragraph as you go.*

**Chapter claim:** AI-written code has security flaws at measurable rates, and people trust it too much. Human review is the stated safeguard, but reviewing code you didn't write is hard, and experience alone doesn't make people good at it.

**Rule for the whole chapter:** lead with the data, not the hype. Give the mixed results (Sandoval) their full weight. The chapter's job is to show that *verification* is now the human's role, and that verification depends on understanding, not to show that AI is bad.

**Legend:** ✅ in `refs.bib` · ➕ add to `refs.bib` · ⚠️ verify the figure against the original before keeping it

---

## 5.1 The hand-off from chapter 4 (≈150 words)

**¶1. Pick up where chapter 4 ended.**
- *Topic sentence idea:* "If every fix in the previous chapter moves the human from writing code to verifying it, then the question becomes how well people verify code they did not write, and more of that code is now written by AI."
- One sentence of scale: AI assistants are now a normal part of writing code. (Keep it general, or find one adoption survey ➕. Don't cite a chatbot or a vendor marketing page.)
- Preview the chapter: what AI code gets wrong (5.2), how people trust it (5.3), how well humans review it (5.4).

---

## 5.2 What AI-written code gets wrong (≈450 words)

**¶2. AI assistants produce insecure code at measurable rates.**
- "Asleep at the Keyboard": Copilot suggestions for security-relevant scenarios were frequently vulnerable. ✅ pearce2022 ⚠️ (take the exact share of vulnerable programs from the paper)
- Optional, for C specifically: *LLM-CSEC* (10 models, CWE-classified weaknesses in AI-generated C). ➕ arXiv 2511.18966, preprint ⚠️
- *So what:* AI writes the same classes of memory bugs chapter 3 described.

**¶3. But the results are mixed, and say so.**
- In "Lost at C," students writing C with an AI assistant did not produce meaningfully more security-critical bugs than those without one. ✅ sandoval2023 ⚠️ (check the exact wording of their conclusion)
- Why the two results can both be true: Pearce measured raw suggestions; Sandoval measured what people shipped after working with the assistant. A human was in the loop.
- *So what:* the human in the loop is doing real work, which is exactly why it matters whether that human understands the code.

**¶4. The boundary is a gap in this evidence.**
- None of these studies looks at code that crosses the Python/C boundary. A 2026 study of LLM-generated bindings notes there is no benchmark for binding generation at all. ✅ ompl2026
- Novelty sentence, exact wording: "We found no prior evaluation of the security of LLM-generated Python/C API code."
- *So what:* the boundary code from chapter 2, where most native bugs in Python apps occur, is the least studied case.

---

## 5.3 Trust and overconfidence (≈400 words)

**¶5. People who use AI assistants can write less secure code and feel more confident about it.**
- ✅ perry2023 ⚠️ (get the exact comparison: share of secure answers in each group, and the confidence result)
- *So what:* confidence and correctness come apart, which is what makes review hard.

**¶6. More trust in AI goes with less critical thinking.**
- Knowledge workers who trusted generative AI more reported doing less critical thinking; those who trusted themselves more reported more. ✅ lee2025 (self-reported; say so)
- Name the general idea, briefly: *automation bias*, relying on an automated suggestion instead of checking it. ➕ one source, or point forward to Bainbridge in ch. 6.

**¶7. Beginners understand the AI's code much less well than their own request.**
- 32 CS1 students, 160 tasks: 59.3% understood the prompt, but only 32.5% understood the LLM-generated code. The authors name automation bias as one barrier. The study was in Python. ➕ Zi et al., *"I Would Have Written My Code Differently": Beginners Struggle to Understand LLM-Generated Code*, FSE Companion 2025, arXiv 2504.19037 ⚠️
- *So what:* if beginners struggle to read AI-written Python, reading AI-written C at the boundary is unlikely to be easier.

---

## 5.4 How well humans review (≈650 words)

**¶8. Closest prior art: developers can't reliably tell secure from insecure AI-generated C.**
- Khalid et al.: about 100 C-proficient developers reviewed real AI-generated C linked-list code. They couldn't reliably tell secure suggestions from insecure ones; only 22% of submissions were fully secure; participants who edited the code more produced fewer vulnerabilities. ✅ khalid2027 ⚠️ (preprint; confirm figures)
- **Differentiate explicitly** (CLAUDE.md requires it): Khalid studies pure C and uses experience as the predictor. This thesis is about the Python/C boundary and the specific L3 knowledge it requires.

**¶9. The awkward finding: experience didn't help.**
- In Khalid, developers with more than three years of experience submitted *more* vulnerabilities. ✅ khalid2027 ⚠️
- This matches older work: in Edmundson et al., experience and education didn't predict who found the vulnerabilities in a code review. ✅ edmundson2013
- **Address it head-on.** Response: *experience* is not the same as *memory-model literacy*. Years of writing Python say little about whether someone knows which calls borrow and which steal. That's why ch. 7 proposes L1/L2/L3 instead.
- Optional support: security mistakes in practice are often conceptual, not careless. ➕ Votipka et al., USENIX Security 2020 (in `prior-art-review.md`)

**¶10. Reviewers miss easy bugs when not told to look, and anchor on what an AI flags.**
- Developers missed easy vulnerabilities unless explicitly asked to look for security problems. ✅ braz2022
- Experts given an automated review focused on the locations it flagged and searched less elsewhere. ➕ Tufano et al., *Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?*, ICSE 2025, arXiv 2411.11401
- *So what:* adding an AI reviewer doesn't simply add coverage; it can narrow where the human looks.

**¶11. Tools don't settle it either.**
- Static analyzers agreed with human labels on only about 61–65% of LLM-written samples. ✅ firouzi2026 ⚠️
- Tie back to ch. 4 ¶8: someone still has to decide which reports are real.

---

## 5.5 So what (≈150 words)

**¶12. Chapter close and hand-off.**
- Pattern: AI writes code with real flaws; people over-trust it; human review is the safeguard; but review quality isn't predicted by experience, and AI help can narrow it.
- The missing variable is *understanding*: what the reviewer actually knows about the memory model.
- Hand-off sentence to ch. 6: *if verification depends on understanding, where does that understanding come from, and is AI building it or replacing it?*

---

## Checklist before this chapter counts as drafted

- [ ] Add to `refs.bib`: Zi et al. 2025, Tufano et al. 2025 (and Votipka 2020, LLM-CSEC if used)
- [ ] Pull exact figures from the originals: Pearce 2022, Perry 2023, Sandoval 2023, Khalid 2027, Zi 2025, Firouzi 2026
- [ ] Khalid's preprint status: check for the final S&P version
- [ ] The Khalid differentiation is stated in plain words, not just implied
- [ ] The "experience didn't help" finding is addressed, not buried
- [ ] Novelty wording matches CLAUDE.md exactly
