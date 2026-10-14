import shutil
from pathlib import Path

def organize_directory(target_path_str):
    # Convert string to a Path object
    target_dir = Path(target_path_str)
    
    # Verify the directory exists
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    # Map category folder names to file extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Archives": [".zip", ".tar", ".gz", ".rar"],
        "Media": [".mp4", ".mp3", ".mov", ".wav"],
        "Code": [".py", ".html", ".css", ".js", ".json"]
    }

    # Iterate through all files in the target directory
    for file_path in target_dir.iterdir():
        # Skip directories, only process files
        if file_path.is_dir():
            continue
            
        file_ext = file_path.suffix.lower()
        moved = False
        
        # Check which category the file belongs to
        for category, extensions in categories.items():
            if file_ext in extensions:
                # Create the category folder if it doesn't exist
                category_dir = target_dir / category
                category_dir.mkdir(exist_ok=True)
                
                # Move the file
                shutil.move(str(file_path), str(category_dir / file_path.name))
                print(f"Moved: {file_path.name} -> {category}/")
                moved = True
                break
                
        # Optional: Catch-all for files that don't match any category
        if not moved and file_ext != "":
            others_dir = target_dir / "Others"
            others_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(others_dir / file_path.name))
            print(f"Moved: {file_path.name} -> Others/")

if __name__ == "__main__":
    # Example: organizing the local Downloads folder
    # Replace with your actual path, e.g., "C:/Users/YourName/Downloads"
    folder_to_organize = input("Enter the folder")
    print(f"Organizing {folder_to_organize}...")
    organize_directory(folder_to_organize)
    print("Done!")