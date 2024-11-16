import os

def rename_readme_to_info(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for filename in filenames:
            if filename.lower() == 'readme.md':
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, 'INFO.md')
                os.rename(old_path, new_path)
                print(f'Renamed file: {old_path} -> {new_path}')

if __name__ == "__main__":
    root_directory = '.'  # Change this to your root directory
    rename_readme_to_info(root_directory)