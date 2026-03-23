import os

from openai import OpenAI
from langchain_openai import ChatOpenAI
from requests.exceptions import RequestException

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:1234/v1")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "")
LLM_API_KEY = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY") or None

client = OpenAI(
    base_url=LLM_BASE_URL,
    api_key=LLM_API_KEY or None,
)

local_llm = ChatOpenAI(
    base_url=LLM_BASE_URL,
    model=LLM_MODEL_NAME,
    api_key=lambda: LLM_API_KEY,
)


def message(prompt: str, role: str = "user", temperature: float = 0.3) -> str:
    if not LLM_MODEL_NAME:
        raise ValueError("LLM_MODEL_NAME must be set in environment")

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

