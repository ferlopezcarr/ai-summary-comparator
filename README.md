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
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
uv sync
```

or

```bash
pip install -e . # If pip is not in PATH: python -m pip install -e .
```

### 3. Configure LLM

- The default client points to LM Studio at <http://192.168.1.154:1234/v1>.
- Update [src/infrastructure/outbound/llm_rest_api.py](src/infrastructure/outbound/llm_rest_api.py) if your endpoint or model differs.

### 4. Configure prompts

- The prompts for generating summaries are defined in [src/domain/prompts.py](src/domain/prompts.py).
- Adjust the prompts as needed for your specific use case or to improve summary quality.

## Run

### 1. Activate the virtual environment if not already active

```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
```

### 2. Run the main script

Use module mode so imports resolve correctly:

```bash
python -m src.main
```

After doing all configurations you should see the generated summaries and their ROUGE-L and BERTScore F1 scores printed in the console.

## Inputs

The folder [resources/input](resources/input) contains the input files where you should place:

- The article text in [article.md](resources/input/article.md).
- The reference summary in [reference_summary.md](resources/input/reference_summary.md).

## Outputs

The folder [resources/output](resources/output) will contain the generated summaries and evaluation results:

- Prints the basic and advanced summaries.
- Prints ROUGE-L and BERTScore F1 for each summary.
