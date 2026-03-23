import os

from openai import OpenAI
from langchain_openai import ChatOpenAI
from requests.exceptions import RequestException

LLM_MODE = os.getenv("LLM_MODE", "local").strip().lower()
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "").strip()
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "").strip()
LLM_API_KEY = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY")

def _resolve_env():
    mode = LLM_MODE
    if mode not in ("local", "online"):
        raise ValueError("LLM_MODE must be 'local' or 'online'")

    if mode == "local":
        base_url = LLM_BASE_URL
        api_key = LLM_API_KEY or None
    else:  # online
        api_key = LLM_API_KEY
        if not api_key:
            raise ValueError("LLM_API_KEY or OPENAI_API_KEY is required for online mode")
        if LLM_BASE_URL:
            base_url = LLM_BASE_URL
        else:
            base_url = None
            print("LLM_MODE=online and no LLM_BASE_URL set; using SDK default OpenAI endpoint")

    if not LLM_MODEL_NAME:
        raise ValueError("LLM_MODEL_NAME must be set in environment")

    return base_url, api_key


LLM_BASE_URL, EFFECTIVE_API_KEY = _resolve_env()

client = OpenAI(
    base_url=LLM_BASE_URL,
    api_key=EFFECTIVE_API_KEY
)

local_llm = ChatOpenAI(
    base_url=LLM_BASE_URL,
    model=LLM_MODEL_NAME,
    api_key=lambda: EFFECTIVE_API_KEY,
)


def message(prompt: str, role: str = "user", temperature: float = 0.3) -> str:
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL_NAME,
            messages=[{"role": role, "content": prompt}],
            temperature=temperature,
            max_tokens=500,
        )
    except RequestException as exc:
        raise ConnectionError(
            f"Could not connect to LLM at {LLM_BASE_URL}. "
            f"Check the server is running and the URL is correct. Original error: {exc}"
        ) from exc
    except Exception as exc:
        raise RuntimeError(f"LLM request failed: {exc}") from exc

    msg = getattr(response.choices[0], "message", None)
    if not msg or not getattr(msg, "content", None):
        raise RuntimeError("Error: no content returned by the LLM response.")

    return msg.content
