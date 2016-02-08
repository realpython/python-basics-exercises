from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
# c.drawString(100,100, "Hello World")
c.drawString(250, 500, "Hello World")
c.save()
