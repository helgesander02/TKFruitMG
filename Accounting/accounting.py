import customtkinter as ctk
import os
import tkcalendar as tkc
from typing import Optional, Tuple, Union
from PIL import ImageTk,Image

import psycopg2
from .into_account import Into_Account_Main_Frame


class right_top_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.customer_name = ctk.CTkLabel(self,text="客戶名稱：", font=("microsoft yahei", 20, 'bold'))
        self.address = ctk.CTkLabel(self,text="地址：", font=("microsoft yahei", 20, 'bold'))
        self.phone = ctk.CTkLabel(self,text="　　手機：", font=("microsoft yahei", 20, 'bold'))
        self.remark = ctk.CTkLabel(self,text="備註：", font=("microsoft yahei", 20, 'bold'))

        self.name_entry = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20))
        self.phone_entry = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20))
        self.address_entry = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20))
        self.remark_entry = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20))

        self.customer_name.place(x=60,y=50)
        self.name_entry.place(x=170,y=50)

        self.phone.place(x=60,y=110)
        self.phone_entry.place(x=170,y=110)

        self.address.place(x=450,y=50)
        self.address_entry.place(x=530,y=50)

        self.remark.place(x=450,y=110)
        self.remark_entry.place(x=530,y=1100)

class right_bot_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.top = top_bar(self, width=kwargs["width"], height=40)
        
        self.mid = ctk.CTkScrollableFrame(self, width=kwargs["width"]-20, height=kwargs["height"]-80, fg_color="#EEEEEE")

        self.bot = ctk.CTkFrame(self, width=kwargs["width"], height=40)
        self.label = ctk.CTkLabel(self.bot, width=50, height=40, text="總計：" ,font=("microsoft yahei", 20, 'bold'))
        self.j_btn = ctk.CTkButton(self.bot, text="入賬" ,font=("microsoft yahei", 12, 'bold'))

        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=40)
        self.bot.place(x=0,y=kwargs["height"]-40)

        self.label.place(x=10,y=0)
        self.j_btn.place(x=1030,y=5)

class top_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/6
        self.bar_1 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="選擇",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="銷貨日期",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="銷貨總計",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="已收金額",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="餘額",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_6 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="備註",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)
        self.bar_6.grid(row=0,column=5)

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
        self.customer_id_entry = ctk.CTkEntry(self,width=210, height=50,
                                                    fg_color="#EEEEEE",
                                                    placeholder_text="客戶編號" 
                                                    #font=("microsoft yahei", 20, 'bold'),
                                                    )

        self.sell_date_entry = tkc.DateEntry(self, selectmode='day',
                                                    font=("microsoft yahei", 30),)

        self.confirm_btn = ctk.CTkButton(self,width=200,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="確認查詢",
                                                    font=("microsoft yahei", 20, 'bold'),
                                                    command=self.search)

        self.reset_btn = ctk.CTkButton(self,width=200,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="重設查詢",
                                                    font=("microsoft yahei", 20, 'bold'),
                                                    command=self.reset)

        self.right_top = right_top_part(self,width=kwargs["width"]-300,height=200,fg_color="#EEEEEE")
        self.right_bot = right_bot_part(self,width=kwargs["width"]-300,height=kwargs["height"]-320,fg_color="#EEEEEE")
        
        self.customer_id_entry.place(x=25,y=50)
        self.sell_date_entry.place(x=40,y=200)
        self.confirm_btn.place(x=25,y=kwargs["height"]-220)
        self.reset_btn.place(x=25,y=kwargs["height"]-160)
             
        self.right_top.place(x=270,y=5)
        self.right_bot.place(x=270,y=220)
    
    def search(self):
            con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            cur = con.cursor()
            cur.execute(f"select name, phone, address, remark from customer where c_id='{self.customer_id_entry.get()}'")
            result = cur.fetchone()
            cur.execute(f"select * from order_it where c_id='{self.customer_id_entry.get()}' and date='{self.sell_date_entry.get_date()}'")
            result2 = cur.fetchall()
            self.right_top.name_entry.configure(text=f"{str(result[0]).rstrip()}")
            self.right_top.phone_entry.configure(text=f"{str(result[1]).rstrip()}")
            self.right_top.address_entry.configure(text=f"{str(result[2]).rstrip()}")
            self.right_top.remark_entry.configure(text=f"{str(result[3]).rstrip()}")
            cur.close()
            con.close()
            row = 0
            s_total = 0
            for i in result2:
                s_total += int(result2[row][6])
                it = item(self.right_bot.mid,fg_color="#EEEEEE")
                it.dat.configure(text=f"{result2[row][9]}")
                it.sbtotal.configure(text=f"{result2[row][6]}")
                it.remark.configure(text=f"{result2[row][7]}")
                it.pack()
                row += 1
            self.right_bot.label.configure(text="總計："+str(s_total))

    def reset(self):
            self.customer_id_entry.delete(0,'end')
            self.sell_date_entry.delete(0,'end')
            self.right_top.name_entry.configure(text="")
            self.right_top.phone_entry.configure(text="")
            self.right_top.address_entry.delete(1.0,'end')
            self.right_top.remark_entry.delete(1.0,'end')
            self.right_bot.label.configure(text="總計：")

class Accounting_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def open_into_account(event):
            self.left.grid_forget()
            self.left = Into_Account_Main_Frame(self, width=kwargs["width"], height=kwargs["height"], fg_color="#FFFFFF")
            self.left.grid(row=0,column=0,padx=10,pady=10)

        self.left = left_part(self, width=kwargs["width"], height=kwargs["height"], fg_color="#FFFFFF")
        # self.right_top = right_top_part(self,width=1200,height=200,fg_color="#EEEEEE")
        # self.right_bot = right_bot_part(self,width=1200,height=500,fg_color="#EEEEEE")
        # self.jump_button = ctk.CTkButton(self.left,command=open_into_account,text="入賬頁面")
        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        # self.jump_button.place(x=25,y=150)
        self.left.right_bot.j_btn.bind("<Button-1>",open_into_account)
        # self.right_top.grid(row=0,column=1,padx=10,pady=10)
        # self.right_bot.grid(row=1,column=1,padx=10,pady=10)