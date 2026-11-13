# Pilot prompts (HUGS 2027)

Ten developer-style requests that require Python/C boundary code. Pilot design: 10 prompts × 2 models × 3 samples ≈ 60 samples (see `thesis-plan.md` §3–4).

## Files

- `P01`–`P10` `*.txt` — the exact text sent to each model. **Frozen once generation starts**; any change becomes a new version with a new ID, never an edit in place.
- `manifest.json` — metadata for the harness and the audit: stratum, binding mechanism, entry point, edge-case inputs for the ASan/UBSan/Valgrind runs, and the defect opportunities each prompt was designed to create. **Never sent to a model.**

## Coverage

| ID | Stratum | Binding | Task | Main boundary hazards (a-priori) |
|---|---|---|---|---|
| P01 | A C-API | c-api | group list of dicts by key | borrowed `PyDict_GetItem`, non-stealing `PyList_Append`/`PyDict_SetItem` |
| P02 | A C-API | c-api | `minmax` over any iterable | `PyIter_Next` error vs exhaustion, `PyFloat_AsDouble` -1 check |
| P03 | A C-API | c-api | filter list with Python predicate | borrowed item across a callback that mutates the list |
| P04 | A C-API | c-api | split list into tuples | stealing `PyTuple_SET_ITEM` on borrowed items |
| P05 | B ctypes | ctypes | wrap C fn returning malloc'd string | `c_char_p` restype leak, cross-DSO allocator mismatch |
| P06 | B cffi | cffi | pass `list[str]` as `const char **` | `ffi.new` temporaries freed before the call, UTF-8 sizing |
| P07 | B ctypes | ctypes | register a Python callback with a C event loop | `CFUNCTYPE` object collected while C holds it |
| P08 | C exceptions | c-api | custom exception type in module init | `PyModule_AddObject` steal-on-success, NULL without exception |
| P09 | C exceptions | c-api | `retry(func, attempts)` | swallowing `BaseException`, saving/restoring exception state |
| P10 | C exceptions | c-api | read file into list, GIL released | API calls without the GIL, allocator families, errno → `OSError` |

4 / 3 / 3 split across strata A / B / C. Six prompts use the raw C API, two ctypes, one cffi, and P07 uses a ctypes callback.

## Writing rules (from `CLAUDE.md`)

- Phrased like Stack Overflow / GitHub-issue requests: first person, a concrete use case, an example call.
- **No security hints.** The words *safe, secure, leak, memory, refcount, vulnerability, sanitizer* do not appear. Performance motivation ("hot loop", "too slow") is used where realistic, since that is why people write boundary code.
- Each prompt names a module and entry point so the harness can build and call every sample the same way. Each asks for build instructions (setup.py or gcc command) so build failures can be recorded instead of fixed by hand.
- Edge cases a real developer would state (empty input → ValueError, etc.) are included because they force error-path code. Error paths are where most refcount and exception-state defects live.

## Open decisions for the generation script

- **System prompt:** none, or one fixed neutral line. Record which one in each sample's metadata.
- **Python target:** prompts mention 3.10+/3.12 where natural. The harness should pin one CPython build (suggest 3.12, built with `--with-pydebug` for the debug runs so refcount assertions fire) and record it.
- **Code extraction:** keep the raw response verbatim in `corpus/` and save extracted files separately. Samples that need hand-assembly to build should be flagged as such, not fixed.
- `defect_opportunities` / `literacy_guess` are hypotheses for designing the prompts. They must **not** be shown to coders before their independent audit, so they don't bias the ground truth.
