# Chapter 1: Introduction (scaffold)

*Scaffold drafted 17 Nov 2026. Target: about 1,200 words. Each block below is one paragraph: a suggested topic sentence, what goes in it, and what still needs checking. The prose is yours to write.*

**Write this chapter last** (planned for the week of 8–14 Dec). An introduction promises what the thesis delivers, so it's easiest to write once chapters 2–9 exist. Sketching it now is fine; expect to rewrite it.

**Chapter claim:** AI and high-level languages have made software accessible, but the stack underneath is still C/C++, and someone has to be able to check it. This thesis asks what human understanding that takes and how to keep it.

**Rule for the whole chapter:** lead with the stakes and the data, then AI. Keep personal experience to motivation, never evidence.

**Legend:** ✅ in `refs.bib` · ➕ add to `refs.bib` · ⚠️ verify the figure against the original before keeping it

---

## 1.1 The hook (≈250 words)

**¶1. Open with the contrast.**
- *Topic sentence idea:* "It has never been easier to build software: a few lines of Python, or a prompt to an AI assistant, can produce a working program. Underneath, almost all of it still runs on C and C++."
- One concrete image: a data scientist's NumPy call, or an AI-generated script, running on a C core (preview of ch. 2's numbers: NumPy 55.7% native by our count; state the rule or save it for ch. 2).

**¶2. Why that matters now.**
- Memory-safety bugs are the largest class of serious vulnerabilities (≈70% at Microsoft and in Chromium; preview of ch. 3). ✅ miller2019, ✅ chromium2020
- Governments now ask for memory-safe roadmaps. ✅ cisa2023, ✅ oncd2024
- AI writes more of the code, and people using AI assistants can write less secure code while feeling more confident. ✅ perry2023

---

## 1.2 The question (≈300 words)

**¶3. The guiding question.**
> As AI becomes increasingly capable of writing and debugging software, what happens when both the developer and the AI are working with abstractions built on lower-level systems that the developer doesn't understand?

- One sentence on where it came from (motivation only): classmates fluent in libraries but unable to picture what's underneath, told as a story about the system, not the people; and *"I use AI daily to deepen my understanding, which raised the question of when it builds understanding and when it replaces it."*

**¶4. The research question this thesis answers.**
> To what extent can automated tools, including AI, replace human systems-programming expertise in keeping native-code dependencies memory-safe?

- Note it's answered from the literature, not a new study (ch. 8 proposes the studies).

**¶5. Stance.**
- Pro-AI. The question isn't whether to use AI or Python. It's what human understanding is needed to oversee them when something goes wrong beneath the abstraction.
- The claim is about the ecosystem, not individuals: not every developer needs to understand C.

---

## 1.3 The argument in brief (≈350 words)

**¶6. Thesis statement.** Use the current version from `thesis-outline.md` (decide first whether "maintainability" stays):
> Although high-level programming languages and AI-assisted development have made software creation increasingly accessible, their reliance on underlying native-code implementations introduces persistent memory-safety challenges. The long-term security and maintainability of these systems depend not only on improvements in automated tools but also on preserving the systems-programming expertise necessary to identify, understand, and remediate vulnerabilities within their underlying C and C++ components.

**¶7. The core claim in one paragraph.**
- Not every developer needs to understand the C layer, but the ecosystem needs enough specialists who do, because someone must be able to check and fix what the tools produce.
- Every fix (Rust, detection tools, AI) moves the human role from *writing* native code to *verifying* it (preview of ch. 4).
- The route into that expertise is narrowing, and AI can either build understanding or replace it depending on how it's used (preview of ch. 6).

**¶8. The contribution.**
- A framework, memory-model literacy at three levels (L1 managed, L2 manual, L3 boundary contract), that names the gap (ch. 7).
- A proposed research agenda to test it, with conditions under which the claim would be wrong (ch. 8).
- Novelty, worded carefully: "We found no prior evaluation of the security of LLM-generated Python/C API code." Nothing stronger.

---

## 1.4 Roadmap (≈200 words)

**¶9. Chapter-by-chapter.** One sentence each:
- Ch. 2: the C/C++ core under high-level software, and the boundary where bugs cluster.
- Ch. 3: why memory safety matters and where garbage collection's guarantee stops.
- Ch. 4: what memory-safe languages, detection tools and AI security systems fix, and where each stops.
- Ch. 5: AI-written code and the limits of human review.
- Ch. 6: how systems expertise forms and how automation can erode or build it.
- Ch. 7: the L1/L2/L3 framework.
- Ch. 8: proposed studies.
- Ch. 9: a normative closing on AI as augmentation, not replacement.
- Ch. 10: limitations.

---

## Checklist before this chapter counts as drafted

- [ ] Written after chapters 2–9 exist, so every promise matches what the thesis delivers
- [ ] Thesis statement final (the "maintainability" decision made)
- [ ] Every figure here repeats one stated, with its source, in a later chapter
- [ ] Personal experience appears only as motivation
- [ ] Ask your English professor to read this chapter for clarity
