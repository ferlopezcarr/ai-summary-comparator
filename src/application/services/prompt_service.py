def get_basic_prompt(article: str) -> str:
    """
    Constructs a basic prompt for summarization based on the provided article text.
    Args:
        article (str): The input article text to be summarized.    
    Returns:
        str: A formatted prompt string to be sent to the LLM for summary generation.
    """
    return f"""
Summarize the following article in a concise and coherent manner, capturing the main points and key information:
{article}
"""

def get_advanced_prompt(article: str) -> str:
    """
    Constructs an advanced prompt for summarization based on the provided article text.
    This prompt may include additional instructions or constraints to guide the LLM in generating a more refined summary.
    Args:
        article (str): The input article text to be summarized.    
    Returns:
        str: A formatted prompt string with advanced instructions for summary generation.
    """
    return f"""
"""

def get_question_prompt() -> str:
    """
    Constructs a prompt for answering a specific question based on the provided article text.
    Args:
        question (str): The specific question to be answered based on the article.    
    Returns:
        str: A formatted prompt string to be sent to the LLM for question answering.
    """
    return """
Use the following context to answer the question.
If you do not know the answer, say so. Be concise.
                                                     
{context}
                                                     
Question: {question}
"""
