from rouge_score import rouge_scorer
from bert_score import score as bert_scorer

scorer = rouge_scorer.RougeScorer(
    ['rouge1','rouge2','rougeL'],
    use_stemmer=True
)

def calculate_rouge_score(reference_summary: str, summary: str) -> dict:
    return scorer.score(reference_summary, summary)

def calculate_bert_score(reference_summary: str, summary: str, language :str = "es") -> tuple:
    return bert_scorer(
        [summary],
        [reference_summary],
        lang = language
    )
