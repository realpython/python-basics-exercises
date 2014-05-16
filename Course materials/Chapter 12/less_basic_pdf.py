from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
 
xmargin = 3.2*inch
ymargin = 6*inch
 
c = canvas.Canvas("hello_again.pdf", pagesize=letter)
 
c.setLineWidth(1)
c.drawString(xmargin, ymargin, "Hello World from ReportLab!")

c.save()