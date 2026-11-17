# Chapter 3: Why Memory Safety Keeps Coming Back (scaffold)

*Scaffold drafted 17 Nov 2026. Target: about 1,800 words. Each block below is one paragraph: a suggested topic sentence, the evidence that goes in it, and what still needs checking. The prose is yours to write; replace each block with your paragraph as you go.*

**Chapter claim:** Memory-safety bugs are still the largest class of serious vulnerabilities, and governments now treat them as a policy problem. Garbage collection solves a great deal, but it relocates the problem to the boundary and the runtime rather than eliminating it.

**Rule for the whole chapter:** in 3.3, give garbage collection full credit before its limits. The section should read as "GC is a great idea with a boundary," not "GC doesn't work."

**Legend:** ✅ in `refs.bib` · ➕ add to `refs.bib` · ⚠️ verify the figure against the original before keeping it

---

## 3.1 The numbers (≈450 words)

**¶1. What a memory-safety bug is.**
- *Topic sentence idea:* "A memory-safety bug happens when a program reads or writes memory it shouldn't: past the end of a buffer, after the memory has been freed, or through a pointer that was never valid."
- Name the main types in plain words: buffer overflow, use-after-free, double free, null dereference. These are the bugs C and C++ allow and managed languages prevent.
- *So what:* the reader needs these terms for every later chapter.

**¶2. They're the largest class of serious vulnerabilities.**
- Microsoft: about 70% of the vulnerabilities it patches each year are memory-safety issues. ✅ miller2019 ⚠️ (confirm the talk title and exact wording)
- Chromium: about 70% of high-severity security bugs are memory-safety problems. ✅ chromium2020 ⚠️
- **Say this explicitly:** Microsoft counted patched CVEs and Chromium counted high-severity bugs, so these are similar findings from different measurements, not the same number twice.
- Optional: the CWE Top 25 ranks memory-safety weaknesses near the top. ➕ (cite the current year's list, or cut)

**¶3. One example that makes it concrete.**
- Heartbleed (2014): a missing bounds check in OpenSSL, a C library underneath much of the web, leaked server memory. ➕ one source (e.g., the CVE entry or a short technical account)
- *So what:* one small C mistake in a shared library can affect software written in any language.

---

## 3.2 Policy has noticed (≈400 words)

**¶4. Governments now ask for memory-safe roadmaps.**
- NSA 2022, *Software Memory Safety* guidance. ➕
- CISA, NSA, FBI and partners 2023, *The Case for Memory Safe Roadmaps*: software manufacturers should publish plans to move to memory-safe languages. ✅ cisa2023
- White House ONCD 2024, *Back to the Building Blocks*. ✅ oncd2024
- *So what:* memory safety is no longer just a technical concern; it's national policy.

**¶5. What the guidance does and doesn't address.**
- The guidance is aimed at **software manufacturers** and their development practices. **Don't claim it exempts scientific or ML software; it doesn't.** It has no category carve-outs.
- What it says little or nothing about: training, curriculum and the workforce who will read and maintain the code during a migration that will take years. (Check this against the documents before stating it; quote what they do say about workforce, if anything.) ⚠️
- Much of the scientific/ML stack from ch. 2 is community-maintained open source, not a "manufacturer" with roadmap obligations, so the pressure lands unevenly.
- *So what:* this silence is the gap the thesis speaks to. Hand-off to ch. 6.

---

## 3.3 What garbage collection solves and where it stops (≈800 words)

**¶6. Full credit: garbage collection is one of computing's great safety wins.**
- GC eliminates use-after-free and double free in managed code, makes programming far more accessible, and makes memory-safe languages practical; modern collectors are fast. ➕ Jones, Hosking & Moss 2023, *The Garbage Collection Handbook* (2nd ed.); ➕ Hertz & Berger 2005 (GC performance)
- *Topic sentence idea:* "Garbage collection is the reason most programmers today never think about freeing memory, and that is a genuine achievement."

**¶7. In CPython, reference counting *is* the garbage collector.**
- CPython frees most objects by counting references to them, with a cycle detector as backup. ➕ cite the CPython documentation
- Inside Python this is invisible. At the boundary (ch. 2), C code has to do the counting by hand.
- Key line for the section: **"Garbage collection does not eliminate memory-related vulnerabilities; it relocates them."**

**¶8. Where the guarantee stops (1): native code sits outside it.**
- C extensions, ctypes/cffi and the buffer protocol bypass the collector. ✅ staicu2023; link back to Yang & Cai's reference-counting bugs in ch. 2.

**¶9. Where the guarantee stops (2): the runtime itself is C.**
- CPython, including the collector, is written in C, so a bug in the runtime is a memory bug. ➕ needs a source (e.g., a CPython memory-safety CVE)

**¶10. Where the guarantee stops (3) and (4): leaks and edge cases inside managed code.**
- References kept alive by mistake (caches, globals, closures) cause unbounded memory growth, which is a reliability and denial-of-service risk. ➕ needs a source
- Reference cycles, finalizers (`__del__`) that resurrect objects, and callbacks that run mid-operation. ➕ needs a source (the CPython docs on `gc` and finalization may be enough)
- *Option if sources are thin:* merge ¶9–10 into one paragraph and keep only what you can cite.

**¶11. Where the guarantee stops (5): concurrency is changing the rules.**
- Free-threaded CPython (PEP 703, Python 3.13+) changes how reference counting works under threads; extensions written for the GIL era can break. ➕ PEP 703 ⚠️

**¶12. Section claim.**
- The managed guarantee is real and valuable, and it stops at a boundary. Everything past that boundary depends on someone who understands manual memory management.

---

## 3.4 So what (≈150 words)

**¶13. Chapter close and hand-off.**
- Memory-safety bugs are the biggest problem, policy says fix them, and the managed-language guarantee stops at exactly the seam from ch. 2.
- Hand-off to ch. 4: *the field's answer is a set of fixes: memory-safe languages, detection tools and AI. How far does each get us?*

---

## Checklist before this chapter counts as drafted

- [ ] Confirm the Microsoft and Chromium figures and wording in the originals
- [ ] Add NSA 2022, the GC Handbook, Hertz & Berger, PEP 703, CPython docs and a Heartbleed source to `refs.bib`
- [ ] Read what CISA 2023 and ONCD 2024 actually say about workforce and training before claiming silence
- [ ] Decide whether ¶9–10 stay separate or merge, depending on sources
- [ ] Check that 3.3 gives GC full credit before its limits
