import customtkinter as ctk
import os
import tkcalendar as tkc
import psycopg2

from typing import Optional, Tuple, Union
from PIL import ImageTk,Image

class right_top_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.customer_name = ctk.CTkLabel(self,text="客戶名稱：",fg_color="blue",font=("Arial",20))
        self.address = ctk.CTkLabel(self,text="地址：",font=("Arial",20),fg_color="pink")
        self.phone = ctk.CTkLabel(self,text="　　手機：",font=("Arial",20),fg_color="green")
        self.remark = ctk.CTkLabel(self,text="備註：",font=("Arial",20),fg_color="brown")
        self.name_entry = ctk.CTkLabel(self)
        self.phone_entry = ctk.CTkLabel(self)
        self.address_entry = ctk.CTkTextbox(self,height=90)
        self.remark_entry = ctk.CTkTextbox(self,height=90)

        self.customer_name.place(x=60,y=50)
        self.name_entry.place(x=170,y=50)
        self.phone.place(x=60,y=110)
        self.phone_entry.place(x=170,y=110)
        self.address.place(x=380,y=50)
        self.address_entry.place(x=450,y=50)
        self.remark.place(x=680,y=50)
        self.remark_entry.place(x=750,y=50)

class item(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.chk_box = ctk.CTkCheckBox(self,width=80,height=40,text="")
        self.chk_box.grid(row=0,column=0,sticky="news")
        self.dat = ctk.CTkLabel(self,width=176,height=40,text=f"銷貨日期")
        self.dat.grid(row=0,column=1,sticky="news")
        self.sbtotal = ctk.CTkLabel(self,width=176,height=40,text=f"銷貨總計")
        self.sbtotal.grid(row=0,column=2,sticky="news")
        self.al_total = ctk.CTkEntry(self,width=176,height=40)
        self.al_total.grid(row=0,column=3,sticky="news")
        self.overage = ctk.CTkLabel(self,width=176,height=40,text="")
        self.overage.grid(row=0,column=4,sticky="news")
        self.remark = ctk.CTkLabel(self,width=176,height=40,text=f"備註")
        self.remark.grid(row=0,column=5,sticky="news")
class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def search():
            con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')
            cur = con.cursor()
            cur.execute(f"select name, phone, address, remark from customer where c_id='{customer_id_entry.get()}'")
            result = cur.fetchone()
            cur.execute(f"select * from order_it where c_id='{customer_id_entry.get()}' and date='{sell_date_entry.get_date()}'")
            result2 = cur.fetchall()
            right_top.name_entry.configure(text=f"{str(result[0]).rstrip()}")
            right_top.phone_entry.configure(text=f"{str(result[1]).rstrip()}")
            right_top.address_entry.insert(1.0,f"{str(result[2]).rstrip()}")
            right_top.remark_entry.insert(1.0,f"{str(result[3]).rstrip()}")
            cur.close()
            con.close()
            row = 0
            s_total = 0
            for i in result2:
                s_total += int(result2[row][6])
                it = item(right_bot.mid,fg_color="#EEEEEE")
                it.dat.configure(text=f"{result2[row][9]}")
                it.sbtotal.configure(text=f"{result2[row][6]}")
                it.remark.configure(text=f"{result2[row][7]}")
                it.pack()
                row += 1
            right_bot.label.configure(text="總計："+str(s_total))
        def reset():
            customer_id_entry.delete(0,'end')
            sell_date_entry.delete(0,'end')
            right_top.name_entry.configure(text="")
            right_top.phone_entry.configure(text="")
            right_top.address_entry.delete(1.0,'end')
            right_top.remark_entry.delete(1.0,'end')
            right_bot.label.configure(text="總計：")
        customer_id_entry = ctk.CTkEntry(self,width=200, height=40,fg_color="yellow",font=("Arial", 20),placeholder_text="客戶代號")
        sell_date_entry = tkc.DateEntry(self,selectmode='day')
        confirm_btn = ctk.CTkButton(self,width=200,height=40,fg_color="blue",text="確認查詢",font=("Arial",20),command=search)
        reset_btn = ctk.CTkButton(self,width=200,height=40,fg_color="green",text="重設查詢",font=("Arial",20),command=reset)
        right_top = right_top_part(self,width=1200,height=200,fg_color="#EEEEEE")
        right_bot = right_bot_part(self,width=1200,height=500,fg_color="#EEEEEE")
        
        reset_btn.place(x=25,y=660)
        confirm_btn.place(x=25,y=610)
        customer_id_entry.place(x=25,y=50)
        sell_date_entry.place(x=25,y=110)
        right_top.place(x=270,y=0)
        right_bot.place(x=270,y=220)

class top_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        bar_1 = ctk.CTkLabel(self, width=176, height=40,text="選擇")
        bar_2 = ctk.CTkLabel(self, width=176, height=40,text="銷貨日期")
        bar_3 = ctk.CTkLabel(self, width=176, height=40,text="銷貨總計")
        bar_4 = ctk.CTkLabel(self, width=176, height=40,text="已收金額")
        bar_5 = ctk.CTkLabel(self, width=176, height=40,text="餘額")
        bar_6 = ctk.CTkLabel(self, width=176, height=40,text="備註")

        bar_1.place(x=0,y=0)
        bar_2.place(x=176,y=0)
        bar_3.place(x=352,y=0)
        bar_4.place(x=528,y=0)
        bar_5.place(x=704,y=0)
        bar_6.place(x=880,y=0)
class right_bot_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        top = top_bar(self,width=1200,height=40)
        self.mid = ctk.CTkScrollableFrame(self,width=1150,height=420,fg_color="#EEEEEE")
        bot = ctk.CTkFrame(self,width=1200,height=40)
        self.label = ctk.CTkLabel(bot,width=50,height=40,text="總計：",font=("Arial",20))
        self.btn = ctk.CTkButton(bot,text="入賬")
        top.place(x=0,y=0)
        self.mid.place(x=0,y=40)
        bot.place(x=0,y=440)
        self.label.place(x=0,y=0)
        self.btn.place(x=1030,y=5)
class Accounting_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.left = left_part(self, width=1450,height=700,fg_color="white")
        # self.right_top = right_top_part(self,width=1200,height=200,fg_color="#EEEEEE")
        # self.right_bot = right_bot_part(self,width=1200,height=500,fg_color="#EEEEEE")

        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        # self.right_top.grid(row=0,column=1,padx=10,pady=10)
        # self.right_bot.grid(row=1,column=1,padx=10,pady=10)