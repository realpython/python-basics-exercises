# 8.2 cover_the_emperor.py
# Add a cover sheet to a PDF; save the full output as a new PDF

import os
from pyPdf import PdfFileReader, PdfFileWriter

path = "C:/Real Python/Course materials/Chapter 12/Practice files"
input_file_name1 = os.path.join(path, "Emperor cover sheet.pdf")
input_file1 = PdfFileReader(file(input_file_name1, "rb"))
input_file_name2 = os.path.join(path, "The Emperor.pdf")
input_file2 = PdfFileReader(file(input_file_name2, "rb"))
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
output_file = file(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
