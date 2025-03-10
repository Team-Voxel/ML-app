from PySide6.QtWidgets import QFileDialog
import shutil
import os

    
def open_file_browser(window, start_dir = "", ext_filter ="All Files (*)"):
    file_path, _ = QFileDialog.getOpenFileName(window, "Open File", start_dir, ext_filter)

    if file_path:
        return file_path
    else:
        return "no path"


def get_file_name(path):
    return os.path.basename(path)


def copy_file_to(source_path, destination_dir):
    if not os.path.isfile(source_path):
        print("Error: Source file does not exist.")
        return False

    if not os.path.isdir(destination_dir):
        print("Error: Destination directory does not exist.")
        return False

    try:
        file_name = os.path.basename(source_path)
        destination_path = os.path.join(destination_dir, file_name)
        shutil.copy2(source_path, destination_path)
        print(f"File copied successfully to {destination_path}")
        return True
    except Exception as e:
        print(f"Error copying file: {e}")
        return False