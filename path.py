import os
from pathlib import Path

def organize_files(source_directory):
    source_path = Path(source_directory)
    
    if not source_path.is_dir():
        print(f"The specified source directory '{source_directory}' does not exist.")
        return

    # Define file type categories and corresponding subdirectories
    file_types = {
        'Images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp'),
        'Documents': ('.doc', '.docx', '.pdf', '.txt', '.xlsx', '.pptx'),
        'Videos': ('.mp4', '.avi', '.mkv', '.mov'),
    }

    # Create subdirectories for each file type
    for category in file_types:
        category_path = source_path / category
        category_path.mkdir(exist_ok=True)

    # Loop through files in the source directory and move them to the appropriate subdirectory
    for file_path in source_path.iterdir():
        if file_path.is_file():
            for category, extensions in file_types.items():
                if file_path.suffix.lower() in extensions:
                    destination = source_path / category / file_path.name
                    file_path.rename(destination)
                    print(f"Moved '{file_path.name}' to '{category}' directory.")

if os.name== "_main_":
    source_directory = input("Enter the source directory path: ")
    organize_files(source_directory)