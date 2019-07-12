# 13.3 - Challenge: Add a Cover Sheet to a PDF File
# Solution to challenge


# Add a cover sheet to a PDF; save the full output as a new PDF

import os
from pyPDF2 import PdfFileReader, PdfFileWriter

path = "C:/python-basics-exercises/ch13-interact-with-pdf-files/\
        practice_files"

input_file_path1 = os.path.join(path, "Emperor cover sheet.pdf")
input_file1 = PdfFileReader(input_file_path1)

input_file_path2 = os.path.join(path, "The Emperor.pdf")
input_file2 = PdfFileReader(input_file_path2)

output_PDF = PdfFileWriter()

# Read in all pages from the cover sheet PDF file
for page_num in range(0, input_file1.getNumPages()):
    page = input_file1.getPage(page_num)
    output_PDF.addPage(page)

# Read in all pages from "The Emperor.pdf" into the same output file
for page_num in range(0, input_file2.getNumPages()):
    page = input_file2.getPage(page_num)
    output_PDF.addPage(page)

# Output the results into a new PDF
output_file_path = os.path.join(path, "Output/The Covered Emperor.pdf")

with open(output_file_path, "wb") as output_file:
    output_PDF.write(output_file)
