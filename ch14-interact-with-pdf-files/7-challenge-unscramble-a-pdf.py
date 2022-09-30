# 14.7 - Challenge: Unscramble a PDF
# Solution to challenge

from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter


def get_page_text(page):
    return page.extractText()


pdf_path = Path.cwd() / "practice_files" / "scrambled.pdf"

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

pages = list(pdf_reader.pages)
pages.sort(key=get_page_text)

for page in pages:
    rotation_degrees = page["/Rotate"]
    if rotation_degrees != 0:
        page.rotateCounterClockwise(rotation_degrees)
    pdf_writer.addPage(page)

output_path = Path.home() / "unscrambled.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
