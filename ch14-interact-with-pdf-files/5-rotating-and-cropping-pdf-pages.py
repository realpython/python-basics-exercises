# 14.5 - Rotating and Cropping PDF pages
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


pdf_path = Path.cwd() / "practice_files" / "split_and_rotate.pdf"

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    rotated_page = page.rotateCounterClockwise(90)
    pdf_writer.addPage(rotated_page)

output_path = Path.home() / "rotated.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)


# ***********
# Exercise 2
#
# Using the `rotated.pdf` file you created in exercise 1, split each
# page of the PDF vertically in the middle. Create a new PDF called
# `split.pdf` in your home directory containing all of the split pages.
#
# `split.pdf` should have four pages with the numbers `1`, `2`, `3`,
# and `4`, in order.
# ***********
import copy

pdf_path = Path.home() / "rotated.pdf"

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    # Calculate the coordinates at the top center of the page
    upper_right_coords = page.mediaBox.upperRight
    center_coords = (upper_right_coords[0] / 2, upper_right_coords[1])
    # Create two copies of the page, one for the left side and one for
    # the right side
    left_page = copy.deepcopy(page)
    right_page = copy.deepcopy(page)
    # Crop the pages by setting the upper right corner coordinates
    # of the left hand page and the upper left corner coordinates of
    # the right hand page to the top center coordinates
    left_page.mediaBox.upperRight = center_coords
    right_page.mediaBox.upperLeft = center_coords
    # Add the cropped pages to the PDF writer
    pdf_writer.addPage(left_page)
    pdf_writer.addPage(right_page)

output_path = Path.home() / "split.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
