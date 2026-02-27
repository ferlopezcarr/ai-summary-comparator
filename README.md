# AI Summary Comparator

Compare two LLM-generated summaries of a biomedical article and score them with ROUGE-L and BERTScore.

## Requirements

- Python 3.12+
- uv (python package manager)
- LM Studio or compatible LLM REST API endpoint.
- Downloaded models to be used with LM Studio (e.g., openai/gpt-oss-20b)

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
uv sync
```

or

```bash
pip install -e .
```

### 3. Configure LLM

- The default client points to LM Studio at <http://192.168.1.154:1234/v1>.
- Update [src/infrastructure/outbound/llm_rest_api.py](src/infrastructure/outbound/llm_rest_api.py) if your endpoint or model differs.

## Run

Use module mode so imports resolve correctly:

```bash
python -m src.main
```

## Inputs

- Place the article text in [article.md](resources/input/article.md).
- Place the reference summary in [reference_summary.md](resources/input/reference_summary.md).

## Outputs

- Prints the basic and advanced summaries.
- Prints ROUGE-L and BERTScore F1 for each summary.
