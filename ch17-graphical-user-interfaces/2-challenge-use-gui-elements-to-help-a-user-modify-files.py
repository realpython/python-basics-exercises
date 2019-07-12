# 17.2 - Challenge: Use GUI Elements to Help a User Modify Files
# Solution to challenge

# save part of a PDF based on a user-supplied page range using a GUI

import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

# let the user choose an input file
input_file_path = gui.fileopenbox("", "Select a PDF to trim...", "*.pdf")
if input_file_path is None:  # exit on "Cancel"
    exit()

# get the page length of the input file
input_file = PdfFileReader(input_file_path)
total_pages = input_file.getNumPages()

# let the user choose a beginning page
page_start = gui.enterbox(
    "Enter the number of the first page to use:", "Where to begin?"
)
if page_start is None:  # exit on "Cancel"
    exit()
# check for possible problems and try again:
#    1) input page number isn't a (non-negative) digit
# or 2) input page number is 0
# or 3) page number is greater than total number of pages
while (
    not page_start.isdigit()
    or page_start == "0"
    or int(page_start) > total_pages
):
    gui.msgbox("Please provide a valid page number.", "Whoops!")
    page_start = gui.enterbox(
        "Enter the number of the first page to use:", "Where to begin?"
    )
    if page_start is None:  # exit on "Cancel"
        exit()

# let the user choose an ending page
page_end = gui.enterbox(
    "Enter the number of the last page to use:", "Where to end?"
)
if page_end is None:  # exit on "Cancel"
    exit()
# check for possible problems and try again:
#    1) input page number isn't a (non-negative) digit
# or 2) input page number is 0
# or 3) input page number is greater than total number of pages
# or 4) input page number for end is less than page number for beginning
while (
    not page_end.isdigit()
    or page_end == "0"
    or int(page_end) > total_pages
    or int(page_end) < int(page_start)
):
    gui.msgbox("Please provide a valid page number.", "Whoops!")
    page_end = gui.enterbox(
        "Enter the number of the last page to use:", "Where to end?"
    )
    if page_end is None:  # exit on "Cancel"
        exit()

# let the user choose an output file name
output_file_path = gui.filesavebox("", "Save the trimmed PDF as...", "*.pdf")
while input_file_path == output_file_path:  # cannot use same file as input
    gui.msgbox(
        "Cannot overwrite original file!", "Please choose another file..."
    )
    output_file_path = gui.filesavebox(
        "", "Save the trimmed PDF as...", "*.pdf"
    )
if output_file_path is None:
    exit()  # exit on "Cancel"

# read in file, write new file with trimmed page range and save the new file
output_PDF = PdfFileWriter()
# subtract 1 from supplied start page number to get correct index value
for page_num in range(int(page_start) - 1, int(page_end)):
    page = input_file.getPage(page_num)
    output_PDF.addPage(page)

with open(output_file_path, "wb") as output_file:
    output_PDF.write(output_file)
