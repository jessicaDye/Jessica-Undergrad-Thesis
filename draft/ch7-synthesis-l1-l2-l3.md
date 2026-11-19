# Chapter 7: Synthesis: Memory-Model Literacy, L1/L2/L3 (outline)

*Outline drafted 19 Nov 2026. Target: about 1,500 words.*

**This is a lighter outline on purpose.** Chapter 7 pulls together chapters 2–6, so its exact arguments depend on how those chapters come out in your writing. Below are the pieces, the order, and the questions each section has to answer. Write it after chapters 2–6 are drafted, and turn this into a paragraph scaffold then if you want one.

**Chapter claim:** Chapters 2–6 point to one specific gap in understanding, which this framework names. Most developers can work at L1 with AI help; the ecosystem needs a smaller group at L2/L3.

**Legend:** ✅ in `refs.bib` · ➕ add to `refs.bib`

---

## Pieces, in order

**7.1 The framework (≈350 words)**
- The table (copy from `thesis-outline.md`): L1 managed model, L2 manual model, L3 boundary contract, each with an example question.
- Present it as a framework built from the literature, not a tested instrument.
- Supporting claim: **L3 depends on L2 and can't be inferred from L1 alone.**
- Framing line: reference counting *is* CPython's garbage collector. At the boundary, its bookkeeping becomes the programmer's job.

**7.2 The motivating example (≈300 words)**
- The tuple-packing refcount bug (`PyTuple_SET_ITEM` stealing a borrowed reference from `PyList_GET_ITEM`). Code and explanation are in `paper/main.tex`.
- What tools did and didn't catch: cppcheck and clang-tidy silent, release CPython crashed with no diagnostic, only a debug build and AddressSanitizer exposed it.
- Say it's one hand-written example, not evidence about AI.

**7.3 Mapping chapters 2–6 onto the levels (≈450 words)**
Questions to answer, one short paragraph each:
- Ch. 2: which level does the boundary bug taxonomy (Yang & Cai, Hu & Zhang) require? *(Mostly L3.)*
- Ch. 3: which garbage-collection limits are L2 problems and which are L3?
- Ch. 4: why does reasoning about Rust's `unsafe` and FFI need L2, and the Rust↔C boundary need its own L3?
- Ch. 5: does reviewers' failure (Khalid, Edmundson) look like missing *experience* or missing L2/L3?
- Ch. 6: which level do notional-machine and threshold-concept research describe, and which level is the epistemic-debt repair task testing?

**7.4 The strongest counterargument (≈250 words)**
- "Only a few specialists need L3, like mechanics and drivers."
- Agree first: most developers don't need L3. That's the claim.
- Then: the claim is about having *enough* specialists. Chapters 5–6 suggest supply is at risk while AI increases the amount of code that needs checking.
- Informal support: Spolsky's "Law of Leaky Abstractions." ✅ spolsky2002 (cite as an essay, not research)

**7.5 So what (≈150 words)**
- The framework makes the claim testable. Hand-off to ch. 8.

---

## Sources likely used
✅ yangcai2026, ✅ huzhang2023, ✅ staicu2023, ✅ astrauskas2020, ✅ xu2021, ✅ khalid2027, ✅ edmundson2013, ✅ spolsky2002, ➕ Sorva 2013, ➕ Kyriakou 2025, ➕ Epistemic Debt

## Before drafting
- [ ] Chapters 2–6 drafted (at least roughly)
- [ ] Decide whether to keep 7.3 as five short paragraphs or one table plus a short paragraph
