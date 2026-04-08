from pypdf import PdfWriter
from reportlab.pdfgen import canvas

def create_dummy_pdf(filename, text):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, text)
    c.save()

if __name__ == "__main__":
    create_dummy_pdf("test1.pdf", "This is page 1 from file 1")
    create_dummy_pdf("test2.pdf", "This is page 1 from file 2")
    print("Created test1.pdf and test2.pdf")
