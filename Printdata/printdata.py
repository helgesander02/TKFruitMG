import customtkinter as ctk
import tkcalendar as tkc
import os, sys
import win32print
import psycopg2
import pandas as pd
from collections import defaultdict
class Right_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def printer():
            printer_name = win32print.GetDefaultPrinter ()
            if sys.version_info >= (3,):
                raw_data = bytes ("This is a test", "utf-8")
            else:
                raw_data = "This is a test"
            hPrinter = win32print.OpenPrinter (printer_name)
            try:
                # This line is for test ↓
                hJob = win32print.StartDocPrinter (hPrinter, 1, ("test of raw data", None, "RAW"))
                # This line is for True print ↓
                try:
                    win32print.StartPagePrinter (hPrinter)
                    win32print.WritePrinter (hPrinter, raw_data)
                    win32print.EndPagePrinter (hPrinter)
                finally:
                    win32print.EndDocPrinter (hPrinter)
            finally:
                win32print.ClosePrinter (hPrinter)
        
        self.top_bar = ctk.CTkFrame(self,width=1180,height=40,fg_color="blue")
        self.main_body = ctk.CTkScrollableFrame(self,width=1160,height=620,fg_color="green")
        self.download_btn = ctk.CTkButton(self.top_bar,width=200,height=40,text="確認下載",command=search)
        self.top_bar.grid(row=0,column=0)
        self.main_body.grid(row=1,column=0)
        self.download_btn.place(x=490,y=0)
class Left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def search():
            better_dict = defaultdict(list)
            con = psycopg2.connect(database='postgres', user='postgres',
                                password='admin')
            con.autocommit = True

            cur = con.cursor()
            cur.execute(f"select * from order_it where c_id='{self.search_id.get()}' and date='{self.cal.get_date()}'")
            field_name = [des[0] for des in cur.description]
            result = cur.fetchall()
            test = []
            for i in result:
                temp = []
                for j in i:
                    temp.append(str(j).rstrip())
                test.append(temp)
            # print(test)
            for count in range(len(test)):
                for i in range(len(test[count])):
                    better_dict[field_name[i]].append(test[count][i])

            print(pd.DataFrame(better_dict).to_csv("download.csv",encoding="utf_8_sig"))
        self.search_id = ctk.CTkEntry(self,width=140,height=40,placeholder_text="客戶代號")
        self.cal = tkc.DateEntry(self)
        self.confirm = ctk.CTkButton(self,width=140,height=40,text="確認查詢",font=("Arial",20),command=search)
        self.reset = ctk.CTkButton(self,width=140,height=40,text="重設查詢",font=("Arial",20))
        self.right = Right_part(self,width=1160,height=40)
        # 以下是版面配置
        self.right.place(x=200,y=20)
        self.search_id.place(x=20,y=20)
        self.cal.place(x=20,y=75)
        self.confirm.place(x=20,y=600)
        self.reset.place(x=20,y=650)
class Printdata_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.left = Left_part(self,width=1400,height=750,fg_color="yellow")
        self.left.grid(row=0,column=0,padx=10,pady=10)