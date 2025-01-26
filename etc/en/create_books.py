import os
import json
import re

# Define the root directories
root_dirs = ["church_history_json_sources/ante_nicene_series", "church_history_json_sources/nicene_series1", "church_history_json_sources/nicene_series2"]

# Function to convert Roman numerals to numbers
def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            num += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            num += roman[s[i]]
    return num

# Function to replace Roman numerals in a string with numbers
def replace_roman_numerals(text):
    return re.sub(r'\b[IVXLCDM]+\b', lambda x: str(roman_to_int(x.group())), text)

# Function to slugify book titles
def slugify(title, max_length=50):
    title = replace_roman_numerals(title)
    slug = re.sub(r'[^\w\-]', '', re.sub(r'\s+', '-', title.lower()))
    return slug[:max_length]

# Function to get the subdirectory based on the root directory
def get_subdir(root_dir):
    if "ante_nicene_series" in root_dir:
        return "ante-nicene"
    elif "nicene_series1" in root_dir:
        return "nicene-1"
    elif "nicene_series2" in root_dir:
        return "nicene-2"
    return ""

# Function to process each JSON file
def process_json_file(file_path, subdir):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for book in data:
            book_title = book['book']
            slug_title = slugify(book_title)
            book_dir = os.path.join("church_history", subdir, slug_title)
            os.makedirs(book_dir, exist_ok=True)
            
            # Create the main markdown file
            md_file_path = os.path.join(book_dir, f"{slug_title}.md")
            with open(md_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(f"# {book_title}\n\n")
                for chapter in book['chapters']:
                    chapter_num = chapter['chapter']
                    for verse_num, verse in enumerate(chapter['verses'], start=1):
                        md_file.write(f"**[{chapter_num}:{verse_num}]** {verse['text']}\n\n")
            
            # Create the README.md file
            readme_file_path = os.path.join(book_dir, "README.md")
            with open(readme_file_path, 'w', encoding='utf-8') as readme_file:
                readme_file.write(f"# {book_title}\n")

# Loop over the root directories and process each JSON file
for root_dir in root_dirs:
    subdir = get_subdir(root_dir)
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                process_json_file(file_path, subdir)