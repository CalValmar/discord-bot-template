import os
from pathlib import Path
from dotenv import load_dotenv


def _normalize_token(raw_token: str | None) -> str | None:
    if not raw_token:
        return None
    token = raw_token.strip().strip('"').strip("'")
    if token.lower().startswith("bot "):
        token = token[4:].strip()
    return token or None


PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

TOKEN = _normalize_token(os.getenv("DISCORD_TOKEN"))
PREFIX = "!"
