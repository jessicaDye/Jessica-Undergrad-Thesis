# Theoretical Grounding — Two Kinds of Transfer

Drafted 28 Aug 2026. Jessica's observation — having done data structures in C++, she understood memory management in Algorithms where classmates did not — is a documented phenomenon with 35 years of literature. Connecting to it is the biggest available upgrade: theoretical grounding is what undergrad submissions lack and reviewers ask for.

## Three literatures that apply

### 1. Notional machines — the frame

A **notional machine** is the abstract model of execution a learner uses to reason about code. Canonical: Sorva, *Notional Machines and Introductory Programming Education* (ACM TOCE 2013). Still active — recent TOCE work on notional machines and perception.

Reframes the whole thesis:

> Python's notional machine does not include memory allocation. A student whose only notional machine is Python's has no model in which "who owns this memory" is a question that can be asked. Low-level coursework installs a different notional machine — and that model, not the syntax, is what transfers.

Also reframes the AI question: **AI assistance can supply code but does not install a notional machine.** Connects directly to the epistemic-debt finding — output without a model.

### 2. Aliasing misconceptions — the closest empirical study

*Student Understanding of Aliasing and Procedure Calls* (SPLASH-E 2017, Brown). Four quizzes, two courses: 32 upper-level (Java), 42 intro (Pyret).

- ~**30% of upper-level students answered incorrectly**; half the class missed ≥1 question
- "Even upper-level students suffer from difficulties that instructors might have assumed have long since been addressed"
- Named misconceptions: **Assignment by Copy**, **Bidirectional Assignment**
- Explicit vocabulary instruction didn't stick — only 3 students used "alias" in final explanations despite emphasis

This is exactly the confusion Jessica watched. Documented, persistent, instruction-resistant. Her hypothesis (prior manual-memory experience inoculates) is a natural unanswered follow-on. Also see *From State to Structure: Towards Abstraction Support in CS2* (Koli Calling 2025).

### 3. Transfer of learning between languages — where the title is hiding

Scholtz & Wiedenbeck, *Learning Second and Subsequent Programming Languages: A Problem of Transfer* (IJHCI 1990) established the frame. Active since: *Semantic Transfer in Programming Languages* (**ITiCSE 2020** — target venue), *Teachers' Views on Teaching Second and Subsequent Programming Languages* (ICER 2021), *Here We Go Again* (CACM 2022).

**"Transfer" does double duty:** institutional transfer (CC→university) and transfer of learning (C++→Python). The claim is that the first produces conditions for the second. Accurate, not cute. Candidate title: ***Two Kinds of Transfer***.

## The complication — engage it directly

The transfer literature documents **negative transfer**: prior language knowledge that interferes. C++→Python can carry wrong assumptions about copying semantics, `=`, object destruction. "Prior C++ helps" is NOT what the literature says.

Defensible narrower version:

> Manual memory management installs a notional machine that includes allocation and ownership. That model is *additive* with respect to Python's — it supplies a layer Python's model omits entirely, rather than contradicting it. Negative transfer is most documented where two languages give the same construct different semantics; the memory model is a case where one language is silent rather than different.

Tells us what to measure: not "did C++ students do better overall" but "did they reason correctly about aliasing, ownership, and mutation."

## Two-part study structure

- **Part 1 (now):** curriculum audit — where does the machine model appear, does the transfer pathway reach it earlier?
- **Part 2 (future work):** concept inventory measuring whether students with prior low-level coursework reason differently about aliasing/ownership/mutation.

Part 2 needs IRB + student access — not this paper. **But proposing it earns real credit**: shows she knows the difference between a structural finding and a learning claim. The SPLASH-E quizzes are an instrument to adapt, not build. Possible follow-on paper if the advisor teaches a relevant course.

## Caution about her own case — confounded

- **Curricular:** C++ in CS I/II/data structures, required assembly + architecture, Java pre-transfer, Python post
- **Dispositional:** converted a vintage Windows 7 all-in-one to Linux Mint, learned C and shell scripting doing it

A reviewer will say the second explains as much as the first — the advantage came from being the kind of student who does that, not the curriculum. **They'd have a point.** Her own case can't separate these; another reason the argument must rest on curricular structure across institutions.

Keep the positionality statement to the curricular pathway. The Linux Mint story belongs in a talk, not a methods section.

## Detail worth chasing — the CIS wrinkle

She was a **CIS student on a CS-heavy track**, not a CS major. Possibly a finding, not a footnote: if CIS/IT associate tracks require systems and architecture coursework that CS-major tracks at four-years treat as optional, the low-level exposure is surviving in programs the field regards as *less* rigorous.

**Add to the audit:** code the associate-degree type (CS transfer / CIS / IT) alongside requirements. Costs nothing extra; may be the most interesting column.

## Reading order (~1 week, parallel with SRC repo work)

1. Sorva (TOCE 2013) — the frame
2. Aliasing and Procedure Calls (SPLASH-E 2017) — closest study + usable instrument
3. Semantic Transfer (ITiCSE 2020) — shows what target-venue reviewers value
4. Here We Go Again (CACM 2022) — accessible overview
5. Scholtz & Wiedenbeck (1990) — cite for lineage
