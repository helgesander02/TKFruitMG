import customtkinter as ctk
import psycopg2


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

class Top_level_top_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/9
        self.item_id = ctk.CTkLabel(self, text="品項編號", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.item_name = ctk.CTkLabel(self, text="品項名稱", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.date = ctk.CTkLabel(self, text="日期", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.norm = ctk.CTkLabel(self, text="規格", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.size = ctk.CTkLabel(self, text="大小", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.quantity = ctk.CTkLabel(self, text="數量", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.price = ctk.CTkLabel(self, text="價格", font=("microsoft yahei", 12, 'bold'), width=w, height=30,) 
        self.total = ctk.CTkLabel(self, text="小計", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)
        self.remark = ctk.CTkLabel(self, text="備註", font=("microsoft yahei", 12, 'bold'), width=w, height=30,)

        self.item_id.grid(row=0,column=0)
        self.item_name.grid(row=0,column=1)
        self.date.grid(row=0,column=2)
        self.norm.grid(row=0,column=3)
        self.size.grid(row=0,column=4)
        self.quantity.grid(row=0,column=5)
        self.price.grid(row=0,column=6)
        self.total.grid(row=0,column=7)
        self.remark.grid(row=0,column=8)

class Top_level_item(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        def item_name(event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
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
        w = kwargs["width"]/9
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

 

        self.item_id_entry.grid(row=0,column=0)
        self.item_name_entry.grid(row=0,column=1)
        self.date_entry.grid(row=0,column=2)
        self.norm_entry.grid(row=0,column=3)
        self.size_entry.grid(row=0,column=4)
        self.quantity_entry.grid(row=0,column=5)
        self.price_entry.grid(row=0,column=6)  
        self.total_entry.grid(row=0,column=7)
        self.remark_entry.grid(row=0,column=8)
        self.item_id_entry.bind('<Tab>',item_name)
        self.price_entry.bind('<Tab>',total_price)
        self.quantity_entry.bind('<Tab>',total_price)

    def reload(self):
            self.master.reload()
