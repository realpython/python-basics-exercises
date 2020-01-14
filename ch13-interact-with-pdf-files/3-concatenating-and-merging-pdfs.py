# 13.3 - Concatenating and Merging PDFs
# Solutions to review exercises

# ***********
# Exercise 1
#
# In the Chapter 13 Practice Files directory there are three PDFs called
# `merge1.pdf`, `merge2.pdf`, and `merge3.pdf`. Using a `PdfFileMerger`
# instance, concatenate the two files `merge1.pdf` and `merge2.pdf`
# using`.append()`.
# ***********

from pathlib import Path

from PyPDF2 import PdfFileMerger


BASE_PATH = Path.home() / "github/realpython/python-basics-exercises/" \
    "ch13-interact-with-pdf-files/practice_files"

pdf_paths = [BASE_PATH / "merge1.pdf", BASE_PATH / "merge2.pdf"]
pdf_merger = PdfFileMerger()

for path in pdf_paths:
    pdf_merger.append(str(path))

output_path = Path.home() / "concatenated.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_merger.write(output_file)
