# 12.2 - Working With File Paths in Python
# Solutions to review exercises


# Exercise 1
from pathlib import Path

file_path = Path.home() / "my_folder" / "my_file.txt"


# Exercise 2
print(file_path.exists())


# Exercise 3
print(file_path.name)


# Exercise 4
print(file_path.parent.name)


# Using os module 
import os
# Get current working directory
print(os.getcwd())

# Listing files and directories in current working directory
print(os.listdir(os.getcwd()))
