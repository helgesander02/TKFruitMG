import customtkinter as ctk
import tkinter as tk
import tkcalendar as tkc
import psycopg2
import os
from PIL import Image

from .edit_order import Edit_Order_Main_Frame
from .into_order import Into_Order_Main_Frame
from .into_top_level import Top_level_view_information

class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.master = master
        
        self.customer_id_entry = ctk.CTkEntry(self,width=210, height=50,
                                              fg_color="#EEEEEE",
                                              text_color="#000000",
                                              font=("microsoft yahei", 20),
                                              placeholder_text="客戶編號")
        
        self.sell_date1_entry = tkc.DateEntry(self, selectmode='day',
                                              font=("microsoft yahei", 20),
                                              year=2000,month=1,day=1,
                                              date_pattern="yyyy-mm-dd")
        
        self.sell_date2_entry = tkc.DateEntry(self, selectmode='day',
                                              font=("microsoft yahei", 20),
                                              date_pattern="yyyy-mm-dd")


        self.confirm_btn = ctk.CTkButton(self,width=200,height=40,
                                         fg_color="#3B8ED0",
                                         text="確認查詢",
                                         font=("microsoft yahei", 20, 'bold'))

        self.new_btn = ctk.CTkButton(self,width=200,height=40,
                                     fg_color="#3B8ED0",
                                     text="新增銷貨單",
                                     font=("microsoft yahei", 20, 'bold'))

        self.right_bot = right_bot_part(self, width=self.w-300, height=self.h-100, fg_color="#EEEEEE")

        self.customer_id_entry.place(x=25, y=50)
        self.sell_date1_entry.place(x=25, y=300)
        self.sell_date2_entry.place(x=25, y=350)
        self.confirm_btn.place(x=25, y=self.h-220)
        self.new_btn.place(x=25, y=self.h-150)
        self.right_bot.place(x=270, y=5)

        self.confirm_btn.bind("<Button-1>", self.insert_data)
        self.customer_id_entry.bind("<Return>", self.insert_data)
        self.new_btn.bind("<Button-1>", self.master.open_into_order)

    def reset(self):
        self.right_bot.destroy()
        self.right_bot = right_bot_part(self, width=self.w-300, height=self.h-100, fg_color="#EEEEEE")
        self.right_bot.place(x=270, y=5)

    def insert_data(self, event):
        self.reset()
        self.right_bot.insert_data(self.customer_id_entry.get(), 
                                   self.sell_date1_entry.get_date(), 
                                   self.sell_date2_entry.get_date())
        
class right_bot_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)     
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.master = master

        self.top = bot_top_part(self, width=self.w, height=40)
        self.mid = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-85, fg_color="#EEEEEE")
        self.mid.m = self
        self.bot = bot_bot_part(self, width=self.w, height=40, fg_color="#DDDDDD")

        self.top.place(x=0, y=0)
        self.mid.place(x=0, y=40)
        self.bot.place(x=0, y=self.h-40)

    def reload(self):
        self.mid.destroy()
        self.mid = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-85, fg_color="#EEEEEE")
        self.mid.m = self
        self.mid.place(x=0, y=40)

        self.bot.destroy()
        self.bot = bot_bot_part(self, width=self.w, height=40, fg_color="#DDDDDD")
        self.bot.place(x=0, y=self.h-40)

        self.insert_data(self.master.c_id, self.master.sell_date1_entry.get_date(), self.master.sell_date2_entry.get_date())

    def insert_data(self, c_id, date1, date2):
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        with con:
            cur = con.cursor()
            if c_id == "":
                cur.execute(f"SELECT customer.name, goods.o_id, SUM(goods.sub_total) \
                            FROM order_form JOIN goods \
                            ON order_form.o_id = goods.o_id JOIN customer \
							ON order_form.c_id = customer.c_id \
                            WHERE (goods.date BETWEEN SYMMETRIC '{date1}' AND '{date2}') \
                            GROUP BY customer.name, goods.o_id")
                
                result = cur.fetchall() 
            else:
                cur.execute(f"SELECT customer.name, goods.o_id, SUM(goods.sub_total) \
                            FROM order_form JOIN goods \
                            ON order_form.o_id = goods.o_id JOIN customer \
                            ON order_form.c_id = customer.c_id \
                            WHERE order_form.c_id = '{c_id}' AND (goods.date BETWEEN SYMMETRIC '{date1}' AND '{date2}') \
                            GROUP BY customer.name, goods.o_id")
                result = cur.fetchall()    

        s = 0
        for row in result:
            entry = entrybox(self.mid ,width=self.w, fg_color="#EEEEEE")
            entry.day.insert(0, f"{row[1][:4]}/{row[1][4:6]}/{row[1][6:8]}")
            entry.name.insert(0, row[0])
            entry.o_id.insert(0, row[1]) 
            entry.total.insert(0, row[2])
            s+=int(row[2])
            entry.pack()

        self.bot.nmb.configure(text=f"總額： {s:,}") 

class bot_top_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/7

        self.bar_0 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="日期",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))
        
        self.bar_1 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="客戶名稱",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="訂單編號",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="訂單小計",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="詳細資料",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="編輯",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_6 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="刪除",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_0.grid(row=0, column=0)
        self.bar_1.grid(row=0, column=1)
        self.bar_2.grid(row=0, column=2)
        self.bar_3.grid(row=0, column=3)
        self.bar_4.grid(row=0, column=4)
        self.bar_5.grid(row=0, column=5)
        self.bar_6.grid(row=0, column=6)

class entrybox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = (kwargs["width"])/7     
        self.master =  master
        self.toplevel_window = None
        self.day = ctk.CTkEntry(self, width=w, height=40, fg_color="#FFFFFF", text_color="#000000")
        self.name = ctk.CTkEntry(self, width=w, height=40, fg_color="#FFFFFF", text_color="#000000")
        self.o_id = ctk.CTkEntry(self, width=w, height=40, fg_color="#FFFFFF", text_color="#000000")
        self.total = ctk.CTkEntry(self, width=w, height=40, fg_color="#FFFFFF", text_color="#000000")

        infoimg = Image.open(f"{os.getcwd()}\\icon\\info.png")
        Reinfoimg = ctk.CTkImage(infoimg, size=(30,30))
        self.info = ctk.CTkButton(self, image=Reinfoimg, width=w, height=40, fg_color="#EEEEEE", hover_color="#EEEEEE", text="")

        editimg = Image.open(f"{os.getcwd()}\\icon\\edit.png")
        Reeditimg = ctk.CTkImage(editimg, size=(30,30))
        self.edit = ctk.CTkButton(self, image=Reeditimg, width=w, height=40, fg_color="#EEEEEE", hover_color="#EEEEEE", text="")

        deleteimg = Image.open(f"{os.getcwd()}\\icon\\close.png")
        Redeleteimg = ctk.CTkImage(deleteimg, size=(35,35))
        self.delete = ctk.CTkButton(self, image=Redeleteimg, width=w, height=40, fg_color="#EEEEEE", hover_color="#EEEEEE", text="")  

        self.day.grid(row=0, column=0)
        self.name.grid(row=0, column=1)
        self.o_id.grid(row=0, column=2)
        self.total.grid(row=0, column=3)
        self.info.grid(row=0, column=4)
        self.edit.grid(row=0, column=5)
        self.delete.grid(row=0, column=6)

        self.info.bind("<Button-1>", self.eninfo)
        self.edit.bind("<Button-1>", self.enedit)
        self.delete.bind("<Button-1>", self.endelete)

    def reload_right_bot_mid(self):
        self.master.m.reload()

    def enedit(self, event):
        self.master.m.master.master.open_edit_order(str(self.master.m.master.customer_id_entry.get()).rstrip(), 
                                                    str(self.name.get()).rstrip(), 
                                                    str(self.o_id.get()).rstrip())

    def eninfo(self, event):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_view_information(self)
            self.toplevel_window.title("")
            self.toplevel_window.attributes('-topmost','true')
        
        else:
            self.toplevel_window.focus()
    
    def endelete(self, event):
        if tk.messagebox.askokcancel(message="是否確定要刪除 !!", icon="warning"):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            with con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM order_form WHERE o_id='{self.o_id.get()}'")
                cur.execute(f"DELETE FROM goods WHERE o_id='{self.o_id.get()}'")

                cur.execute(f"SELECT ac_id FROM accounting WHERE o_id='{self.o_id.get()}'")
                ac_ids = cur.fetchall()

                cur.execute(f"DELETE FROM accounting WHERE o_id='{self.o_id.get()}'")
                for ac_id in ac_ids:
                    cur.execute(f"DELETE FROM receipt WHERE ac_id='{ac_id[0]}'")

            self.reload_right_bot_mid()
               
class bot_bot_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]  

        self.nmb = ctk.CTkLabel(self, text="總額：", font=("microsoft yahei", 20, 'bold'), text_color=("#000000"))
        self.nmb.place(x=20, y=5)

class Order_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"] 

        self.main = left_part(self, width=kwargs["width"], height=kwargs["height"], fg_color="#FFFFFF")
        self.main.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

    def open_into_order(self, event):
        self.main.place_forget()
        self.intomain = Into_Order_Main_Frame(self, width=self.w, height=self.h, fg_color="#FFFFFF")
        self.intomain.place(x=0, y=0)

    def open_edit_order(self, c_id, name, o_id):
        self.main.place_forget()
        self.editmain = Edit_Order_Main_Frame(self, c_id=c_id, c_name=name, o_id=o_id, width=self.w, height=self.h, fg_color="#FFFFFF")
        self.editmain.place(x=0, y=0)
        


        