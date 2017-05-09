# chapter 9 remove_files.py
# Remove JPG files from multiple folders based on file size

import os

path = "C:/Real Python/refactor/chp10/practice_files/little pics"
for current_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        full_path = os.path.join(current_folder, file_name)
        # check if file is a JPG
        check_JPG = file_name.lower().endswith(".jpg")
        # check if size is less than 2Kb
        check_size = os.path.getsize(full_path) < 2000
        if check_JPG and check_size:  # both conditions must be True
            print('Deleting "{}"...'.format(file_name))
            os.remove(full_path)
