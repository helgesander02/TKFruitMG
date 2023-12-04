import customtkinter as ctk
import tkinter as tk
import psycopg2
import os
from PIL import ImageTk,Image

class Top_level_view_information(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x400")
        self.top = Top_level_top_bar(self, width=1000, height=40)
        self.mid = ctk.CTkScrollableFrame(self, width=980, height=400-40, fg_color="#EEEEEE")
        self.o_id = self.master.o_id.get()
        self.mid.o_id = self.o_id
             
        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=40)

        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        with con:
            cur = con.cursor()
            cur.execute(f"SELECT item_id, item_name, date, specification, size, price, quantity, sub_total, remark \
                            FROM goods WHERE o_id = '{self.o_id}'")
            result = cur.fetchall()

        for r in result:
            it = Top_level_item(self.mid, width=980, fg_color="#EEEEEE")
            it.pack()
            it.item_id_entry.insert(0, str(r[0]).rstrip())
            it.item_name_entry.insert(0, str(r[1]).rstrip())
            it.date_entry.insert(0, str(r[2]).rstrip())
            it.norm_entry.insert(0, str(r[3]).rstrip())
            it.size_entry.insert(0, str(r[4]).rstrip())
            it.quantity_entry.insert(0, str(r[6]).rstrip())
            it.price_entry.insert(0, str(r[5]).rstrip())        
            it.total_entry.insert(0, str(r[7]).rstrip())
            it.remark_entry.insert(0, str(r[8]).rstrip())
        
class Top_level_edit_information(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x400")
        self.master = args[0]
        self.allit = []
        self.o_id = self.master.o_id.get()
        self.top = Top_level_top_bar(self, width=1000, height=40)
        self.mid = Top_level_mid(self, width=980, height=320, fg_color="#EEEEEE")
        self.bot = ctk.CTkFrame(self, width=1000, height=40, fg_color="#DDDDDD")
        self.updata = ctk.CTkButton(self.bot, width=100, height=20, text="更新", font=("microsoft yahei", 12, 'bold'))
        self.load = ctk.CTkButton(self.bot, width=100, height=20, text="重設", font=("microsoft yahei", 12, 'bold'))
        self.new = ctk.CTkButton(self.bot, width=100, height=20, text="新增", font=("microsoft yahei", 12, 'bold'))
        
        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=40)
        self.bot.place(x=0,y=370)
        self.updata.place(x=850,y=5)
        self.load.place(x=700,y=5)
        self.new.place(x=550,y=5)
        self.updata.bind("<Button-1>", self.UpData)
        self.load.bind("<Button-1>", self.ReLoad)
        self.new.bind("<Button-1>", self.New)

    def UpData(self, event):
        for i in range(len(self.allit)):
            if self.allit[i].item_id_entry.get() == "":
                self.allit.pop(i)

        try:
            if len(self.allit) == 0:
                tk.messagebox.showinfo(title='更新銷貨單', message="未輸入資料!!")
            else:
                con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
                #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
                with con:
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM goods WHERE o_id='{self.o_id}'")
                    con.commit()

                    for it in self.allit:
                        cur.execute(f"INSERT INTO goods(o_id, item_id, item_name, date, specification, size, price, quantity, sub_total, remark) \
                                        VALUES('{self.o_id}','{it.item_id_entry.get()}','{it.item_name_entry.get()}', \
                                                '{it.date_entry.get()}','{it.norm_entry.get()}', '{it.size_entry.get()}', \
                                                '{it.price_entry.get()}','{it.quantity_entry.get()}','{it.total_entry.get()}', \
                                                '{it.remark_entry.get()}')")
                        con.commit()

                self.master.reload_right_bot_mid()
                self.destroy()
                tk.messagebox.showinfo(title='更新銷貨單', message="更改完成")
        except:
            tk.messagebox.showinfo(title='更新銷貨單', message="未輸入資料!!")

    def reload(self):
        self.mid.destroy()
        self.allit = []
        self.mid = Top_level_mid(self, width=980, height=320, fg_color="#EEEEEE")
        self.mid.place(x=0,y=40)

    def ReLoad(self, event):
        self.mid.destroy()
        self.allit = []
        self.mid = Top_level_mid(self, width=980, height=320, fg_color="#EEEEEE")
        self.mid.place(x=0,y=40)

    def New(self, event):
        it = Top_level_item(self.mid, width=980, fg_color="#EEEEEE")
        it.pack()
        self.allit.append(it)

class Top_level_mid(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.o_id = self.master.o_id

        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        with con:
            cur = con.cursor()
            cur.execute(f"SELECT item_id, item_name, date, specification, size, price, quantity, sub_total, remark \
                            FROM goods WHERE o_id = '{self.o_id}'")
            result = cur.fetchall()

        for r in result:
            it = Top_level_item(self, width=980, fg_color="#EEEEEE")
            it.pack()
            it.item_id_entry.insert(0, str(r[0]).rstrip())
            it.item_name_entry.insert(0, str(r[1]).rstrip())
            it.date_entry.insert(0, str(r[2]).rstrip())
            it.norm_entry.insert(0, str(r[3]).rstrip())
            it.size_entry.insert(0, str(r[4]).rstrip())
            it.quantity_entry.insert(0, str(r[6]).rstrip())
            it.price_entry.insert(0, str(r[5]).rstrip())
            it.total_entry.insert(0, str(r[7]).rstrip())
            it.remark_entry.insert(0, str(r[8]).rstrip())
            self.master.allit.append(it)
        
        
    def reload(self):
        self.master.reload()

class Top_level_top_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/10
        self.item_id = ctk.CTkLabel(self, text="品項編號", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.item_name = ctk.CTkLabel(self, text="品項名稱", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.date = ctk.CTkLabel(self, text="日期", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.norm = ctk.CTkLabel(self, text="規格", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.size = ctk.CTkLabel(self, text="大小", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.quantity = ctk.CTkLabel(self, text="數量", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.price = ctk.CTkLabel(self, text="價格", font=("microsoft yahei", 12, 'bold'), width=w, height=30,) 
        self.total = ctk.CTkLabel(self, text="小計", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.remark = ctk.CTkLabel(self, text="備註", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.delete = ctk.CTkLabel(self, text="刪除", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)

        self.item_id.grid(row=0,column=0)
        self.item_name.grid(row=0,column=1)
        self.date.grid(row=0,column=2)
        self.norm.grid(row=0,column=3)
        self.size.grid(row=0,column=4)
        self.quantity.grid(row=0,column=5)
        self.price.grid(row=0,column=6)
        self.total.grid(row=0,column=7)
        self.remark.grid(row=0,column=8)
        self.delete.grid(row=0,column=9)

class Top_level_item(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        def item_name(event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
            with con:
                cur = con.cursor()
                cur.execute(f"SELECT item_name from item where item_id = '{self.item_id_entry.get()}'")
                result = cur.fetchone()

            if self.item_name_entry.get() == "":
                self.item_name_entry.insert(0,str(result[0]).rstrip())
                self.date_entry.focus()
            else:
                self.item_name_entry.delete(0, len(self.item_name_entry.get()))
                self.item_name_entry.insert(0,str(result[0]).rstrip())
                self.date_entry.focus()

        def total_price(event):
            price = self.price_entry.get()
            quan = self.quantity_entry.get()
            
            if price=="" or quan=="":
                total = 0
                self.totalsum += total

            elif self.total_entry.get() == "":
                total = int(price) * int(quan)
                self.totalsum += total
                self.total_entry.insert(0,total)
                self.remark_entry.focus()

            else:
                total = int(price) * int(quan)
                self.totalsum += (total-int(self.total_entry.get()))
                self.total_entry.delete(0, len(self.total_entry.get()))
                self.total_entry.insert(0,total)
                self.remark_entry.focus()

        super().__init__(master, **kwargs)
        w = kwargs["width"]/10
        self.totalsum = 0
        self.master = master
        self.o_id = master.o_id
        self.toplevel_window = None
        self.item_id_entry = ctk.CTkEntry(self,width=w,height=20)
        self.item_name_entry = ctk.CTkEntry(self,width=w,height=20)
        self.date_entry = ctk.CTkEntry(self,width=w,height=20)
        self.norm_entry = ctk.CTkEntry(self,width=w,height=20)
        self.size_entry = ctk.CTkEntry(self,width=w,height=20)
        self.quantity_entry = ctk.CTkEntry(self,width=w,height=20)
        self.price_entry = ctk.CTkEntry(self,width=w,height=20)       
        self.total_entry = ctk.CTkEntry(self,width=w,height=20)
        self.remark_entry = ctk.CTkEntry(self,width=w,height=20)

        deleteimg = Image.open(f"{os.getcwd()}\\icon\\close.png")
        Redeleteimg = ctk.CTkImage(deleteimg,size=(20,20))
        self.delete = ctk.CTkButton(self, image=Redeleteimg, width=w, height=20, fg_color="#EEEEEE", hover_color="#EEEEEE", text="")    

        self.item_id_entry.grid(row=0,column=0)
        self.item_name_entry.grid(row=0,column=1)
        self.date_entry.grid(row=0,column=2)
        self.norm_entry.grid(row=0,column=3)
        self.size_entry.grid(row=0,column=4)
        self.quantity_entry.grid(row=0,column=5)
        self.price_entry.grid(row=0,column=6)  
        self.total_entry.grid(row=0,column=7)
        self.remark_entry.grid(row=0,column=8)
        self.delete.grid(row=0,column=9)
        self.delete.bind("<Button-1>", self.itemdelete)
        self.item_id_entry.bind('<Tab>',item_name)
        self.price_entry.bind('<Tab>',total_price)
        self.quantity_entry.bind('<Tab>',total_price)

    def reload(self):
            self.master.reload()

    def itemdelete(self, event):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_check_itemdelete(self)
            self.toplevel_window.attributes('-topmost','true') 
            self.toplevel_window.focus() 
        else:
            self.toplevel_window.focus()

class Top_level_check_delete(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x150")
        self.master = args[0]
        def click(event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
            with con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM order_form WHERE o_id='{self.master.o_id.get()}'")
                cur.execute(f"DELETE FROM goods WHERE o_id='{self.master.o_id.get()}'")

                cur.execute(f"SELECT ac_id FROM accounting WHERE o_id='{self.master.o_id.get()}'")
                ac_ids = cur.fetchall()

                cur.execute(f"DELETE FROM accounting WHERE o_id='{self.master.o_id.get()}'")
                for ac_id in ac_ids:
                    cur.execute(f"DELETE FROM receipt WHERE ac_id='{ac_id[0]}'")

            self.master.reload_right_bot_mid()
            self.destroy()

        def cancel(event):
            self.destroy()

        self.msg = ctk.CTkLabel(self, text="是否確定要刪除此訂貨單 !!", font=("microsoft yahei", 20, 'bold'))
        self.confirm = ctk.CTkButton(self,width=100,height=25,text="確認", font=("microsoft yahei", 14, 'bold'))
        self.confirm.bind('<Button-1>', click)
        self.cancel = ctk.CTkButton(self,width=100,height=25,text="取消", font=("microsoft yahei", 14, 'bold'))
        self.cancel.bind('<Button-1>', cancel)
        self.msg.place(x=35,y=40)
        self.confirm.place(x=45,y=110)
        self.cancel.place(x=155,y=110)

class Top_level_check_itemdelete(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x150")
        self.master = args[0]
        def click(event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
            if self.master.item_id_entry.get() != "":
                with con:
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM goods WHERE o_id='{self.master.o_id}' AND item_id='{self.master.item_id_entry.get()}'")
            self.master.reload()
            self.destroy()

        def cancel(event):
            self.destroy()

        self.msg = ctk.CTkLabel(self, text="是否確定要刪除此明細 !!", font=("microsoft yahei", 20, 'bold'))
        self.confirm = ctk.CTkButton(self,width=100,height=25,text="確認", font=("microsoft yahei", 14, 'bold'))
        self.confirm.bind('<Button-1>', click)
        self.cancel = ctk.CTkButton(self,width=100,height=25,text="取消", font=("microsoft yahei", 14, 'bold'))
        self.cancel.bind('<Button-1>', cancel)
        self.msg.place(x=50,y=40)
        self.confirm.place(x=45,y=110)
        self.cancel.place(x=155,y=110)