import customtkinter as ctk
import os
from PIL import Image, ImageTk
import fitz

class PDFViewer(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def pdf_to_img(page_num):
            page = self.doc.load_page(page_num)
            pix = page.get_pixmap(matrix= self.mat)
            return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        def show_image(page_num):
            try:
                assert page_num >= 0 and page_num < len(self.doc)
                im = pdf_to_img(page_num)
                img_tk = ImageTk.PhotoImage(im)
                panel = ctk.CTkLabel(self, text= "", image=img_tk)
                panel.pack()
            except:
                pass

        filename = "./allpdf/menu.pdf"
        if os.path.exists(filename):
            self.doc = fitz.open(filename)
            zoom = 2
            self.mat = fitz.Matrix(zoom, zoom)
            for num in range(len(self.doc)):
                show_image(num)

            self.doc.close()