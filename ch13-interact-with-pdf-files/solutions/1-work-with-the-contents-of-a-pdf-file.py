# 13.1 - Work With the Contents of a PDF File
# Solutions to review exercises


import os
from pyPDF2 import PdfFileReader, PdfFileWriter


# Exercise 1
path = "C:/Real Python/refactor/chp12/practice_files"
input_file_name = os.path.join(path, "The Whistling Gypsy.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))

# Display meta-data about file
print("Title:", input_file.getDocumentInfo().title)
print("Author:", input_file.getDocumentInfo().author)
print("Number of pages:", input_file.getNumPages())


# Exercise 2
# Specify and open output text file
output_file_name = os.path.join(path, "Output/The Whistling Gypsy.txt")
with open(output_file_name, "w") as output_file:
    # Extract every page of text
    for page_num in range(0, input_file.getNumPages()):
        text = input_file.getPage(page_num).extractText()
        text = text.encode("utf-8")  # convert text to unicode
        output_file.write(text)


# Exercise 3
# Save file without cover page
output_PDF = PdfFileWriter()
for page_num in range(1, input_file.getNumPages()):
    output_PDF.addPage(input_file.getPage(page_num))

output_file_name = os.path.join(path, "Output/The Whistling Gypsy un-covered.pdf")
with open(output_file_name, "wb") as output_file:
    output_PDF.write(output_file)
