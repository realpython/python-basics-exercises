# 14.5 - Challenge: PdfFileSplitter Class
# Solution to challenge

from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter


class PdfFileSplitter:
    """Class for splitting a PDF into two files."""

    def __init__(self, pdf_path):
        # Open the PDF file with a new PdfFileReader instance
        self.pdf_reader = PdfFileReader(pdf_path)
        # Initialize the .writer1 and .writer2 attributes to None
        self.writer1 = None
        self.writer2 = None

    def split(self, breakpoint):
        """Split the PDF into two PdfFileWriter instances"""
        # Set .writer1 and .writer2 to new PdfFileWriter intances
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()
        # Add all pages up to, but not including, the breakpoint
        # to writer1
        for page in self.pdf_reader.pages[:breakpoint]:
            self.writer1.addPage(page)
        # Add all the remaining pages to writer2
        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.addPage(page)

    def write(self, filename):
        """Write both PdfFileWriter instances to files"""
        # Write the first file to <filename>_1.pdf
        with Path(filename + "_1.pdf").open(mode="wb") as output_file:
            self.writer1.write(output_file)
        # Write the second file to <filename>_2.pdf
        with Path(filename + "_2.pdf").open(mode="wb") as output_file:
            self.writer2.write(output_file)


# Split the Pride_and_Prejudice.pdf file into two PDFs, the first
# containing the first 150 pages, and the second containing the
# remaining pages.
pdf_splitter = PdfFileSplitter("ch14-interact-with-pdf-files/practice_files/Pride_and_Prejudice.pdf")
pdf_splitter.split(breakpoint=150)
pdf_splitter.write("pride_split")
