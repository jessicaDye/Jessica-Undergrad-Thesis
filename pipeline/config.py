"""Pinned configuration for the pilot corpus. Changing anything here after
generation starts is a design change: record it in the paper's methods.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT_SET = "pilot"
PROMPTS_DIR = ROOT / "prompts" / PROMPT_SET
CORPUS_DIR = ROOT / "corpus" / PROMPT_SET
RUNS_DIR = ROOT / "runs"

SAMPLES_PER_PROMPT = 3

# Generator models. `model` must be an exact, dated/versioned API model ID
# (not an alias that can silently change). Fill in with `generate.py --list-models`.
GENERATORS = {
    "claude": {"provider": "anthropic", "model": "FILL_ME"},
    "gpt": {"provider": "openai", "model": "FILL_ME"},
}

# The LLM-review tier uses a third vendor so no model reviews its own output.
REVIEWER = {"provider": "gemini", "model": "FILL_ME"}

# Sampling: provider defaults, no system prompt -- what a developer pasting the
# request into a chat or API gets. Logged per sample regardless.
SYSTEM_PROMPT = None
TEMPERATURE = None          # None = provider default (recorded as "default")
MAX_OUTPUT_TOKENS = 16000
