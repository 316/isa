#*-* coding: utf-8 *-*
from reportlab.pdfgen import canvas

def example():
    c=canvas.Canvas("example.pdf")
    c.drawString(100,750,"Welcome to Reportlab!")
    c.save()
    return response.download(c)
