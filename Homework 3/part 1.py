import os
import shutil
import sys

def copy_files_recursively(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            copy_files_recursively(item_path, dest_dir)
        elif os.path.isfile(item_path):
            ext = os.path.splitext(item)[1][1:].lower() 
            if ext == "":
                ext = "no_extension"
            ext_dir = os.path.join(dest_dir, ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.copy(item_path, ext_dir)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<destination_directory>]")
        return

    source_dir = sys.argv[1]
    if len(sys.argv) == 3:
        dest_dir = sys.argv[2]
    else:
        dest_dir = os.path.join(source_dir, "dist")

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    try:
        copy_files_recursively(source_dir, dest_dir)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
