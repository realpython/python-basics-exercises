# 10.2 remove_files.py
# Remove JPG files from multiple folders based on file size

import os

path = "C:/Real Python/Course materials/Chapter 10/Practice files/little pics"
for currentFolder, subfolders, fileNames in os.walk(path):
    for fileName in fileNames:
        fullPath = os.path.join(currentFolder, fileName)
        # check if file is a JPG
        checkJPG = fileName.lower().endswith(".jpg")
        # check if size is less than 2Kb
        checkSize = os.path.getsize(fullPath) < 2000
        if checkJPG and checkSize:  # both conditions must be True
            print 'Deleting "{}"...'.format(fileName)
            os.remove(fullPath)
