# Hu & Zhang 2020 — Reading Digest

*The Python/C API: Evolution, Usage Statistics, and Bug Patterns*, Mingzhe Hu & Yu Zhang, USTC, SANER 2020. Conference version of the JSEP 2023 article. Free PDF + replication package: **github.com/S4Plus/pyceac**

## Core argument

Python front-end + C/C++ native implementation is "almost the standard structure for many mainstream software systems." Feature discrepancies between the languages — memory management, exception handling, type systems — create security hazards **specifically in the interface layer**. Static analysis of CPython's API across versions, usage measured across real projects, taxonomy of **10 bug pattern classes** illustrated with real Pillow defects.

## The sentences to quote

On a missed `Py_DECREF` in Pillow's encoder — such handling is:

> "often missed by developers because they need not do this in pure Python code."

On version-handling flaws:

> "For developers who lack multilingual programming experience or multi-version tests, this handling is often overlooked, which can bring tons of failure feedback when open sourced."

Two peer-reviewed statements that Python-trained developers introduce defects at the boundary *because of what their training did not require*. Closest thing in the literature to a direct statement of the thesis — written by SE researchers with no interest in curriculum.

## Their Table II — published baseline for comparison

C/C++ code ratio at ~2019 versions:

| Project | Version | KLoC | C/C++ ratio |
|---|---|---|---|
| Pillow | 5.4.1 | 65.4 | 40.8% |
| NumPy | v1.1.0rc1 | 151.9 | **55.5%** |
| TensorFlow | v1.10.0 | 2,185.1 | 51.6% |
| PyTorch | v1.0rc1 | 690.2 | 57.9% |
| python-krbV | 1.0.90 | 4.9 | 86.4% |
| PyAudio | 0.2.11 | 3.3 | 57.2% |
| python-ldap | 3.2.0 | 12.6 | 22.5% |

**Validity check to use:** their NumPy = 55.5%; our HEAD measurement Aug 2026 = 55.7%. Two independent measurements, seven years apart, different methods, same number. Corroborates the longitudinal stability finding with a prior *published* source rather than only our own tooling.

**Be careful with PyTorch:** their v1.0rc1 was 690 KLoC vs several million today, and their "C/C++ ratio" method isn't specified precisely enough to assume it matches ours. Note the difference, don't over-interpret.

## The 10 bug patterns

1. Insufficient error checking — return values used without null check
2. Integer overflow — `PyArg_Parse*` format chars (B, H, I, K, k) convert to C types with no overflow check
3. Dynamic memory management flaws — leaks, multiple frees, dangling pointers, allocator-family mismatches
4. API evolution flaws — Py2/3 incompatibility, ABI breakage, `Py_ssize_t` vs C `int` for sequence indexing
5. Buffer overflow — values crossing the boundary overflow in the interface layer; Python's negative indices invalid natively
6. TOCTOU — race conditions in file access
7. Reference counting errors — native objects outside the GC; `Py_INCREF`/`Py_DECREF` explicit; borrowing/stealing semantics make it highly error-prone
8. Type misuses — dynamic typing raises type-confusion risk at the boundary
9–10. Described behaviorally, no empirical instances

## Four memory allocator families

Memory from `PyMem_Malloc` must be freed with `PyMem_Free`; `PyMem_Del` or plain `free` are both wrong.

| Allocator | Since | Default versions | Thread safe | Binary compat | Small-obj opt |
|---|---|---|---|---|---|
| `malloc` | — | < 3.4 | Y | Y | N |
| `PyMem_RawMalloc` | 3.4 | 3.4, 3.5 | Y | Y | N |
| `PyMem_Malloc` | 3.4 | ≥ 3.6 | N | Y | Y |
| `PyMem_MALLOC` | 3.4 | — | N | N | Y |

A Python-only education gives a student no reason to have ever formed the concept that a free must match its allocate.

## How to differentiate from it

Theirs is **software-engineering research**: here's a defect taxonomy, here's a detection toolchain. Ours is the question they didn't ask — *if these defects arise because developers lack the mental model, what does that imply for curriculum?* State this explicitly in related work; it protects against a reviewer who thinks we're re-treading their ground.

Their replication package (corpus, checkers, generated data) is public — a running start if Study 4 gets extended.
