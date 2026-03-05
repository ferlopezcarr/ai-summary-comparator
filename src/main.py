from dotenv import load_dotenv
load_dotenv()

from src.infrastructure.inbound.article_file_service import read_resource, save_resource
from src.infrastructure.outbound.llm_rest_api import ask_question, generate_embedding_db, message
from src.application.services.prompt_service import get_basic_prompt, get_advanced_prompt
from src.application.services.score_service import calculate_rouge_score, calculate_bert_score

language = "en"  # Set the language for evaluation (e.g., "en" for English)

article = read_resource("article.md")
reference_summary = read_resource("reference_summary.md")

basic_prompt = get_basic_prompt(article)
refined_prompt = get_advanced_prompt(article)

basic_summary = message(basic_prompt)
advanced_summary = message(refined_prompt)

if not basic_summary or not advanced_summary:
    print("Error: Failed to generate summaries.")
    exit(1)

# Evaluate summaries using ROUGE-L
rouge_basic = calculate_rouge_score(reference_summary, basic_summary)
rouge_advanced = calculate_rouge_score(reference_summary, advanced_summary)

# Evaluate summaries using BERTScore
P_basic, R_basic, F1_basic = calculate_bert_score(reference_summary, basic_summary)
P_adv, R_adv, F1_adv = calculate_bert_score(reference_summary, advanced_summary, language)

def main():
    print("\n==========================================")
    print(" AI SUMMARY COMPARATOR")
    print("==========================================\n")

    basic_summary_filename = "basic_summary.md"
    advanced_summary_filename = "advanced_summary.md"
    print(f"BASIC SUMMARY in {basic_summary_filename}")
    save_resource(basic_summary_filename, basic_summary)
    print(f"ADVANCED SUMMARY in {advanced_summary_filename}")
    save_resource(advanced_summary_filename, advanced_summary)

    print("\n----------- ROUGE-L -----------")
    print("Basic:", round(rouge_basic["rougeL"].fmeasure, 4))
    print("Advanced:", round(rouge_advanced["rougeL"].fmeasure, 4))

    print("\n----------- BERTScore F1 -----------")
    print("Basic:", round(F1_basic.mean().item(), 4))
    print("Advanced:", round(F1_adv.mean().item(), 4))

    filename = input("\nEnter the filename of the article to ask questions about (default: article.pdf): ")
    if not filename.strip():
        filename = "article.pdf"
    
    vector_db = generate_embedding_db(filename)

    while True:
        user_input = input("\nEnter a question about the article (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the AI Summary Comparator. Goodbye!")
            break
        response = ask_question(user_input, vector_db)
        print("\nAI Response:")
        print(response)

    print("\n==========================================")


if __name__ == "__main__":
    main()
