import customtkinter as ctk
import os

from typing import Optional, Tuple, Union
from PIL import ImageTk,Image

class right_top_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        customer_name = ctk.CTkLabel(self,text="客戶名稱：",fg_color="blue",font=("Arial",20))
        address = ctk.CTkLabel(self,text="地址：",font=("Arial",20),fg_color="pink")
        phone = ctk.CTkLabel(self,text="　　手機：",font=("Arial",20),fg_color="green")
        remark = ctk.CTkLabel(self,text="備註：",font=("Arial",20),fg_color="brown")

        customer_name.place(x=60,y=50)
        phone.place(x=60,y=110)
        address.place(x=380,y=50)
        remark.place(x=680,y=50)
        
class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
            customer_id_entry = ctk.CTkEntry(self,width=200, height=40,fg_color="yellow",font=("Arial", 20),placeholder_text="客戶代號")
            sell_date_entry = ctk.CTkEntry(self,width=160, height=40,fg_color="blue",font=("Arial", 20),placeholder_text="銷貨日期：",placeholder_text_color="black")
            confirm_btn = ctk.CTkButton(self,width=200,height=40,fg_color="blue",text="確認查詢",font=("Arial",20))
            reset_btn = ctk.CTkButton(self,width=200,height=40,fg_color="green",text="重設查詢",font=("Arial",20))
            reset_btn.place(x=25,y=660)
            confirm_btn.place(x=25,y=610)
            customer_id_entry.place(x=25,y=50)
            sell_date_entry.place(x=25,y=110)

class right_bot_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        bar_1 = ctk.CTkLabel(self, width=176, height=40,text="選擇")
        bar_2 = ctk.CTkLabel(self, width=176, height=40,text="銷貨日期")
        bar_3 = ctk.CTkLabel(self, width=176, height=40,text="銷貨總計")
        bar_4 = ctk.CTkLabel(self, width=176, height=40,text="已收金額")
        bar_5 = ctk.CTkLabel(self, width=176, height=40,text="餘額")
        bar_6 = ctk.CTkLabel(self, width=800, height=40,text="備註")

        bar_1.place(x=0,y=0)
        bar_2.place(x=176,y=0)
        bar_3.place(x=352,y=0)
        bar_4.place(x=528,y=0)
        bar_5.place(x=704,y=0)
        bar_6.place(x=880,y=0)
class Accounting_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.left = left_part(self, width=250,height=750,fg_color="#EEEEEE")
        self.right_top = right_top_part(self,width=1200,height=200,fg_color="#EEEEEE")
        self.right_bot = right_bot_part(self,width=1200,height=500,fg_color="#EEEEEE")

        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        self.right_top.grid(row=0,column=1,padx=10,pady=10)
        self.right_bot.grid(row=1,column=1,padx=10,pady=10)