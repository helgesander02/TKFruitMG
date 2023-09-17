import customtkinter as ctk
import tkcalendar as tkc
import tkinter as tk
import os
import psycopg2
from datetime import date
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table

from .pdfviewer import PDFViewer
from .style import normaltbstyle, titletbstyle, columntbstyle 

class Right_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]

        self.top_bar = ctk.CTkFrame(self, width=self.w, height=40)
        self.download_btn = ctk.CTkButton(self.top_bar, width=self.w, height=40, text="確認列印", font=("microsoft yahei", 20, 'bold'))
        self.download_btn.bind("<Button-1>", self.PrintPDF)
        self.main_body = PDFViewer(self, width=self.w-20, height=self.h-80)  

        self.download_btn.pack()
        self.top_bar.pack()
        self.main_body.pack()

    def PrintPDF(self, event):
        os.system(f"print /D:'\\computer\printer' '{os.getcwd()}//allpdf//menu.pdf'")

class Left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  
        self.w = kwargs["width"]
        self.h = kwargs["height"]      
        self.search_id = ctk.CTkEntry(self, width=210, height=50, placeholder_text="客戶代號")
        self.search_id.bind("<Return>", self.ReadPDF)
        self.toplevel = None
        self.cal1 = tkc.DateEntry(self, font=("microsoft yahei", 20), year=2000, month=1, day=1, date_pattern="yyyy-mm-dd")
        self.cal2 = tkc.DateEntry(self, font=("microsoft yahei", 20), date_pattern="yyyy-mm-dd")

        self.confirm = ctk.CTkButton(self, font=("microsoft yahei", 20, 'bold'), width=200, height=40, text="確認查詢")
        self.confirm.bind("<Button-1>", self.ReadPDF)
        
        self.right = Right_part(self,width=self.w-300, height=self.h)
        
        self.search_id.place(x=30,y=40)
        self.cal1.place(x=30,y=250)
        self.cal2.place(x=30,y=300)
        self.confirm.place(x=30,y=self.h-100)
        self.right.place(x=280,y=20) 

    def ReadPDF(self, event):
        try:
            if self.search_id.get() == "":
                tk.messagebox.showinfo(title='', message="請輸入客戶代號!!")

            else:
                con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
                #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
                with con:
                    cur = con.cursor()
                    cur.execute(f"SELECT order_form.o_id, goods.item_name, goods.date, goods.specification, goods.size, goods.price, goods.quantity, goods.sub_total, goods.remark  \
                                    FROM order_form JOIN goods ON order_form.o_id=goods.o_id \
                                    WHERE order_form.c_id = '{self.search_id.get()}' \
                                    AND (goods.date BETWEEN SYMMETRIC '{self.cal1.get_date()}' AND '{self.cal2.get_date()}')")
                    result = cur.fetchall()

                    cur.execute(f"SELECT * FROM customer WHERE customer.c_id = '{self.search_id.get()}'")
                    customer = cur.fetchall()
                
                if not(os.path.exists("./allpdf")):
                    os.mkdir("allpdf")
                os.chdir("./allpdf")

                fileName  = "menu.pdf"
                pdfTemplate = SimpleDocTemplate(fileName)

                story = []
                #------------------------------------------------------------------------------------------------------------------
                space = "&nbsp;"

                titledataList = [
                    ["聯絡人：", "", "電話：", "", "統一編號：", ""],
                    ["地址：", "果菜市場：", "", "", "", ""],
                    ["客戶名稱：", f"{customer[0][1]}", "聯絡人：", "", "電話：", f"{customer[0][2]}"],
                    ["地址：", f"{customer[0][3]}", "列印日期：", f"{date.today()}", "頁次：", ""],
                ]
                titletable = Table(titledataList, style=titletbstyle, colWidths=[90,90])
                story.append(titletable)

                story.append(Paragraph("&nbsp;"))

                columndataList = [
                    ["貨品名稱", "規格", "Size", "單價", "數量", "小計", "備註", ""],
                ]
                columntable = Table(columndataList, style=columntbstyle, colWidths=[60,60])
                story.append(columntable)

                normadataList = []
                o = ""
                total = 0
                price = 0
                for i in range(len(result)):
                    total += result[i][7]
                    if o == "":   
                        o = result[i][0]
                        price += result[i][7]
                        normadataList.append(["銷貨日期：", f"{str(result[i][2].rstrip())}", "銷貨單：", f"{str(result[i][0].rstrip())}", "", "", "", ""])
                        normadataList.append([f"{str(result[i][1].rstrip())}", f"{str(result[i][3].rstrip())}", \
                                                f"{str(result[i][4].rstrip())}", f"{result[i][5]:,}", \
                                                f"{result[i][6]:,}", f"{result[i][7]:,}", f"{str(result[i][8]).rstrip()}", ""])

                    elif o == result[i][0]:
                        price += result[i][7]
                        normadataList.append([f"{str(result[i][1].rstrip())}", f"{str(result[i][3].rstrip())}", \
                                                f"{str(result[i][4].rstrip())}", f"{result[i][5]:,}", \
                                                f"{result[i][6]:,}", f"{result[i][7]:,}", f"{str(result[i][8]).rstrip()}", ""])
                    else:
                        normadataList.append(["金額：", f"{price:,}", "", "", "", "", "", ""])
                        normadataList.append(["", "", "", "", "", "", "", ""])
                        normadataList.append(["", "", "", "", "", "", "", ""])
                        o = result[i][0]
                        price = result[i][7]
                        normadataList.append(["銷貨日期：", f"{str(result[i][2].rstrip())}", "銷貨單：", f"{str(result[i][0].rstrip())}", "", "", "", ""])
                        normadataList.append([f"{str(result[i][1].rstrip())}", f"{str(result[i][3].rstrip())}", \
                                                f"{str(result[i][4].rstrip())}", f"{result[i][5]:,}", \
                                                f"{result[i][6]:,}", f"{result[i][7]:,}", f"{str(result[i][8]).rstrip()}", ""])

                normadataList.append(["金額：", f"{price:,}", "", "", "", "", "", ""])
                normadataList.append(["", "", "", "", "", "", "", ""])
                normadataList.append(["", "", "", "", "總金額：", f"{total:,}", "", ""])

                columntable = Table(normadataList, style=normaltbstyle, colWidths=[60,60])
                story.append(columntable)
                #------------------------------------------------------------------------------------------------------------------
                pdfTemplate.build(story)

                os.chdir("../")

                self.right.place_forget()
                self.right = Right_part(self,width=self.w-300, height=self.h)
                self.right.place(x=280,y=20)    
        except:
            tk.messagebox.showinfo(title='', message="請輸入客戶代號!!")

class Printdata_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.left = Left_part(self,width=kwargs["width"]-40,height=kwargs["height"]-90,fg_color="#FFFFFF")
        self.left.grid(row=0,column=0,padx=15,pady=10)