# 11.2 - Working With Paths in Python
# Solutions to review exercises


# Initial setup
import os
import glob

# This path may need to be changed depending on your setup
path = "C:/Real Python/python-basics-exercises/ch11-file-input-and-output\
/practice_files/images"


# Exercise 1
# Display the full paths of all files and folders in the main "images" folder
print('Full contents of "images" folder:')
for file_name in os.listdir(path):
    print(os.path.join(path, file_name))


# Exercise 2
# Display the full paths of any `*.png` files in the "images" folder
file_matches = os.path.join(path, "*.png")
print('All PNG files in "images" folder:')
for file_name in glob.glob(file_matches):
    print(file_name)


# Exercise 3
# Rename all `*.png` files in the "images" folder and its subfolders
# to `*_backup.png`
for current_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        file_path = os.path.join(current_folder, file_name)
        if file_path.lower().endswith(".png"):
            new_path = file_path[-4] + "_backup.png"
            os.rename(file_path, new_path)


# Exercsie 4
# Check that the two files have been converted to JPGs successfully
print(os.path.exists(os.path.join(path, "png file - not a gif_backup.png")))
print(
    os.path.exists(
        os.path.join(path, "additional files/one last image_backup.png")
    )
)


# Exercise 5
os.mkdir("Output")
with open("Output/python.txt", "w") as out_file:
    out_file.write("I was put here by Python!")
