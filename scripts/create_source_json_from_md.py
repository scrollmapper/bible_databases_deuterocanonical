import os
import json
import re

def parse_md_to_json(md_content):
    lines = md_content.splitlines()
    book = {"name": "", "chapters": []}
    current_chapter = None
    verse_pattern = re.compile(r"\*\*\[(\d+):(\d+)\]\*\* (.+?)(?=\*\*\[\d+:\d+\]\*\*|$)", re.DOTALL)
    
    # Extract the chapter name from the first non-empty line starting with #
    for line in lines:
        if line.strip():
            if line.startswith("#"):
                book["name"] = line[1:].strip()
                break
    
    matches = verse_pattern.findall(md_content)
    for match in matches:
        chapter_number = int(match[0])
        verse_number = int(match[1])
        verse_text = match[2].strip()
        
        if current_chapter is None or current_chapter["chapter"] != chapter_number:
            if current_chapter is not None:
                book["chapters"].append(current_chapter)
            current_chapter = {
                "chapter": chapter_number,
                "name": f"{book['name']} {chapter_number}",
                "verses": []
            }
        
        current_chapter["verses"].append({
            "verse": verse_number,
            "chapter": chapter_number,
            "name": f"{book['name']} {chapter_number}:{verse_number}",
            "text": verse_text
        })
    
    if current_chapter is not None:
        book["chapters"].append(current_chapter)
    
    return book

def convert_md_to_json(md_file_path, json_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    
    book_json = parse_md_to_json(md_content)
    books_json = {"books": [book_json]}
    
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(books_json, json_file, ensure_ascii=False, indent=4)

def iterate_and_convert(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                book_name = os.path.splitext(file)[0]
                # Ensure the file is in the format <book>/<book>.md
                if os.path.basename(root) == book_name:
                    md_file_path = os.path.join(root, file)
                    json_file_path = os.path.join(root, f"{book_name}.json")
                    convert_md_to_json(md_file_path, json_file_path)
                    print(f"Converted {md_file_path} to {json_file_path}")

if __name__ == "__main__":
    base_directory = "../sources/"  # Change this to your base directory
    iterate_and_convert(base_directory)