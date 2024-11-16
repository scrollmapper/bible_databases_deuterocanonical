import os
import json

def create_readme_for_book(book_dir, book_name):
    json_file_path = os.path.join(book_dir, f"{book_name}.json")
    
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        book_data = json.load(json_file)
        book_title = book_data["books"][0]["name"]
    
    readme_path = os.path.join(book_dir, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, 'w', encoding='utf-8') as readme_file:
            readme_file.write(f"# {book_title}\n")
        print(f"Created README.md for {book_name} in {book_dir}")
    else:
        print(f"README.md already exists for {book_name} in {book_dir}")

def iterate_and_create_readmes(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                book_name = os.path.splitext(file)[0]
                # Ensure the file is in the format <book>/<book>.json
                if os.path.basename(root) == book_name:
                    create_readme_for_book(root, book_name)

if __name__ == "__main__":
    base_directory = "."  # Change this to your base directory
    iterate_and_create_readmes(base_directory)