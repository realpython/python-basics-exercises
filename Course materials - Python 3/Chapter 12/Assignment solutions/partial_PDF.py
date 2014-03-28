# 12.1 partial_PDF.py
# save part of a PDF based on a user-supplied page range using a GUI

from easygui import *
from pyPdf import PdfFileReader, PdfFileWriter

# let the user choose an input file
inputFileName = fileopenbox("", "Select a PDF to trim...", "*.pdf")
if inputFileName == None: # exit on "Cancel"
    exit()

# get the page length of the input file
inputFile = PdfFileReader(file(inputFileName, "rb"))
totalPages = inputFile.getNumPages()

# let the user choose a beginning page
pageStart = enterbox("Enter the number of the first page to use:", "Where to begin?")
if pageStart==None: # exit on "Cancel"
    exit()
# check for possible problems and try again:
#    1) input page number isn't a (non-negative) digit
# or 2) input page number is 0
# or 3) page number is greater than total number of pages
while not pageStart.isdigit() or pageStart=="0" or int(pageStart) > totalPages:
    msgbox("Please provide a valid page number.", "Whoops!")
    pageStart = enterbox("Enter the number of the first page to use:", "Where to begin?")
    if pageStart==None: # exit on "Cancel"
        exit()

# let the user choose an ending page
pageEnd = enterbox("Enter the number of the last page to use:", "Where to end?")
if pageEnd==None: # exit on "Cancel"
    exit()
# check for possible problems and try again:
#    1) input page number isn't a (non-negative) digit
# or 2) input page number is 0
# or 3) input page number is greater than total number of pages
# or 4) input page number for end is less than page number for beginning
while not pageEnd.isdigit() or pageEnd=="0" \
      or int(pageEnd) > totalPages or int(pageEnd) < int(pageStart):
    msgbox("Please provide a valid page number.", "Whoops!")
    pageEnd = enterbox("Enter the number of the last page to use:", "Where to end?")
    if pageEnd==None: # exit on "Cancel"
        exit()

# let the user choose an output file name
outputFileName = filesavebox("", "Save the trimmed PDF as...", "*.pdf")
while inputFileName == outputFileName: # cannot use same file as input
    msgbox("Cannot overwrite original file!", "Please choose another file...")
    outputFileName = filesavebox("", "Save the trimmed PDF as...", "*.pdf")
if outputFileName == None:
    exit() # exit on "Cancel"

# read in file, write new file with trimmed page range and save the new file
outputPDF = PdfFileWriter()
# subtract 1 from supplied start page number to get correct index value
for pageNum in range(int(pageStart)-1, int(pageEnd)):
    page = inputFile.getPage(pageNum)
    outputPDF.addPage(page)
outputFile = file(outputFileName, "wb")
outputPDF.write(outputFile)
outputFile.close()
