# BERTScore Overview

This document explains how BERTScore (and the `bert_scorer` function used in this project) works, what the scores mean, and how to interpret the output.

## What BERTScore Measures

BERTScore compares a candidate text (your generated summary) against a reference text (your ground-truth summary). It uses contextual embeddings from a pretrained BERT-like model to measure semantic similarity rather than exact word overlap.

Key points:

- It is semantic: similar meanings can score well even if wording differs.
- It is token-based: each token is represented by a contextual embedding.
- It computes Precision, Recall, and F1 using token-to-token similarity.

## How the Algorithm Works (High Level)

1. Tokenize the candidate and reference texts.
2. Run both through a pretrained transformer model to produce contextual embeddings.
3. Compute cosine similarities between all candidate and reference tokens.
4. For each candidate token, find the best matching reference token (max similarity).
5. For each reference token, find the best matching candidate token.
6. Compute:
   - Precision: average best-match similarity for candidate tokens.
   - Recall: average best-match similarity for reference tokens.
   - F1: harmonic mean of Precision and Recall.

## What `bert_scorer` Returns

The `bert_scorer` function (from `bert_score.score`) returns a tuple:

- `P`: Precision scores
- `R`: Recall scores
- `F1`: F1 scores

In this project, each input is a single pair of texts, so each output is a tensor with one value. You typically use `F1.mean().item()` to get a scalar.

## Language and Model Selection

BERTScore can automatically select a suitable model based on the language:

- `lang="es"` uses a multilingual model (e.g., `bert-base-multilingual-cased`).
- If you want a specific model, you can pass `model_type="<model-name>"`.

Choosing a model that matches your text domain and language can improve relevance.

## Why You See "UNEXPECTED" Weights

When BERTScore loads a pretrained checkpoint, it may log warnings about "UNEXPECTED" keys. This is normal when the model checkpoint includes pretraining heads (like `cls.*`) that are not used for scoring. The core encoder weights are loaded correctly.

## Practical Interpretation

- Scores closer to 1.0 mean higher semantic similarity.
- For summaries, F1 is commonly used as the main metric.
- Compare scores across runs rather than absolute thresholds.

## Example Usage in This Project

The scoring function used here:

```python
from bert_score import score as bert_scorer

P, R, F1 = bert_scorer(
    [summary],
    [reference_summary],
    lang="es"
)
```

## Tips

- Cache the model locally to reduce repeated downloads.
- Set `HF_TOKEN` if you hit rate limits from Hugging Face.
- Use consistent preprocessing for candidate and reference texts.
