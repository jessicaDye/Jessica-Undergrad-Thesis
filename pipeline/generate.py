"""Generate the pilot corpus: every prompt x every generator model x N samples.

    .venv/bin/python pipeline/generate.py --list-models     # pick exact model IDs
    .venv/bin/python pipeline/generate.py --dry-run         # show what would run
    .venv/bin/python pipeline/generate.py                   # generate (resumable)
    .venv/bin/python pipeline/generate.py --only P04 --models claude --samples 1

The corpus is frozen: an existing sample is never regenerated or overwritten.
Each sample directory holds
    response.md   the model's text, verbatim
    raw_api.json  the full API response object
    meta.json     prompt hash, model requested/returned, params, timestamps, usage
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
import time
from importlib.metadata import version

from dotenv import load_dotenv

import config

load_dotenv(config.ROOT / ".env", override=True)  # .env wins over shell env


def utcnow():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def load_prompts():
    manifest = json.loads((config.PROMPTS_DIR / "manifest.json").read_text())
    out = []
    for p in manifest["prompts"]:
        text = (config.PROMPTS_DIR / p["prompt_file"]).read_text()
        out.append({**p, "text": text,
                    "sha256": hashlib.sha256(text.encode()).hexdigest(),
                    "manifest_version": manifest["version"]})
    return out


# --- providers ---------------------------------------------------------------

def call_anthropic(model, prompt):
    import anthropic
    client = anthropic.Anthropic()
    kw = dict(model=model, max_tokens=config.MAX_OUTPUT_TOKENS,
              messages=[{"role": "user", "content": prompt}])
    if config.SYSTEM_PROMPT:
        kw["system"] = config.SYSTEM_PROMPT
    if config.TEMPERATURE is not None:
        kw["temperature"] = config.TEMPERATURE
    r = client.messages.create(**kw)
    text = "".join(b.text for b in r.content if b.type == "text")
    return text, r.model, r.stop_reason, r.usage.model_dump(), r.model_dump(), \
        f"anthropic=={version('anthropic')}"


def call_openai(model, prompt):
    import openai
    client = openai.OpenAI()
    kw = dict(model=model, input=prompt, max_output_tokens=config.MAX_OUTPUT_TOKENS)
    if config.SYSTEM_PROMPT:
        kw["instructions"] = config.SYSTEM_PROMPT
    if config.TEMPERATURE is not None:
        kw["temperature"] = config.TEMPERATURE
    r = client.responses.create(**kw)
    return r.output_text, r.model, r.status, \
        (r.usage.model_dump() if r.usage else None), r.model_dump(), \
        f"openai=={version('openai')}"


CALLERS = {"anthropic": call_anthropic, "openai": call_openai}


def list_models():
    import anthropic, openai
    from google import genai
    print("# anthropic"); [print(" ", m.id) for m in anthropic.Anthropic().models.list(limit=50)]
    print("# openai");    [print(" ", m.id) for m in sorted(openai.OpenAI().models.list(), key=lambda m: m.id)]
    print("# gemini");    [print(" ", m.name) for m in genai.Client().models.list()]


# --- main --------------------------------------------------------------------

def generate_one(prompt, key, spec, k):
    d = config.CORPUS_DIR / prompt["id"] / key / f"s{k}"
    if (d / "response.md").exists():
        return "skip"
    d.mkdir(parents=True, exist_ok=True)
    started = utcnow()
    for attempt in range(1, 6):
        try:
            text, model_ret, stop, usage, raw, sdk = CALLERS[spec["provider"]](spec["model"], prompt["text"])
            break
        except Exception as e:  # transient API errors: back off and retry
            print(f"    attempt {attempt} failed: {type(e).__name__}: {e}", file=sys.stderr)
            if attempt == 5:
                raise
            time.sleep(10 * attempt)
    meta = {
        "sample_id": f"{prompt['id']}-{key}-s{k}",
        "prompt_id": prompt["id"], "prompt_file": prompt["prompt_file"],
        "prompt_sha256": prompt["sha256"], "prompt_set": config.PROMPT_SET,
        "manifest_version": prompt["manifest_version"],
        "generator_key": key, "provider": spec["provider"],
        "model_requested": spec["model"], "model_returned": model_ret,
        "sdk": sdk, "system_prompt": config.SYSTEM_PROMPT,
        "temperature": config.TEMPERATURE if config.TEMPERATURE is not None else "default",
        "max_output_tokens": config.MAX_OUTPUT_TOKENS,
        "sample_index": k, "attempts": attempt,
        "requested_at": started, "received_at": utcnow(),
        "stop_reason": stop, "usage": usage,
    }
    (d / "raw_api.json").write_text(json.dumps(raw, indent=2, default=str))
    (d / "meta.json").write_text(json.dumps(meta, indent=2))
    (d / "response.md").write_text(text)  # written last: marks the sample complete
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", nargs="*", help="prompt IDs, e.g. P01 P04")
    ap.add_argument("--models", nargs="*", help="generator keys, e.g. claude gpt")
    ap.add_argument("--samples", type=int, default=config.SAMPLES_PER_PROMPT)
    a = ap.parse_args()
    if a.list_models:
        return list_models()

    gens = {k: v for k, v in config.GENERATORS.items() if not a.models or k in a.models}
    for k, v in gens.items():
        if v["model"] == "FILL_ME":
            sys.exit(f"Set an exact model ID for '{k}' in pipeline/config.py first.")
    prompts = [p for p in load_prompts() if not a.only or p["id"] in a.only]

    jobs = [(p, k, v, i) for p in prompts for k, v in gens.items()
            for i in range(1, a.samples + 1)]
    print(f"{len(jobs)} samples planned -> {config.CORPUS_DIR.relative_to(config.ROOT)}")
    for p, k, v, i in jobs:
        tag = f"{p['id']}-{k}-s{i}"
        if a.dry_run:
            print("  would generate", tag, "with", v["model"]); continue
        status = generate_one(p, k, v, i)
        print(f"  {tag}: {status}", flush=True)


if __name__ == "__main__":
    main()
