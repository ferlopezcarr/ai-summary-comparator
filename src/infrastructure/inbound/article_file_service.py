# Read a file called "article.md" from "resources" directory and return its content as a string
import os

from regex import E

RESOURCES_DIR='resources'

def read_resource(filename: str) -> str:
    file_path = os.path.join(RESOURCES_DIR, "input", filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        message = f"File {filename} not found in {RESOURCES_DIR}."
        raise Exception(message)

def save_resource(filename: str, content: str) -> None:
    file_path = os.path.join(RESOURCES_DIR, "output", filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)