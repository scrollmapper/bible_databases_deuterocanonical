import os
import json

def generate_book_list(base_dir):
    book_list = []
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                book_name = os.path.splitext(file)[0]
                json_file_path = os.path.join(root, file)
                
                # Ensure the file is in the format <book>/<book>.json
                if os.path.basename(root) == book_name:
                    with open(json_file_path, 'r', encoding='utf-8') as json_file:
                        book_data = json.load(json_file)
                        book_title = book_data["books"][0]["name"]
                        book_dir = os.path.relpath(root, base_dir).replace("\\", "/")
                        book_list.append((book_title, book_dir))
    
    return book_list

def create_readme(book_list, readme_path):
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write("# Books\n\n")
        for book_title, book_dir in sorted(book_list):
            readme_file.write(f"- [{book_title}]({book_dir}/)\n")

if __name__ == "__main__":
    base_directory = "../sources/"  # Change this to your base directory
    readme_path = os.path.join(base_directory, "README.md")
    
    book_list = generate_book_list(base_directory)
    create_readme(book_list, readme_path)
    
    print(f"Generated {readme_path} with book list.")