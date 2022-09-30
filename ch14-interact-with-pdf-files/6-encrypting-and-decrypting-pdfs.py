# 14.6 - Encrypting and Decrypting PDFs
# Solutions to review exercises

# ***********
# Exercise 1
#
# In the Chapter 13 Practice Files folder there is a PDF file called
# `top_secret.pdf`. Encrypt the file with the user password
# `Unguessable`. Save the encrypted file as in your home directory as
# `top_secret_encrypted.pdf`.
# ***********

from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter


pdf_path = Path.cwd() / "practice_files" / "top_secret.pdf"

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_pwd="Unguessable")

output_path = Path.home() / "top_secret_encrypted.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)


# ***********
# Exercise 2
#
# Open the `top_secret_encrpyted.pdf` file you created in exercise 1,
# decrypt it, and print the text on the first page of the PDF.
# ***********

pdf_path = Path.home() / "top_secret_encrypted.pdf"
pdf_reader = PdfFileReader(str(pdf_path))

pdf_reader.decrypt("Unguessable")

first_page = pdf_reader.getPage(0)
print(first_page.extractText())
