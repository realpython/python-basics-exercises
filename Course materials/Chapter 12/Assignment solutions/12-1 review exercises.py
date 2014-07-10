# 12.1 review exercises


import os
from pyPdf import PdfFileReader, PdfFileWriter

path = "C:/Real Python/Course materials/Chapter 12/Practice files"
inputFileName = os.path.join(path, "The Whistling Gypsy.pdf")
inputFile = PdfFileReader(file(inputFileName, "rb"))

# Display meta-data about file
print "Title:", inputFile.getDocumentInfo().title
print "Author:", inputFile.getDocumentInfo().author
print "Number of pages:", inputFile.getNumPages()

# Specify and open output text file
outputFileName = os.path.join(path, "Output/The Whistling Gypsy.txt")
with open(outputFileName, "w") as outputFile:
    # Extract every page of text
    for pageNum in range(0, inputFile.getNumPages()):
        text = inputFile.getPage(pageNum).extractText()
        text = text.encode("utf-8")  # convert text to unicode
        outputFile.write(text)

# Save file without cover page
outputPDF = PdfFileWriter()
for pageNum in range(1, inputFile.getNumPages()):
    outputPDF.addPage(inputFile.getPage(pageNum))

outputFileName = os.path.join(path, "Output/The Whistling Gypsy un-covered.pdf")
with file(outputFileName, "wb") as outputFile:
    outputPDF.write(outputFile)
