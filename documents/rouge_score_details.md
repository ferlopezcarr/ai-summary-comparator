# ROUGE Overview

This document explains how ROUGE (and the `rouge_scorer` used in this project) works, what the scores mean, and how to interpret the output.

## What ROUGE Measures

ROUGE compares a candidate summary against a reference summary by measuring overlap between the two texts. It focuses on surface-level similarity (exact or near-exact matches), which makes it useful for evaluating summarization quality.

Key points:

- It is overlap-based: it measures shared tokens or sequences.
- It is recall-heavy by design, but F1 is commonly used for balance.
- It does not capture semantic similarity well when wording differs a lot.

## ROUGE Variants in This Project

The project uses these ROUGE metrics:

- ROUGE-1: overlap of unigrams (individual tokens).
- ROUGE-2: overlap of bigrams (two-token sequences).
- ROUGE-L: longest common subsequence (LCS) between candidate and reference.

ROUGE-L is often preferred for summaries because it captures sentence-level ordering without requiring exact contiguous matches.

## How the Algorithm Works (High Level)

1. Tokenize the candidate and reference texts.
2. Compute overlap between token sets or sequences.
3. Calculate Precision, Recall, and F1:
   - Precision: proportion of candidate tokens also found in the reference.
   - Recall: proportion of reference tokens found in the candidate.
   - F1: harmonic mean of Precision and Recall.

For ROUGE-L, the overlap is based on the length of the longest common subsequence.

## What `rouge_scorer` Returns

The `rouge_scorer.RougeScorer` returns a dictionary keyed by metric name, each with a score object containing:

- `precision`
- `recall`
- `fmeasure`

In this project, `rougeL.fmeasure` is printed for each summary.

## Example Usage in This Project

```python
from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=True
)

scores = scorer.score(reference_summary, summary)
rouge_l = scores["rougeL"].fmeasure
```

## Practical Interpretation

- Higher scores mean more overlap with the reference.
- ROUGE is sensitive to wording and tokenization.
- Use ROUGE alongside semantic metrics (like BERTScore) for a more complete picture.

## Tips

- Keep preprocessing consistent for candidate and reference.
- Consider stemming or lowercasing if your texts vary in inflection.
- Do not compare scores across different tokenization or preprocessing settings.
