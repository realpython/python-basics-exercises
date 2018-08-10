# 1.12.2 - Assignment: Add a Cover Sheet to a PDF File
# Solution to assignment


# Add a cover sheet to a PDF; save the full output as a new PDF

import os
<<<<<<< HEAD
from pyPDF2 import PdfFileReader, PdfFileWriter
=======
from pyPDF import PdfFileReader, PdfFileWriter
>>>>>>> 8c6da63ad8724a2f0ed3eb8538b85686a172dff4

path = "C:/Real Python/Course materials/Chapter 12/Practice files"

input_file_name1 = os.path.join(path, "Emperor cover sheet.pdf")
input_file1 = PdfFileReader(open(input_file_name1, "rb"))

input_file_name2 = os.path.join(path, "The Emperor.pdf")
input_file2 = PdfFileReader(open(input_file_name2, "rb"))

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
output_file_name = os.path.join(path, "Output/The Covered Emperor.pdf")

with open(output_file_name, "wb") as output_file:
    output_PDF.write(output_file)
