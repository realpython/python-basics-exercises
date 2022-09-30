# 14.4 - Concatenating and Merging PDFs
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


BASE_PATH = Path.cwd() / "practice_files"

pdf_paths = [BASE_PATH / "merge1.pdf", BASE_PATH / "merge2.pdf"]
pdf_merger = PdfFileMerger()

for path in pdf_paths:
    pdf_merger.append(str(path))

output_path = Path.home() / "concatenated.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_merger.write(output_file)


# ***********
# Exercise 2
#
# Using the same `PdfFileMerger` instance from exercise 1, merge the
# file `merge3.pdf` in-between the pages from `merge1.pdf` and
# `merge2.pdf` using `.merge()`.
#
# The final result should be a PDF with three pages. The first page
# should have the number `1` on it, the second should have `2`, and the
# third should have `3`.
# ***********

pdf_merger = PdfFileMerger()
pdf_merger.append(str(output_path))

pdf_path = BASE_PATH / "merge3.pdf"
pdf_merger.merge(1, str(pdf_path))

output_path = Path.home() / "merged.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_merger.write(output_file)
