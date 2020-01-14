# 13.4 - Rotating and Cropping PDF pages
# Solutions to review exercises

# ***********
# Exercise 1
#
# In the Chapter 13 Practice Files folder there is a PDF called
# `split_and_rotate.pdf`. Create a new PDF called `rotated.pdf` in your
# home directory containing the pages of `split_and_rotate.pdf` rotated
# counter-clockwise 90 degrees.
# ***********

from pathlib import Path 

from PyPDF2 import PdfFileReader, PdfFileWriter


pdf_path = Path.home() / "github/realpython/python-basics-exercises/" \
    "ch13-interact-with-pdf-files/practice_files/split_and_rotate.pdf"

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    rotated_page = page.rotateCounterClockwise(90)
    pdf_writer.addPage(rotated_page)

output_path = Path.home() / "rotated.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
