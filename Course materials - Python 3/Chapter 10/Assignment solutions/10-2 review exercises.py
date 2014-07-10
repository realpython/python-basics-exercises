# 10.2 review exercises


# Initial setup
import os
import glob
# This path may need to be changed depending on your setup
path = "C:/Real Python/Course Materials - Python 3/Chapter 10/Practice files/images"


# Display the full paths of all files and folders in the main "images" folder
print('Full contents of "images" folder:')
for fileName in os.listdir(path):
    print(os.path.join(path, fileName))

# Display the full paths of any PNG files in the "images" folder
fileMatches = os.path.join(path, "*.png")
print('All PNG files in "images" folder:')
for fileName in glob.glob(fileMatches):
    print(fileName)

# Change all PNGs to JPGs in the "images" folder and its subfolders
# Could use indexing to get the file extension, but try using os.path.splitext()
for currentFolder, subfolders, fileNames in os.walk(path):
    for fileName in fileNames:
        filePath = os.path.join(currentFolder, fileName)
        fileTuple = os.path.splitext(filePath)  # split into (path, extension)
        if fileTuple[1].lower() == ".png":  # check if extension is PNG
            pass  # os.rename(filePath, fileTuple[0] + ".jpg")

# Check that the two files have been converted to JPGs successfully
print(os.path.exists(os.path.join(path, "png file - not a gif.jpg")))
print(os.path.exists(os.path.join(path, "additional files/one last image.jpg")))
