# 方便地获取整个PDF页面并将它们转换为图像。
# pip install PyMuPDF
import fitz
def pdf_to_images(pdf_file):
    doc = fitz.open(pdf_file)
    for p in doc:
        pix = p.get_pixmap()
        output = f"page{p.number}.png"
        pix.writePNG(output)
pdf_to_images("test.pdf")