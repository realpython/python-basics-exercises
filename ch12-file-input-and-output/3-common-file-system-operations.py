# 12.3 Common File System Operations
# Solutions to Exercises


# Exercise 1
from pathlib import Path

new_dir = Path.home() / "my_folder"
new_dir.mkdir()


# Exercise 2
file1 = new_dir / "file1.txt"
file2 = new_dir / "file2.txt"
image1 = new_dir / "image1.png"

file1.touch()
file2.touch()
image1.touch()


# Exercise 3
images_dir = new_dir / "images"
images_dir.mkdir()
image1.replace(images_dir / "image1.png")


# Exercise 4
file1.unlink()


# Exercise 5
import shutil

shutil.rmtree(new_dir)
