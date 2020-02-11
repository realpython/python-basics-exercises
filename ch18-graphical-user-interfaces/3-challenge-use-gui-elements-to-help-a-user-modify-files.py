# 18.3 - Challenge: Use GUI Elements to Help a User Modify Files
# Solution to challenge

# save part of a PDF based on a user-supplied page range using a GUI

import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

# 1. Ask the user to select a PDF file to open.
input_file_path = gui.fileopenbox("", "Select a PDF to trim...", "*.pdf")

# 2. If no PDF file is chosen, exit the program.
if input_file_path is None:
    exit()

# 3. Ask for a starting page number.
page_start = gui.enterbox(
    "Enter the number of the first page to use:", "Where to begin?"
)

# 4. If the user does not enter a starting page number, exit the program.
if page_start is None:
    exit()

# 5. Valid page numbers are positive integers. If the user enters an invalid page number:
#     - Warn the user that the entry is invalid
#     - Return to step 3.
# This solution also checks that the starting page number is not beyond the last page of the PDF!# 3. Asl for a starting page number.
input_file = PdfFileReader(input_file_path)  # Open the PDF
total_pages = input_file.getNumPages()  # Get the total number of pages
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

# 6. Ask for an ending page number
page_end = gui.enterbox(
    "Enter the number of the last page to use:", "Where to end?"
)

# 7. If the user does not enter and ending page number, exit the program.
if page_end is None:  # exit on "Cancel"
    exit()

# 8. If the user enters an invalid page number:
#     - Warn the user that the entry is invalid
#     - Return to step 6.
# This solution also check that the ending page number is not less than the starting
# page number, and that it is not greater than the last page in the PDF
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

# 9. Ask for the location to save the extracted pages
output_file_path = gui.filesavebox("", "Save the trimmed PDF as...", "*.pdf")

# 10. If the user does not select a save location, exit the program.
if output_file_path is None:
    exit()

# 11. If the chosen save location is the same as the input file path:
#      - Warn the user that they can not overwrite the input file.
#      - Return the step 9.
while input_file_path == output_file_path:  # cannot use same file as input
    gui.msgbox(
        "Cannot overwrite original file!", "Please choose another file..."
    )
    output_file_path = gui.filesavebox(
        "", "Save the trimmed PDF as...", "*.pdf"
    )
    if output_file_path is None:
        exit()

# 12. Perform the page extraction
output_PDF = PdfFileWriter()

for page_num in range(int(page_start) - 1, int(page_end)):
    page = input_file.getPage(page_num)
    output_PDF.addPage(page)

with open(output_file_path, "wb") as output_file:
    output_PDF.write(output_file)
