# 12.1 review exercises


import os
from pyPdf import PdfFileReader, PdfFileWriter

path = "C:/Real Python/Course materials/Chapter 12/Practice files"
input_file_name = os.path.join(path, "The Whistling Gypsy.pdf")
input_file = PdfFileReader(file(input_file_name, "rb"))

# Display meta-data about file
print "Title:", input_file.getDocumentInfo().title
print "Author:", input_file.getDocumentInfo().author
print "Number of pages:", input_file.getNumPages()

# Specify and open output text file
output_file_name = os.path.join(path, "Output/The Whistling Gypsy.txt")
with open(output_file_name, "w") as output_file:
    # Extract every page of text
    for page_num in range(0, input_file.getNumPages()):
        text = input_file.getPage(page_num).extractText()
        text = text.encode("utf-8")  # convert text to unicode
        output_file.write(text)

# Save file without cover page
output_PDF = PdfFileWriter()
for page_num in range(1, input_file.getNumPages()):
    output_PDF.addPage(input_file.getPage(page_num))

output_file_name = os.path.join(path, "Output/The Whistling Gypsy un-covered.pdf")
with file(output_file_name, "wb") as output_file:
    output_PDF.write(output_file)
