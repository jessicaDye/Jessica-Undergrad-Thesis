# Research Design — Measuring the Native Core (with pilot data)

Pilots run 26 Aug 2026 against public repos at HEAD. All four designs are reproducible, need no IRB, and survey nobody. Script: `langshare.py`.

**Design change from earlier advice:** I previously said the curriculum audit was the long pole and to start it within a week. After running pilots, **Study 1+2 is the better SRC contribution** — faster, cleaner, more novel. Curriculum audits are a populated CS-ed genre; native-core growth trajectory is not. Move the audit to the ITiCSE paper.

## Study 1 — Composition of the native core (PILOTED)

Classify files by extension into native (C/C++/CUDA/asm/Fortran), Cython, Python; count lines; report with and without vendored trees.

| Package | Native LOC | Cython | Python | Native % | Native+Cython % |
|---|---|---|---|---|---|
| NumPy | 358,921 | 15,526 | 269,748 | **55.7%** | 58.1% |
| CPython | 1,045,775 | — | 1,161,559 | **47.4%** | 47.4% |
| PyTorch | 1,454,681 | — | 2,759,908 | **34.5%** | 34.5% |
| pandas | 5,145 | 54,539 | 704,612 | 0.7% | 7.8% |
| scikit-learn | 8,408 | 21,728 | 435,682 | 1.8% | 6.5% |
| h5py | 1,165 | 14,439 | 20,899 | 3.2% | **42.7%** |

Excl. vendored. PyTorch → 38.7% incl. vendored; contains 111,842 LOC CUDA, 11,207 assembly.

**The stack is heterogeneous — this is a gift, not a problem.** "It's all C underneath" is false and a reviewer would dismantle it. Sharper claim: *the native core is concentrated in foundational layers; packages students touch daily are thin Python veneers over NumPy and CPython, which are ~half native. The abstraction is layered, so the distance to the memory-unsafe substrate is more than one hop and correspondingly more invisible.*

h5py shows in-repo composition **systematically undercounts** — 3.2% native in-repo, 42.7% with Cython, and it wraps HDF5 (external C entirely).

Effort: 2–3 days.

## Study 2 — Is the native core growing? (PILOTED) ← headline finding

NumPy across release tags:

| Release | Date | Native LOC | Native % |
|---|---|---|---|
| v1.10.0 | Oct 2015 | 243,360 | 57.4% |
| v1.13.0 | Jun 2017 | 261,267 | 56.7% |
| v1.16.0 | Jan 2019 | 270,088 | 55.2% |
| v1.19.0 | Jun 2020 | 278,538 | 53.5% |
| v1.22.0 | Dec 2021 | 305,157 | 52.6% |
| v1.25.0 | Jun 2023 | 333,684 | 53.6% |
| v2.0.0 | Jun 2024 | 343,411 | 54.4% |
| v2.3.0 | Jun 2025 | 349,220 | 54.1% |
| v2.5.0 | Jun 2026 | 355,371 | 55.9% |

Over 11 years in which Python became the dominant teaching language, NumPy's native code grew **+46% absolute** and held ~53–57% share. It did not shrink. Directly answers "isn't C a shrinking domain?" with own data. Run across 4–5 packages → the figure that carries the paper.

Effort: 2–3 days. Full clones are large; budget disk.

## Study 3 — Who maintains it? (PILOTED)

NumPy, commits since Jan 2021:

| | Distinct authors | Top-10 share of file-touches |
|---|---|---|
| Native (.c/.h/.cpp/.cu) | 272 | **72.4%** |
| Python (.py) | 778 | 55.0% |

Native code maintained by <half as many people, far more concentrated; one contributor >25% of native file-touches. Variant of established bus-factor methodology — cite and adapt, don't invent.

**Do NOT infer individual contributors' educational backgrounds** — unreliable, privacy problem, ethics reviewers will object. Aggregate concentration is defensible and sufficient.

Effort: 1–2 days.

## Study 4 — Where do vulnerabilities live? (NOT piloted — sandbox network blocked)

OSV.dev, free, no API key: `POST https://api.osv.dev/v1/query` with `{"package":{"name":"numpy","ecosystem":"PyPI"}}`. Classify by CWE against memory-safety set (119, 120, 121, 122, 125, 415, 416, 476, 787, 190). Strong version: follow each advisory to its fixing commit, record **file extensions changed** — that directly links vulnerability to language.

**Must engage:** *An empirical study of the Python/C API on evolution and bug patterns* (JSEP 2023) — close to this territory, read early; differentiation is that it asks SE questions and you ask what the answers mean for curriculum. Also *Empirical analysis of security vulnerabilities in Python packages* (EMSE 2022).

Effort: 1–2 weeks.

## Novelty claim

Every method is established in mining-software-repositories work. **The novelty is the question, not the technique** — these instruments have been pointed at SE questions; nobody has pointed them at a computing-education one. Honest, clean, and far safer than claiming methodological innovation.

## SRC plan (5 weeks)

Studies 1+2 across 6–8 packages, plus Study 3 on 2–3. Complete self-contained empirical contribution, fits 2 pages with one figure.

Package set: CPython, NumPy, SciPy, PyTorch, pandas, scikit-learn, h5py, Pillow — foundational + user-facing so heterogeneity is visible.

Defer Study 4 and the curriculum audit to ITiCSE. Four studies in two pages is four studies badly.

## Limitations to state up front

- LOC is a crude proxy for complexity/importance/maintenance burden
- In-repo composition undercounts native dependencies (HDF5, BLAS/LAPACK, CUDA libs)
- Script counts comment and blank lines — use cloc/tokei for code-only, state which
- Vendored-tree inclusion changes results materially — pick a rule, apply consistently
- File-touches ≠ contribution quality or comprehension
- Package selection must be defended — state criteria before picking
