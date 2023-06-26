import customtkinter as ctk
import tkcalendar as tkc
import psycopg2
import requests
import os
import win32api
import win32print
from datetime import date
from pathlib import Path
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont


class Right_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def previewPDF(choice):
            self.temp_fn = os.getcwd() + "\\allpdf\\" + choice
            win32api.ShellExecute(0,"open",self.temp_fn,"",".",0)
        def printPDF(event):
            win32api.ShellExecute (0,"print",self.temp_fn,win32print.GetDefaultPrinter(),".",0)
        dir_path = os.getcwd() + r"\\allpdf"
        all_pdf_list = os.listdir(dir_path)
        self.temp_fn = ""
        self.top_bar = ctk.CTkFrame(self,width=kwargs["width"],height=40)
        self.main_body = ctk.CTkFrame(self,width=kwargs["width"]-20,height=kwargs["height"]-80)
        self.download_lbl = ctk.CTkLabel(self.top_bar,width=kwargs["width"],height=40,text="選擇後預覽訂單")
        self.download_btn = ctk.CTkButton(self.main_body,text="確認列印")
        self.download_btn.bind("<Button-1>", printPDF)
        self.op_menu = ctk.CTkOptionMenu(self.main_body,values=all_pdf_list,command=previewPDF)
        self.op_menu.pack()
        self.download_btn.pack(pady=10)
        self.top_bar.pack()
        self.main_body.pack()
        self.download_lbl.pack()

class Left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def download(event):
            pdf = Document()
            
            conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            # conn = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            with conn:
                cur = conn.cursor()
                cur.execute(f"SELECT order_form.o_id,order_form.c_id,goods.item_id,goods.item_name,goods.date,goods.specification,goods.size,\
                            goods.price,goods.quantity,goods.sub_total,goods.remark  FROM order_form JOIN goods ON order_form.o_id=goods.o_id \
                            WHERE order_form.c_id = '{self.search_id.get()}' AND (goods.date BETWEEN SYMMETRIC '{self.cal1.get_date()}' AND '{self.cal2.get_date()}')")
                result = cur.fetchall()
            page = Page()
            pdf.add_page(page)

            layout = SingleColumnLayout(page)
            # download and store the font
            # this is obviously not needed if you already have a ttf font on disk
            if not(os.path.exists('./Printdata/microsoft.ttf')):
                font_path: Path = Path(__file__).parent / "microsoft.ttf"
                with open(font_path, "wb") as font_file_handle:
                    font_file_handle.write(
                        requests.get(
                            "https://drive.google.com/u/0/uc?id=1RdcCu1_CYdmXRrbq8J2aVfN9t5JSgq6-&export=download",
                            stream=True,
                        ).content
                    )
            else:
                # construct the Font object
                font_path: Path = Path(__file__).parent / "microsoft.ttf"
         
            custom_font: Font = TrueTypeFont.true_type_font_from_file(font_path)
            layout.add(Paragraph("品項名稱 規格 大小 數量 單價 小計 備註", respect_spaces_in_text=True, border_top=True,border_bottom=True,border_width=1,text_alignment=Alignment.CENTERED))
            pre_s_num = result[0][0]
            count = 0
            for i in result:
                if i[0] != pre_s_num or count==0:
                    layout.add(Paragraph("------------------------------------------------------------------------------------"))
                    layout.add(Paragraph(f"Date:{str(i[4]).rstrip()}Serial Number:{str(i[0]).rstrip()}Price:{str(i[7]).rstrip()}",respect_spaces_in_text=True))
                layout.add(Paragraph(f"{str(i[3]).rstrip()}      {str(i[5]).rstrip()}       {str(i[6]).rstrip()}\
                                     {str(i[7]).rstrip()}      {str(i[8]).rstrip()}      {str(i[9]).rstrip()}      \
                                     {str(i[10]).rstrip()}",font=custom_font,respect_spaces_in_text=True))
                pre_s_num = i[0]
                count += 1
            layout.add(Paragraph("------------------------------------------------------------------------------------"))

            if not(os.path.exists("./allpdf")):
                os.mkdir("allpdf")
            os.chdir("./allpdf")
            
            td = date.today()
            filename = f"{self.search_id.get()}{td.year}{td.month}{td.day}.pdf"
            with open(Path(filename), "wb") as pdf_file_handle:
                PDF.dumps(pdf_file_handle, pdf)
            os.chdir("../")
        def printPDF(event):
            dir_path = os.getcwd() + r"\\allpdf"
            fn = os.getcwd() + "\\allpdf\\" + os.listdir(dir_path)[0]
            win32api.ShellExecute (0,"print",fn,win32print.GetDefaultPrinter(),".",0)
        self.search_id = ctk.CTkEntry(self,width=210,height=50,placeholder_text="客戶代號")
        self.cal1 = tkc.DateEntry(self, font=("microsoft yahei", 20))
        self.cal2 = tkc.DateEntry(self, font=("microsoft yahei", 20))
        self.confirm = ctk.CTkButton(self,width=200,height=40,text="確認查詢",font=("Arial",20))
        self.confirm.bind("<Button-1>", download)
        self.reset = ctk.CTkButton(self,width=200,height=40,text="重設查詢",font=("Arial",20))
        
        self.right = Right_part(self,width=kwargs["width"]-300,height=kwargs["height"])
        self.right.download_btn.bind("<Button-1>", printPDF)
        
        self.search_id.place(x=30,y=20)
        self.cal1.place(x=30,y=200)
        self.cal2.place(x=30,y=250)
        self.confirm.place(x=30,y=kwargs["height"]-150)
        self.reset.place(x=30,y=kwargs["height"]-100)
        self.right.place(x=280,y=20)     

class Printdata_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def reset(event):
            self.left.place_forget()
            self.left = Left_part(self,width=kwargs["width"]-40,height=kwargs["height"]-90,fg_color="#EEEEEE")
            self.left.grid(row=0,column=0,padx=15,pady=10)
            self.left.reset.bind("<Button-1>", reset)


        self.left = Left_part(self,width=kwargs["width"]-40,height=kwargs["height"]-90,fg_color="#EEEEEE")
        self.left.grid(row=0,column=0,padx=15,pady=10)
        self.left.reset.bind("<Button-1>", reset)