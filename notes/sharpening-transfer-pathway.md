# Sharpening the Angle — The Transfer Pathway

Drafted 28 Aug 2026. Problem: AI-and-CS-education is the most crowded topic at SIGCSE/ITiCSE. Solution: the community-college transfer pathway.

## The angle

Jessica's own path — C/C++ at community college → Java → Python after transfer — describes a **naturally occurring variation in curricular sequence**, produced at institutional scale, in a population CS-ed research has studied on nearly every dimension except this one.

**Verified:** California's CS Transfer Model Curriculum requires **C-ID COMP 142 — Computer Organization and Assembly Language** as one of five required computing courses in its 28-unit core. Every CS Associate Degree for Transfer student in California takes assembly in the lower division, before arriving at the university. Four-year programs vary widely in whether architecture is required, when, and whether it's electively satisfiable — all publicly documented.

**Testable structural claim:** transfer-pathway students may encounter the machine model *earlier and more reliably* than native four-year students. If so, transfer students arrive better prepared in exactly the dimension industry says is scarce.

## Why it's the strongest available

1. **Inverts a deficit narrative.** The canonical paper — *Experiences of Computer Science Transfer Students* (ICER 2018, Kwik & Ko, UW; 160 surveyed, 8 interviewed) — found transfer students more diverse (44% first-gen, older, lower SES) with "transfer shock," 78% higher likelihood of GPA drop. Deficit-leaning. **And it does not discuss programming languages or curricular content at all** — checked specifically. The field's main paper on this population never asked what they were taught. Clean, specific gap.
2. **Escapes the AI crowd.** Curriculum-structure + transfer-pathway paper; AI enters in discussion as why stakes changed, not as subject.
3. **Two reviewer constituencies** — systems curriculum *and* broadening participation / transfer equity, both standing SIGCSE/ITiCSE priorities.
4. **Public, standardized data.** C-ID gives statewide common course identifiers — rigor most undergrad curriculum studies can't reach.

## Correction before getting attached

**Don't assume CCs teach C++ first.** Orange Coast College's CS1 (CS A122, COMP 122) specifies only "a high-level language"; its **CS2 is Data Structures in *Python***. Python and Java are alternative entry points. The intro-language hypothesis may no longer hold even where it held when Jessica took those courses — check, don't assume. If it changed, that's a finding.

**The durable difference is the required lower-division architecture/assembly course, not the intro language.** Reframe the question from "which language first" to **"at what point in the sequence does the machine model appear, and is it required or avoidable?"**

## Using the personal experience honestly

- **It's a hypothesis source, not a finding.** n=1, retrospective, motivated. Cannot support claims about transfer students generally.
- **But it belongs in the paper** via a brief **positionality statement** in methods — standard convention in qualitative/curricular CS-ed research. E.g. *"the first author completed a community-college-to-university transfer pathway in which low-level programming preceded Python, which motivated this study's research questions."* Discloses bias, explains why she noticed the variable, gains credibility. Check venue conventions with advisor.

*Experience earns the question; data has to earn the answer.*

## Revised study

**RQ:** At what point in the undergraduate sequence does required coursework in computer organization and assembly appear, and does it differ systematically between CC transfer pathways and native four-year pathways?

**Sample:** California as natural frame (C-ID comparability, documented CSU/UC transfer structure). 15–20 community colleges paired with their most common transfer destinations. If time allows, add a contrast state without statewide articulation — tests whether the effect is about transfer pathways generally or California's structure specifically.

**Code per program:** architecture/assembly required / elective / absent; lower vs upper division; satisfiable by a course with no low-level component?; CS1 language; CS2 language; any required manual-memory-management coursework.

**The comparison that makes the paper:** per transfer pairing, does the student meet the machine model earlier via the CC than they would have as a native student at the destination? Report the distribution — the interesting result may be variance, not a clean gap.

Same effort as the earlier generic audit, much sharper question, still IRB-free.

## Three secondary sharpeners

- **Historical precedent (cheap).** Assembly/Pascal → C → Java (late 90s) → Python; same argument each time. Spolsky's 2005 "Perils of JavaSchools" is the practitioner version. Half a page. **Cite Spolsky as a primary source documenting a position, not as evidence** — it's an opinion essay.
- **International contrast (high value, higher cost).** ITiCSE 2027 is in Glasgow; reviewers there dislike US-only framing. Many European/Asian programs still teach C early. 5–6 non-US programs would broaden reach. Only if the primary audit finishes early — a shallow section is worse than none.
- **Verification framing → curricular proposal.** Almost no undergrad curriculum teaches *code review of unfamiliar low-level code* as a distinct skill. Recommendation becomes "teach reading and auditing native code," not "teach more C." Position papers often lack actionable recommendations; reviewers ask for them.

## Plan impact

- **SRC (30 Sept):** still lead with repository data (Studies 1–2). Transfer angle too large for five weeks.
- **ITiCSE 2027 (January):** transfer audit is the centerpiece; repository data becomes motivation — *here's how much native code exists and how fast it grows; here's where students meet it; here's a pathway that reaches it earlier than the one we treat as standard.* Not an AI paper. Much less crowded lane.

## Honest risks

- **The effect may not exist.** Four-years may require architecture just as reliably, only later. Report a null — SIGCSE welcomes null results — but don't let the story's appeal pull the coding.
- **California may not generalize.** C-ID is unusually structured. Frame as California's articulated pathway unless a contrast state is added; say so plainly.
- **Transfer research has its own experts.** Read the ICER 2018 paper properly and check what has cited it — that's the related-work spine.
- **Biggest failure mode: confirming her own experience.** Pre-register the coding scheme with the advisor before starting; have a second coder do ~20% and report an agreement statistic. Addresses the objection before it's raised.
