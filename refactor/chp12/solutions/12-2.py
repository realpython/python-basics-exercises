# 12.2 review exercises

import os
import copy
from pyPdf import PdfFileReader, PdfFileWriter

path = "C:/Real Python/refactor/chp12/practice_files"
input_file_name = os.path.join(path, "Walrus.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()

input_file.decrypt("IamtheWalrus")  # decrypt the input file

for page_num in range(0, input_file.getNumPages()):
    # rotate pages (call everything page_left for now; will make a copy)
    page_left = input_file.getPage(page_num)
    page_left.rotateCounterClockwise(90)

    page_right = copy.copy(page_left)  # split each page in half
    upper_right = page_left.mediaBox.upperRight  # get original page corner

    # crop and add left-side page
    page_left.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_left)
    # crop and add right-side page
    page_right.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_right)

# save new pages to an output file
output_file_name = os.path.join(path, "Output/Updated Walrus.pdf")
with open(output_file_name, "wb") as output_file:
    output_PDF.write(output_file)
