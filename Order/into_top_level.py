import customtkinter as ctk
import psycopg2

class Top_level_view_information(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x300")
        self.top = Top_level_top_bar(self, width=700, height=40)
        self.mid = ctk.CTkScrollableFrame(self, width=700-20, height=300-40, fg_color="#EEEEEE")
        
        
        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=30)

        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        with con:
            cur = con.cursor()
            cur.execute(f"SELECT item_id, item_name, date, specification, size, price, quantity, sub_total, remark \
                            FROM goods WHERE o_id = '{self.master.o_id.get()}'")
            result = cur.fetchall()

        for r in result:
            it = Top_level_item(self.mid, width=680, fg_color="#EEEEEE")
            it.pack()
            it.item_id_entry.insert(0, str(r[0]).rstrip())
            it.item_name_entry.insert(0, str(r[1]).rstrip())
            it.date_entry.insert(0, str(r[2]).rstrip())
            it.norm_entry.insert(0, str(r[3]).rstrip())
            it.size_entry.insert(0, str(r[4]).rstrip())
            it.price_entry.insert(0, str(r[5]).rstrip())
            it.quantity_entry.insert(0, str(r[6]).rstrip())
            it.total_entry.insert(0, str(r[7]).rstrip())
            it.remark_entry.insert(0, str(r[8]).rstrip())
        
class Top_level_edit_information(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x340")
        self.master = args[0]
        self.top = Top_level_top_bar(self, width=700, height=40)
        self.mid = ctk.CTkScrollableFrame(self, width=680, height=260, fg_color="#EEEEEE")
        self.bot = ctk.CTkFrame(self, width=700, height=40)
        self.updata = ctk.CTkButton(self.bot, width=120, height=30, text="更新", font=("microsoft yahei", 16, 'bold'))
        self.reload = ctk.CTkButton(self.bot, width=120, height=30, text="重設", font=("microsoft yahei", 16, 'bold'))
        self.allit = []

        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=30)
        self.bot.place(x=0,y=300)
        self.updata.place(x=550,y=5)
        self.reload.place(x=400,y=5)
        self.updata.bind("<Button-1>", self.UpData)
        self.reload.bind("<Button-1>", self.ReLoad)

        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        with con:
            cur = con.cursor()
            cur.execute(f"SELECT item_id, item_name, date, specification, size, price, quantity, sub_total, remark \
                            FROM goods WHERE o_id = '{self.master.o_id.get()}'")
            result = cur.fetchall()

        for r in result:
            it = Top_level_item(self.mid, width=680, fg_color="#EEEEEE")
            it.pack()
            it.item_id_entry.insert(0, str(r[0]).rstrip())
            it.item_name_entry.insert(0, str(r[1]).rstrip())
            it.date_entry.insert(0, str(r[2]).rstrip())
            it.norm_entry.insert(0, str(r[3]).rstrip())
            it.size_entry.insert(0, str(r[4]).rstrip())
            it.price_entry.insert(0, str(r[5]).rstrip())
            it.quantity_entry.insert(0, str(r[6]).rstrip())
            it.total_entry.insert(0, str(r[7]).rstrip())
            it.remark_entry.insert(0, str(r[8]).rstrip())
            self.allit.append(it)

    def UpData(self, event):
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        with con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM goods WHERE o_id='{self.master.o_id.get()}'")
            con.commit()

            for it in self.allit:
                cur.execute(f"INSERT INTO goods(o_id, item_id, item_name, date, specification, size, price, quantity, sub_total, remark) \
                                VALUES('{self.master.o_id.get()}','{it.item_id_entry.get()}','{it.item_name_entry.get()}', \
                                        '{it.date_entry.get()}','{it.norm_entry.get()}', '{it.size_entry.get()}', \
                                        '{it.price_entry.get()}','{it.quantity_entry.get()}','{it.total_entry.get()}', \
                                        '{it.remark_entry.get()}')")
                con.commit()

        self.master.reload_right_bot_mid
        self.destroy()

    def ReLoad(self, event):
        self.mid.place_forget()
        self.allit = []
        self.mid = ctk.CTkScrollableFrame(self, width=680, height=260, fg_color="#EEEEEE")
        self.mid.place(x=0,y=30)

        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        with con:
            cur = con.cursor()
            cur.execute(f"SELECT item_id, item_name, date, specification, size, price, quantity, sub_total, remark \
                            FROM goods WHERE o_id = '{self.master.o_id.get()}'")
            result = cur.fetchall()

        for r in result:
            it = Top_level_item(self.mid, width=680, fg_color="#EEEEEE")
            it.pack()
            it.item_id_entry.insert(0, str(r[0]).rstrip())
            it.item_name_entry.insert(0, str(r[1]).rstrip())
            it.date_entry.insert(0, str(r[2]).rstrip())
            it.norm_entry.insert(0, str(r[3]).rstrip())
            it.size_entry.insert(0, str(r[4]).rstrip())
            it.price_entry.insert(0, str(r[5]).rstrip())
            it.quantity_entry.insert(0, str(r[6]).rstrip())
            it.total_entry.insert(0, str(r[7]).rstrip())
            it.remark_entry.insert(0, str(r[8]).rstrip())
            self.allit.append(it)

class Top_level_top_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/9
        self.item_id = ctk.CTkLabel(self, text="品項名稱", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.item_name = ctk.CTkLabel(self, text="品項名稱", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.date = ctk.CTkLabel(self, text="日期", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.norm = ctk.CTkLabel(self, text="規格", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.size = ctk.CTkLabel(self, text="大小", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.price = ctk.CTkLabel(self, text="價格", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.quantity = ctk.CTkLabel(self, text="數量", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.total = ctk.CTkLabel(self, text="小計", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.remark = ctk.CTkLabel(self, text="備註", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)

        self.item_id.grid(row=0,column=0)
        self.item_name.grid(row=0,column=1)
        self.date.grid(row=0,column=2)
        self.norm.grid(row=0,column=3)
        self.size.grid(row=0,column=4)
        self.price.grid(row=0,column=5)
        self.quantity.grid(row=0,column=6)
        self.total.grid(row=0,column=7)
        self.remark.grid(row=0,column=8)

class Top_level_item(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/9
        self.item_id_entry = ctk.CTkEntry(self,width=w,height=20)
        self.item_name_entry = ctk.CTkEntry(self,width=w,height=20)
        self.date_entry = ctk.CTkEntry(self,width=w,height=20)
        self.norm_entry = ctk.CTkEntry(self,width=w,height=20)
        self.size_entry = ctk.CTkEntry(self,width=w,height=20)
        self.price_entry = ctk.CTkEntry(self,width=w,height=20)
        self.quantity_entry = ctk.CTkEntry(self,width=w,height=20)
        self.total_entry = ctk.CTkEntry(self,width=w,height=20)
        self.remark_entry = ctk.CTkEntry(self,width=w,height=20)  

        self.item_id_entry.grid(row=0,column=0)
        self.item_name_entry.grid(row=0,column=1)
        self.date_entry.grid(row=0,column=2)
        self.norm_entry.grid(row=0,column=3)
        self.size_entry.grid(row=0,column=4)
        self.price_entry.grid(row=0,column=5)
        self.quantity_entry.grid(row=0,column=6)
        self.total_entry.grid(row=0,column=7)
        self.remark_entry.grid(row=0,column=8)