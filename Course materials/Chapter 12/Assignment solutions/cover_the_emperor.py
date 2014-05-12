# 12.2 cover_the_emperor.py
# Add a cover sheet to a PDF; save the full output as a new PDF

import os
from pyPdf import PdfFileReader, PdfFileWriter

path = "C:/Real Python/Course materials/Chapter 8/Practice files"
inputFileName1 = os.path.join(path, "Emperor cover sheet.pdf")
inputFile1 = PdfFileReader(file(inputFileName1, "rb"))
inputFileName2 = os.path.join(path, "The Emperor.pdf")
inputFile2 = PdfFileReader(file(inputFileName2, "rb"))
outputPDF = PdfFileWriter()

# Read in all pages from the cover sheet PDF file
for pageNum in range(0, inputFile1.getNumPages()):
    page = inputFile1.getPage(pageNum)
    outputPDF.addPage(page)

# Read in all pages from "The Emperor.pdf" into the same output file
for pageNum in range(0, inputFile2.getNumPages()):
    page = inputFile2.getPage(pageNum)
    outputPDF.addPage(page)

# Output the results into a new PDF
outputFileName = os.path.join(path, "Output/The Covered Emperor.pdf")
outputFile = file(outputFileName, "wb")
outputPDF.write(outputFile)
outputFile.close()
