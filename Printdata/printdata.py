import customtkinter as ctk
import tkcalendar as tkc
import os
import psycopg2
import win32api
import win32print
from pathlib import Path
import fitz
from PIL import Image, ImageTk
from datetime import date

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph

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

class Right_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def PrintPDF(event):
            win32api.ShellExecute (0, "print", os.getcwd() + "\\allpdf\\menu.pdf", win32print.GetDefaultPrinter(), ".", 0)

        self.top_bar = ctk.CTkFrame(self, width=kwargs["width"], height=40)
        self.download_btn = ctk.CTkButton(self.top_bar, width=kwargs["width"], height=40, text="確認列印", font=("microsoft yahei", 20, 'bold'))
        self.download_btn.bind("<Button-1>", PrintPDF)
        self.main_body = PDFViewer(self, width=kwargs["width"]-20, height=kwargs["height"]-80)  

        self.download_btn.pack()
        self.top_bar.pack()
        self.main_body.pack()

class Left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def ReadPDF(event):
            conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            #conn = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            with conn:
                cur = conn.cursor()
                cur.execute(f"SELECT order_form.o_id,order_form.c_id,goods.item_id,goods.item_name,goods.date,goods.specification,goods.size,\
                            goods.price,goods.quantity,goods.sub_total,goods.remark  FROM order_form JOIN goods ON order_form.o_id=goods.o_id \
                            WHERE order_form.c_id = '{self.search_id.get()}' AND (goods.date BETWEEN SYMMETRIC '{self.cal1.get_date()}' AND '{self.cal2.get_date()}')")
                result = cur.fetchall()

                cur.execute(f"SELECT * FROM customer WHERE customer.c_id = '{self.search_id.get()}'")
                customer = cur.fetchall()

            styles = getSampleStyleSheet()
            pdfmetrics.registerFont(TTFont('microsoft.ttf', "./Printdata/microsoft.ttf"))

            styletitle = ParagraphStyle(
                'styleNormalCustom',
                fontName='microsoft.ttf',
                parent=styles["Title"],
                fontSize=12,
                leading=18,
                spaceAfter=2,
                spaceBefore=2,
                alignment=TA_LEFT,
            )

            stylenormal = ParagraphStyle(
                'styleNormalCustom',
                fontName='microsoft.ttf',
                parent=styles["Normal"],
                fontSize=10,
                leading=20,
                spaceAfter=2,
                spaceBefore=2,
                alignment=TA_LEFT,
            ) 

            if not(os.path.exists("./allpdf")):
                os.mkdir("allpdf")
            os.chdir("./allpdf")

            fileName  = "menu.pdf"
            pdfTemplate = SimpleDocTemplate(fileName)

            story = []
            space = "&nbsp;"
            story.append(Paragraph(f"聯絡人：{space*42}電話：{space*33}統一編號：{space}", styletitle))
            story.append(Paragraph(f"地址：果菜市場{space*75}列印日期：{date.today()}", styletitle))
            story.append(Paragraph("&nbsp;"))
            story.append(Paragraph(f"客戶姓名：{customer[0][1]}{space*38}地址：{customer[0][3]}", styletitle))
            story.append(Paragraph(f"電話：{customer[0][2]}{space*30}備註：{customer[0][4]}", styletitle))
            story.append(Paragraph("&nbsp;"))
            story.append(Paragraph("-"*130))
            story.append(Paragraph(f"品項名稱{space*15}規格{space*10}大小{space*10}數量{space*10}單價{space*10}小計{space*15}備註{space}", stylenormal))
            story.append(Paragraph("-"*130))

            pre_s_num = []
            price = 0
            for row in result:
                if row[0] != pre_s_num and pre_s_num != []:
                    story.append(Paragraph(f"總計：{price}", stylenormal))
                    price = 0

                if row[0] != pre_s_num:
                    story.append(Paragraph("&nbsp;"))
                    story.append(Paragraph(f"銷貨日期：{str(row[4]).rstrip()}{space*15}銷貨單編號：{str(row[0]).rstrip()}", stylenormal))
                
                story.append(Paragraph(f"{str(row[3]).rstrip()}{space*20}{str(row[5]).rstrip()}{space*20}{str(row[6]).rstrip()}\
                                     {space*20}{str(row[7]).rstrip()}{space*15}{str(row[8]).rstrip()}{space*15}{str(row[9]).rstrip()}\
                                     {space*20}{str(row[10]).rstrip()}", stylenormal))
                price += int(row[9])
                pre_s_num = row[0]
            story.append(Paragraph(f"總計：{price}", stylenormal))

            pdfTemplate.build(story)

            os.chdir("../")

            self.right.place_forget()
            self.right = Right_part(self,width=kwargs["width"]-300, height=kwargs["height"])
            self.right.place(x=280,y=20)
            
        self.search_id = ctk.CTkEntry(self, width=210, height=50, placeholder_text="客戶代號")
        self.search_id.bind("<Return>", ReadPDF)
        self.cal1 = tkc.DateEntry(self, font=("microsoft yahei", 20), year=2000, month=1, day=1, date_pattern="yyyy-mm-dd")
        self.cal2 = tkc.DateEntry(self, font=("microsoft yahei", 20), date_pattern="yyyy-mm-dd")
        self.confirm = ctk.CTkButton(self, font=("microsoft yahei", 20, 'bold'), width=200, height=40, text="確認查詢")
        self.confirm.bind("<Button-1>", ReadPDF)
        
        self.right = Right_part(self,width=kwargs["width"]-300, height=kwargs["height"])
        
        self.search_id.place(x=30,y=40)
        self.cal1.place(x=30,y=250)
        self.cal2.place(x=30,y=300)
        self.confirm.place(x=30,y=kwargs["height"]-100)
        self.right.place(x=280,y=20)     

class Printdata_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.left = Left_part(self,width=kwargs["width"]-40,height=kwargs["height"]-90,fg_color="#FFFFFF")
        self.left.grid(row=0,column=0,padx=15,pady=10)