import os
import shutil

def move_jpg_files(source_folder, target_folder):
    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"Created folder: {target_folder}")
    
    # Loop through all files in the source folder
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):  # check only .jpg files
            source_path = os.path.join(source_folder, file_name)
            target_path = os.path.join(target_folder, file_name)
            
            shutil.move(source_path, target_path)  # move file
            print(f"Moved: {file_name}")
    
    print("✅ All .jpg files have been moved successfully!")

# Example usage (change these paths to your folders)
source = "C:/Users/DIU/Downloads"
target = "C:/Users/DIU/Pictures"

move_jpg_files(source, target)
