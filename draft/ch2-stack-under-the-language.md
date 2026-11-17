# Chapter 2: The Stack Under the Language (scaffold)

*Scaffold drafted 17 Nov 2026. Target: about 1,500 words. Each block below is one paragraph: a suggested topic sentence, the evidence that goes in it, and what still needs checking. The prose is yours to write; replace each block with your paragraph as you go.*

**Chapter claim:** Software that looks memory-safe from the outside runs on a large C/C++ core. The point where Python hands off to that core is where the bugs concentrate.

**Rule for the whole chapter:** lead with the data. This chapter is the evidence base the rest of the thesis stands on, so keep AI out of it except for one forward-pointing sentence at the end.

**Legend:** ✅ in `refs.bib` · ➕ add to `refs.bib` · ⚠️ verify the figure against the original before keeping it

---

## 2.1 What "Python" actually runs on (≈450 words)

**¶1. The layers under a high-level program.**
- *Topic sentence idea:* "When a developer writes a few lines of Python to train a model or analyze data, most of the code that actually runs was written in C or C++."
- Walk down the stack: the Python program → libraries like NumPy and PyTorch → the CPython interpreter → system libraries such as OpenSSL and libc. One sentence on the same pattern elsewhere: JavaScript engines in browsers and Node are C++.
- *So what:* the language a developer writes in isn't the language most of their program is written in.

**¶2. How much of it is native code.**
- Our own counts (Aug 2026; lines classified by file extension, vendored code excluded): **NumPy 55.7%, CPython 47.4%, PyTorch 34.5%** C/C++.
- Hu & Zhang measured NumPy at **55.5%** in 2019 with a different method. Two independent measurements seven years apart give nearly the same number. ✅ huzhang2023 (Table II in the SANER 2020 version; see `notes/hu-zhang-2020-digest.md`) ⚠️
- Yang & Cai report **38%** for NumPy under their own counting rule. State both rules; the point holds under either. ✅ yangcai2026
- *Careful:* don't compare PyTorch numbers across studies. Hu & Zhang's PyTorch was a 2018 version a fraction of today's size.
- *So what:* this isn't a thin wrapper. Roughly a third to a half of these projects is native code.

**¶3. Native bugs are reachable from Python.**
- Fuzzing ML frameworks *through their Python APIs* found memory-safety bugs in their C/C++ cores (null dereferences in PyTorch, an out-of-bounds read in h5py's HDF5 core). ➕ *Python Fuzzing for Trustworthy ML Frameworks*, arXiv 2403.12723 ⚠️ (an existence proof, not a rate)
- A real example of severity: CVE-2024-31580, a heap buffer overflow in PyTorch's C++ runtime, rated High (CVSS 8.7), fixed in 2.2.0. ➕ cite the NVD entry ⚠️
- *So what:* a Python developer can trigger a C memory bug without writing a line of C.

---

## 2.2 The boundary is where it breaks (≈700 words)

**¶4. What the Python/C boundary is.**
- C extensions, ctypes and cffi are how Python calls native code. At that point the C code takes on obligations the Python runtime normally handles: counting references, setting exceptions, freeing memory with the right allocator. ✅ huzhang2023
- Introduce the vocabulary you'll need in ch. 7: **new, borrowed and stolen references**, exception state, allocator families. One sentence each, in plain words.
- *So what:* the boundary is a contract, and breaking it is a memory bug.

**¶5. What goes wrong there: the evidence.**
- Yang & Cai studied 1,039 confirmed native-bug fixes across 200 Python-C projects and analyzed 216 in depth. ✅ yangcai2026 ⚠️ (preprint; check for an archival version)
  - How the bugs showed up: reference counting in **41.7%**, foreign-object handling in **31.5%**, cross-language exception handling in **31.5%**.
  - Root causes: memory safety in **29.2%**, mostly reference-count misuse and null dereference.
  - In **52.8%** of cases, the main obstacle to automated detection was the semantic difference between the two languages. (Save this for ch. 4: it's a reason tools struggle here.)
- *So what:* these aren't ordinary C mistakes. They're violations of the boundary contract.

**¶6. Why developers get it wrong: the training gap, in the literature's own words.**
- Hu & Zhang's 10 bug patterns, illustrated with real defects in Pillow. ✅ huzhang2023
- Their explanation of a missed `Py_DECREF`: it's "often missed by developers because they need not do this in pure Python code." (Quote it; it's the closest published statement of your thesis, written by software-engineering researchers with no interest in curriculum.) ⚠️ check page number
- *So what:* the knowledge Python training doesn't require is exactly the knowledge the boundary demands.

**¶7. The boundary itself is the risk, not just C.**
- In a large GitHub study, vulnerability proneness in multilingual code tracked the *interfacing mechanism*, not the individual languages. ✅ lilicai2022
- Native extensions break the scripting language's safety guarantees (Node.js, Python, Ruby). ✅ staicu2023
- *So what:* using a safe language for most of a project doesn't make the seams safe.

---

## 2.3 The same pattern in ML bindings (≈200 words)

**¶8. Bindings are a growing, under-studied boundary.**
- ML frameworks expose C++ cores to many languages through bindings, and the bindings themselves introduce bugs. ➕ pick one or two of A5–A9 in `notes/annotated-abstracts-v1.md` (e.g., the 1,000-bug deep-learning framework study, A7)
- No benchmark covers LLM generation of language bindings, and LLMs frequently mishandled shared-pointer ownership in generated binding code. ✅ ompl2026 ⚠️ (preprint)
- *So what:* as more binding code is generated rather than hand-written, the boundary grows.

---

## 2.4 So what (≈150 words)

**¶9. Chapter close and hand-off.**
- The code most developers never see is the code everything depends on, and the seam into it is where bugs cluster.
- Hand-off to ch. 3: *why does this matter so much? Because memory-safety bugs are the largest class of serious vulnerabilities, and the managed-language guarantee stops at exactly this seam.*

---

## Checklist before this chapter counts as drafted

- [ ] Recount or re-confirm our NumPy/CPython/PyTorch figures and write the counting rule into ¶2
- [ ] Confirm Hu & Zhang's Table II numbers and the `Py_DECREF` quote's page in the original
- [ ] Yang & Cai: check for an archival version; confirm percentages
- [ ] Add the fuzzing paper (arXiv 2403.12723), the CVE entry and one bindings study to `refs.bib`
- [ ] Keep AI out of this chapter except the hand-off
