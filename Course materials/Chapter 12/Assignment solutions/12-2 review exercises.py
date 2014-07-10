# 12.2 review exercises

import os
import copy
from pyPdf import PdfFileReader, PdfFileWriter

path = "C:/Real Python/Course materials/Chapter 12/Practice files"
inputFileName = os.path.join(path, "Walrus.pdf")
inputFile = PdfFileReader(file(inputFileName, "rb"))
outputPDF = PdfFileWriter()

inputFile.decrypt("IamtheWalrus")  # decrypt the input file

for pageNum in range(0, inputFile.getNumPages()):
    # rotate pages (call everything pageLeft for now; will make a copy)
    pageLeft = inputFile.getPage(pageNum)
    pageLeft.rotateCounterClockwise(90)

    pageRight = copy.copy(pageLeft)  # split each page in half
    upperRight = pageLeft.mediaBox.upperRight  # get original page corner

    # crop and add left-side page
    pageLeft.mediaBox.upperRight = (upperRight[0]/2, upperRight[1])
    outputPDF.addPage(pageLeft)
    # crop and add right-side page
    pageRight.mediaBox.upperLeft = (upperRight[0]/2, upperRight[1])
    outputPDF.addPage(pageRight)

# save new pages to an output file
outputFileName = os.path.join(path, "Output/Updated Walrus.pdf")
with file(outputFileName, "wb") as outputFile:
    outputPDF.write(outputFile)
