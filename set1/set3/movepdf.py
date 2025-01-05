import os
import shutil

# Define source and destination directories
source_dir = '/Users/Rebin/Documents/Wallapper_Group_Website/contents'
destination_dir = '/Users/Rebin/Documents/Wallapper_Group_Website/data'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Iterate over each item in the source directory
for subdir in os.listdir(source_dir):
    subdir_path = os.path.join(source_dir, subdir)
    
    # Check if the item is a directory
    if os.path.isdir(subdir_path):
        # Move each file in the subdirectory to the destination directory
        for file in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, file)
            if os.path.isfile(file_path):
                try:
                    shutil.move(file_path, destination_dir)
                    print(f"Moved: {file_path}")
                except Exception as e:
                    print(f"Failed to move {file_path}: {e}")
