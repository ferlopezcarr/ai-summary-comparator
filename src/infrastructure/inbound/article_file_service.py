# Read a file called "article.md" from "resources" directory and return its content as a string
import os

INPUT_DIR = os.getenv("INPUT_DIR", "resources/input")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "resources/output")

def get_input_file_path(filename: str) -> str:
    return os.path.join(INPUT_DIR, filename)

def read_resource(filename: str) -> str:
    file_path = os.path.join(INPUT_DIR, filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        message = f"File {filename} not found in {INPUT_DIR}."
        raise Exception(message)

def save_resource(filename: str, content: str) -> None:
    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)