# Chapter 4: The Fixes and Where Each Stops (scaffold)

*Scaffold drafted 17 Nov 2026. Target: about 2,500 words. Each block below is one paragraph: a suggested topic sentence, the evidence that goes in it, and what still needs checking. The prose is yours to write; replace each block with your paragraph as you go.*

**Chapter claim:** Memory-safe languages, detection tools and AI security systems each shrink the memory-safety problem a great deal. None of them removes the need for people who can read and judge native code, and each one moves the human role from *writing* code to *verifying* it.

**Rule for the whole chapter:** give each fix full credit first, with its best numbers, and then its limits. A reader who uses Rust or AIxCC tools should finish each section thinking "that's fair."

**Legend:** ✅ in `refs.bib` · ➕ add to `refs.bib` · ⚠️ verify the figure against the original before keeping it

---

## 4.1 The strongest objection (≈200 words)

**¶1. State the objection at full strength.**
- *Topic sentence idea:* "The strongest objection to this thesis is that the problem is already being solved: new code can be written in memory-safe languages, and what remains can be checked by increasingly capable automated tools, including AI."
- Name the three families covered in this chapter: memory-safe languages, detection tools (sanitizers, fuzzing, hardware), AI security systems.
- Policy backs the first one: governments now ask vendors for memory-safe roadmaps. ✅ cisa2023, ✅ oncd2024
- End with the chapter's question: *does any of these remove the need for a human who understands the native layer?*

---

## 4.2 Memory-safe languages (≈900 words)

**¶2. Full credit: Rust works.**
- Android's share of memory-safety vulnerabilities fell sharply as new code moved to memory-safe languages. ✅ google2025rust ⚠️ (the "below 20%" and "1000×" figures were only seen in secondary summaries; take the numbers from Google's own post)
- Mechanism: the ownership and borrowing rules turn whole bug classes (use-after-free, double free) into compile errors.
- *So what:* for new code, this is the most effective fix available.

**¶3. Limit 1: rewriting is slow, so the old C stays.**
- Android's improvement came mainly from writing *new* code in Rust, not from replacing old C/C++. ✅ google2025rust ⚠️
- The old layer is huge and is exactly what the Python stack sits on (link back to ch. 2: CPython, NumPy, PyTorch).
- *So what:* the native core described in ch. 2 will be around for a long time.

**¶4. Limit 2: Rust still calls C.**
- `unsafe` is more common than expected in real crates, and its most common use is calling other unsafe code, including C libraries through the FFI. ✅ astrauskas2020 ⚠️ (get the exact percentages from the paper)
- Parallel: the same boundary risk shows up in scripting-language native extensions. ✅ staicu2023
- *So what:* the boundary contract (L3, ch. 7) doesn't go away. It moves to a new boundary (Rust↔C instead of Python↔C).

**¶5. Limit 3: Rust's guarantee ends where `unsafe` begins.**
- Studying every memory-safety Rust CVE up to 2020, Xu et al. find that all of them required `unsafe` code. That is good news for Rust and also the point: someone must reason correctly about the unsafe parts. ➕ xu2021 (added to `refs.bib`; verify the count of 186 bug reports)
- Google describes nearly shipping its first Rust memory-safety bug. ✅ google2025rust ⚠️
- *So what:* reasoning about `unsafe` takes the manual memory model (L2), which is the same knowledge C requires.

**¶6. Section claim.**
- Memory-safe languages shrink the problem for new code. The existing native layer and the boundaries into it still need people who can read C.

---

## 4.3 Detection tools: sanitizers, fuzzing, hardware (≈500 words)

**¶7. Full credit: sanitizers and fuzzing find memory bugs automatically and at scale.**
- AddressSanitizer and fuzzing are standard practice and catch exactly the bug classes this thesis is about.
- ➕ Need one citable source for ASan/fuzzing in practice (e.g., the original AddressSanitizer paper, USENIX ATC 2012, or Google's OSS-Fuzz). Pick one.

**¶8. Limit: tools have blind spots, and someone has to triage what they report.**
- Sanitizers fall short of their conceptual coverage because of incomplete or faulty implementations. ➕ MSET, "Evaluating the Effectiveness of Memory Safety Sanitizers," IEEE S&P 2025, doi:10.1109/SP61157.2025.00088 (in `prior-art-review.md`; **look up the authors before adding to `refs.bib`**)
- Static analyzers disagree with ground truth more often than you'd expect: only about 61–65% of CodeQL and Semgrep verdicts matched human labels on LLM-written code. ✅ firouzi2026 ⚠️
- Sanitizers only find bugs the test inputs reach.

**¶9 (optional, cut if short on space). Hardware: CHERI and MTE.**
- Hardware tagging can stop many memory errors at run time, but it is deployed on few platforms so far, and it reports errors rather than fixing them.
- ➕ Needs a source. If you don't want to chase one, cut this paragraph and mention hardware in a single sentence in ¶1.

---

## 4.4 AI security tools (≈700 words)

**¶10. Full credit, and an honest concession.**
- DARPA's AI Cyber Challenge finals (Aug 2025): systems found 54 of 63 planted vulnerabilities (86%) and patched 43 (68%), up from 37% / 25% in the 2024 semifinals. They also found 18 real vulnerabilities in open-source code. ✅ darpa2025aixcc ⚠️ (use DARPA's corrected figures)
- **Concession to state plainly:** the systems did *better* on C than on Java (30 of 40 fuzzable C vulnerabilities vs. 4 of 23 Java). Memory-safety bugs in C are among the *most* automatable bug classes. ⚠️ (from `notes/the-ai-question.md`; confirm in DARPA's materials)
- *Why the concession helps you:* it shows the argument isn't "humans find bugs better than machines." The argument is about who judges the findings and fixes.

**¶11. Limit 1: much of the success was fuzzing, not AI.**
- About half the planted vulnerabilities (34 of 63) and patches (31 of 63) were solvable by parallel fuzzing alone under lab conditions; the AI-specific contribution was narrower. ✅ darpa2025aixcc ⚠️

**¶12. Limit 2: the strongest systems still keep a human in the loop.**
- Patches that passed automated checks still needed manual review for semantic errors. ✅ darpa2025aixcc ⚠️
- DeepMind's CodeMender: every patch is reviewed by a human before it's submitted upstream. ✅ deepmind2025codemender (confirm the post title)
- Optional: Google's Big Sleep found a SQLite bug before release. ➕ needs a source; cut if you don't find the original post.

**¶13. Limit 3: AI also *writes* native code, which adds to the review load.**
- Short bridge to ch. 5: AI assistants produce insecure code at measurable rates, and people trust it too much. ✅ perry2023, ✅ pearce2022
- *So what:* the same technology that helps find bugs also produces more code that needs checking.

---

## 4.5 Synthesis: every fix moves the human from writer to verifier (≈200 words)

**¶14. Chapter close and hand-off.**
- Pattern across all three families: each fix is real, and each relocates the human role rather than removing it. Rust leaves `unsafe` and the FFI to someone who knows the manual model. Sanitizers and fuzzers leave triage. AI tools leave patch review.
- Verifying a fix takes at least as much understanding as writing it (preview of L2/L3 in ch. 7).
- Preview Bainbridge (ch. 6): the more automated the system, the more it depends on rare human skill for the cases automation misses. ✅ bainbridge1983
- Hand-off sentence to ch. 5: *if the human role is now verification, how well do people verify code they didn't write, especially AI-written code?*

---

## Checklist before this chapter counts as drafted

- [ ] Pull exact figures from the originals: Google 2025 (Android), Astrauskas 2020 (unsafe usage), Xu 2021, DARPA AIxCC
- [ ] Add MSET to `refs.bib` (authors) and one ASan/fuzzing source
- [ ] Decide: keep or cut ¶9 (hardware) and the Big Sleep mention
- [ ] Every section opens with credit, then limits
- [ ] Check the chapter against the spine: does each section end on "a human who understands the native layer is still needed"?
