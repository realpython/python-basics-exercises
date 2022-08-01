# 14.2 - Extract Pages From a PDF
# Solutions to review exercises

# ***********
# Exercise 1
#
# Extract the last page from the `Pride_and_Prejudice.pdf` file and
# save it to a new file called `last_page.pdf` in your home directory.
# ***********

# First import the classes and libraries needed
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

# Get the path to the `Pride_and_Prejudice.pdf` file. We'll assume you
# downloaded the solutions folder and extracted it into the home
# directory on your computer. If this is not the case, you'll need to
# update the path below.
pdf_path = Path.home() / "python-basics-exercises/ch14-interact-with-pdf-files/practice_files/Pride_and_Prejudice.pdf"

# Now you can create the PdfFileReader instance. Remember that
# PdfFileReader objects can only be instantiated with path strings, not
# Path objects!
pdf_reader = PdfFileReader(str(pdf_path))

# Use the .pages attribute to get an iterable over all pages in the
# PDF. The last page can be accessed with the index -1.
last_page = pdf_reader.pages[-1]

# Now you can create a PdfFileWriter instance and add the last page to it.
pdf_writer = PdfFileWriter()
pdf_writer.addPage(last_page)

# Finally, write the contents of pdf_writer to the file `last_page.pdf`
# in your home directory.
output_path = Path.home() / "last_page.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)


# ***********
# Exercise 2
#
# Extract all pages with even numbered _indices_ from the
# `Pride_and_Prejudice.pdf` and save them to a new file called
# `every_other_page.pdf` in your home directory.
# ***********

# There are several ways to extract pages with even numbered indices
# so we'll cover a few of them here.

# Solution A: Using a `for` loop
# ------------------------------

# One way to do it is with a `for` loop. We'll create a new PdfFileWriter
# instance, then loop over the numbers 0 up to the number of pages in the
# PDF, and add the pages with even indices to the PdfFileWriter instance.
pdf_writer = PdfFileWriter()
num_pages = pdf_reader.getNumPages()

for idx in range(num_pages):  # NOTE: idx is a common short name for "index"
    if idx % 2 == 0:  # Check that the index is even
        page = pdf_reader.getPage(idx)  # Get the page at the index
        pdf_writer.addPage(page)  # Add the page to `pdf_writer`

# Now write the contents of `pdf_writer` the the file `every_other_page.pdf`
# in your home directory
output_path = Path.home() / "every_other_page.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# Solution B: Slicing .`pages` with steps
# ------------------------------

# A more succinct, alghouth possibly more difficult to understand,
# solution involves slicing the `.pages` iterable. The indices start
# with 0 and every even index can be obtained by iterating over
# `.pages` in steps of size 2, so `.pages[::2]` is an iterable
# containing just the pages with even indices.
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages[::2]:
    pdf_writer.addPage(page)

# Now write the contents of `pdf_writer` the the file
# `every_other_page.pdf` in your home directory.
output_path = Path.home() / "every_other_page.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)


# ***********
# Exercise 3
#
# Split the `Pride_and_Prejudice.pdf` file into two new PDF files. The
# first file should contain the first 150 pages, and the second file
# should contain the remaining pages. Save both files in your home
# directory as `part_1.pdf` and `part_2.pdf`.
# ***********

# Start by creating two new PdfFileWriter instances.
part1_writer = PdfFileWriter()
part2_writer = PdfFileWriter()

# Next, create two new iterables containing the correct pages.
part1_pages = pdf_reader.pages[:150]  # Contains pages 0 - 149
part2_pages = pdf_reader.pages[150:]  # Contains pages 150 - last page

# Add the pages to their corresponding writers.
for page in part1_pages:
    part1_writer.addPage(page)

for page in part2_pages:
    part2_writer.addPage(page)

# Now write the contents of each writer to the files `part_1.pdf` and
# `part_2.pdf` in your home directory.
part1_output_path = Path.home() / "part_1.pdf"
with part1_output_path.open(mode="wb") as part1_output_file:
    part1_writer.write(part1_output_file)

part2_output_path = Path.home() / "part_2.pdf"
with part2_output_path.open(mode="wb") as part2_output_file:
    part2_writer.write(part2_output_file)
