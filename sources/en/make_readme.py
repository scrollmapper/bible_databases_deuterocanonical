import os

def create_readme_in_folders():
    root_url = "https://github.com/LeoBlanchette/the_70_books/tree/main/copied_texts"
    base_dir = os.getcwd()
    
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        
        if os.path.isdir(folder_path):
            # Convert folder name to readable title
            readable_title = " ".join(word.capitalize() for word in folder_name.split("_"))
            
            # Create the README.md content
            readme_content = f"# {readable_title}\n\nBack to root: {root_url}\n"
            
            # Write the README.md file
            readme_path = os.path.join(folder_path, "README.md")
            if not os.path.exists(readme_path):
                with open(readme_path, "w") as readme_file:
                    readme_file.write(readme_content)

if __name__ == "__main__":
    create_readme_in_folders()
