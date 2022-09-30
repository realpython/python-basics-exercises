# 14.1 - Extract Text From a PDF
# Solutions to review exercises


# ***********
# Exercise 1
#
# In the Chapter 13 Practice Files directory there is a PDF file called
# `zen.pdf`. Create a `PdfFileReader` from this PDF.
# ***********

# Before you can do anything, you need to import the right objects from
# the PyPDF2 and pathlib libraries
from pathlib import Path
from PyPDF2 import PdfFileReader

# To create a PdfFileReader instance, you need to path to the PDF file.
# We'll assume you downloaded the solutions folder and are running this
# program from the solutions folder. If this is not the case, you'll
# need to update the path below.
pdf_path = Path.cwd() / "practice_files" / "zen.pdf"

# Now you can create the PdfFileReader instance. Remember that
# PdfFileReader objects can only be instantiated with path strings, not
# Path objects!
pdf_reader = PdfFileReader(str(pdf_path))


# ***********
# Exercise 2
#
# Using the `PdfFileReader` instance from Exercise 1, print the total
# number of pages in the PDF.
# ***********

# Use .getNumPages() to get the number of pages, then print the result
# using the print() built-in
num_pages = pdf_reader.getNumPages()
print(num_pages)


# ***********
# Exercise 3
#
# Print the text from the first page of the PDF in Exercise 1.
# ***********

# Use .getPage() to get the first page. Remember pages are indexed
# starting with 0!
first_page = pdf_reader.getPage(0)

# Then use .extractText() to extract the text
text = first_page.extractText()

# Finally, print the text
print(text)


# **NOTE**: The text in zen.pdf is from "The Zen Of Python" written by
# Tim Peters in 1999. The Zen is a collection of 19 guiding principles
# for developing with Python. The story goes that there are actually 20
# such principles, but only 19 were written down!
#
# You can see the original submission for The Zen of Python in PEP20:
# https://www.python.org/dev/peps/pep-0020/
#
# For some historical context surrounding The Zen, see:
# https://mail.python.org/pipermail/python-list/1999-June/001951.html
#
# Author Al Seigart has an interpretation of The Zen on his blog:
# https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/
#
# Moshe Zadka has another great article on The Zen:
# https://orbifold.xyz/zen-of-python.html
