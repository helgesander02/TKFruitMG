import customtkinter as ctk
import tkinter as tk
import tkcalendar as tkc
import psycopg2

class top_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def ch_date(*args):
            self.order_id.configure(text=f"訂貨單編號：{self.select_od_id(date_in=self.sel.get())}", font=("microsoft yahei", 24, 'bold'), text_color="#000000")
            try:
                self.bot.order_id = self.order_id.cget("text")[6:]
            except:
                pass
        
        # top
        self.c_id = ctk.CTkEntry(self,width=250,height=50,placeholder_text="輸入客戶代號",font=("microsoft yahei", 24), fg_color="#DDDDDD", text_color="#000000")
        self.c_id.focus()
        self.c_name = ctk.CTkLabel(self, text="",font=("microsoft yahei", 24, 'bold'), text_color="#000000")
        self.order_id = ctk.CTkLabel(self)
        self.sel = ctk.StringVar()
        self.sel.trace('w',ch_date)
        self.cal = tkc.DateEntry(self, font=("microsoft yahei", 20),textvariable=self.sel,date_pattern="yyyy-mm-dd")
        self.order_id.configure(text=f"訂貨單編號：{self.select_od_id(date_in=self.cal.get_date())}", font=("microsoft yahei", 24, 'bold'), text_color="#000000")

        self.c_id.place(x=40,y=40)
        self.c_name.place(x=300,y=40) 
        self.cal.place(x=450,y=40)
        self.order_id.place(x=kwargs["width"]-400,y=50)

        # bot
        self.bot = bot_part(self,width=kwargs["width"],height=kwargs["height"],c_id=self.c_id,cal=self.cal, order_id=self.order_id.cget("text")[6:], fg_color="#EEEEEE")
        self.bot.place(x=0,y=120)

        # event
        self.c_id.bind('<Tab>', self.search_name)
    
    def search_name(self, event):
        try:
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            with con:
                cur = con.cursor()
                cur.execute(f"SELECT name from customer where c_id = '{self.c_id.get()}'")
                result = cur.fetchone()

            if result[0] == "":
                self.c_name.configure(text="沒有這個顧客")
            else:
                self.c_name.configure(text=result[0])
        except:
            self.c_name.configure(text="沒有這個顧客")
         

    def select_od_id(self, date_in):
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        with con:
            cur = con.cursor()
            cur.execute(f"select o_id, date from goods where date='{date_in}' order by o_id")
            dt_time = cur.fetchall()
            order_id = f"{str(date_in)[:4]}{str(date_in)[5:7]}{str(date_in)[8:]}"

        if len(dt_time) == 0:
            return f"{order_id}0001"
        else:
            n_id = str(dt_time[-1][0]).rstrip()
            o_id = str(int(n_id[-4:]) + 1).zfill(4)
            return f"{order_id}{o_id}"
        
class bot_part(ctk.CTkFrame):
    def __init__(self, master, c_id, cal, order_id, **kwargs):
        super().__init__(master, **kwargs)     
        self.w = kwargs["width"]
        self.order_id = order_id
        self.c_id = c_id
        self.cal = cal
        self.toplevel_window = None
        self.totalsum = 0
        self.allbar = 1
        self.save_file = []

        # top title
        self.top_bar = title(self,width=self.w, height=40, fg_color="#EEEEEE")
        self.top_bar.place(x=0,y=0)

        # mid data
        self.mid_frame = ctk.CTkScrollableFrame(self,width=self.w,height=kwargs["height"]-200, fg_color="#EEEEEE")
        self.mid_frame.place(x=0,y=40)
        self.mid_frame.master = self
        self.entry_1 = data_entrybox(self.mid_frame ,width=self.w, fg_color="#EEEEEE")
        self.entry_1.pack()
        self.save_file.append(self.entry_1)

        # bot button
        self.bot_frame = ctk.CTkFrame(self,width=self.w,height=40, fg_color="#DDDDDD")
        self.bot_frame.place(x=0,y=kwargs["height"]-160)       
        self.btn_exit = ctk.CTkButton(self.bot_frame,width=150,height=30,text="重設訂單", fg_color='#3B8ED0', font=("microsoft yahei", 14, 'bold'))
        self.btn_save = ctk.CTkButton(self.bot_frame,width=150,height=30,text="存檔", fg_color='#3B8ED0', font=("microsoft yahei", 14, 'bold'))
        self.total = ctk.CTkLabel(self.bot_frame,text="總計：",font=("microsoft yahei", 20, 'bold'), text_color="#000000")
        self.btn_exit.place(x=self.w-400,y=5)
        self.btn_save.place(x=self.w-200,y=5)
        self.total.place(x=10,y=7)

        # event
        self.btn_save.bind("<Button-1>", self.save_data)
        
    def next_row(self, event):
        self.allbar += 1
        self.entry_1 = data_entrybox(self.mid_frame, width=self.w, fg_color="#EEEEEE")
        self.entry_1.pack()
        self.entry_1.item_id.focus()
        self.save_file.append(self.entry_1)

    def save_data(self, event):
        for i in range(len(self.save_file)):
            if self.save_file[i].item_id.get() == "":
                if i != 0:
                    self.save_file.pop(i)

        try:
            if self.save_file[0].item_id.get() == "" :
                tk.messagebox.showinfo(title='儲存銷貨單', message="未輸入資料!!")
                
            else: 
                con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
                with con:
                    cur = con.cursor()
                    cur.execute(f"insert into order_form(o_id, c_id) \
                                values('{self.order_id}','{self.c_id.get()}')")
                    for entrybox in self.save_file:
                        cur.execute(f"insert into goods(o_id,item_id,item_name,date,specification,size,price,quantity,sub_total,remark)\
                                    values('{self.order_id}','{entrybox.item_id.get()}','{entrybox.item_name.get()}', \
                                        '{self.cal.get_date()}','{entrybox.specification.get()}','{entrybox.size.get()}', \
                                        '{entrybox.price.get()}','{entrybox.quantity.get()}','{entrybox.subtotal.get()}', \
                                        '{entrybox.remark.get()}')")
                    con.commit()

                tk.messagebox.showinfo(title='儲存銷貨單', message="存檔成功")
        except:
            tk.messagebox.showinfo(title='儲存銷貨單', message="未輸入資料")

class title(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/8

        self.bar_2 = ctk.CTkLabel(self,text="品項代號", width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self,text="品項名稱", width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self,text="規格",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self,text="大小",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_6 = ctk.CTkLabel(self,text="數量",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_7 = ctk.CTkLabel(self,text="價錢",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF")) 

        self.bar_8 = ctk.CTkLabel(self,text="小計",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_9 = ctk.CTkLabel(self,text="備註",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2.grid(row=0, column=0)
        self.bar_3.grid(row=0, column=1)
        self.bar_4.grid(row=0, column=2)
        self.bar_5.grid(row=0, column=3)
        self.bar_6.grid(row=0, column=4)
        self.bar_7.grid(row=0, column=5)       
        self.bar_8.grid(row=0, column=6)
        self.bar_9.grid(row=0, column=7)

class data_entrybox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)        
        w = (kwargs["width"]-20)/8
        self.master = master

        self.item_id = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.item_name = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.specification = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.size = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.quantity = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.price = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.subtotal = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.remark = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")

        self.item_id.grid(row=0,column=0)
        self.item_name.grid(row=0,column=1)
        self.specification.grid(row=0,column=2)
        self.size.grid(row=0,column=3)
        self.quantity.grid(row=0,column=4)
        self.price.grid(row=0,column=5)
        self.subtotal.grid(row=0,column=6)
        self.remark.grid(row=0,column=7)

        # event
        self.item_id.bind('<Tab>', self.set_item_name)
        self.quantity.bind('<Tab>', self.total_price)
        self.price.bind('<Tab>', self.total_price)
        self.remark.bind('<Tab>', self.master.master.next_row)

    def set_item_name(self, event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            with con:
                cur = con.cursor()
                cur.execute(f"SELECT item_name from item where item_id = '{self.item_id.get()}'")
                result = cur.fetchone()

            self.item_name.delete(0, len(self.item_name.get()))
            self.item_name.insert(0,str(result[0]).rstrip())
            self.specification.focus()

    def total_price(self, event):
        price = self.price.get()
        quan = self.quantity.get()
        
        if price=="" or quan=="":
            total = 0
            self.master.master.totalsum += total

        elif self.subtotal.get() == "":
            total = int(price) * int(quan)
            self.master.master.totalsum += total
            self.subtotal.insert(0,total)
            self.remark.focus()

        else:
            total = int(price) * int(quan)
            self.master.master.totalsum += (total-int(self.subtotal.get()))
            self.subtotal.delete(0, len(self.subtotal.get()))
            self.subtotal.insert(0,total)
            self.remark.focus()

        self.master.master.total.configure(text=f"總計：{self.master.master.totalsum:,}")

class Into_Order_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def back_to_order(event):
            self.master.intomain.destroy()
            self.master.main.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

        def reset(event):
            self.top_part.destroy()
            self.top_part = top_part(self, width=kwargs["width"]-80, height=kwargs["height"]-120, fg_color="#EEEEEE")
            
            self.back_btn = ctk.CTkButton(self.top_part.bot.bot_frame, 
                                          width=150, height=30, 
                                          text="返回", 
                                          fg_color='#3B8ED0', 
                                          font=("microsoft yahei", 14, "bold"))
            
            self.top_part.place(x=35,y=25)
            self.back_btn.place(x=kwargs["width"]-680, y=5)

            self.back_btn.bind("<Button-1>", back_to_order)
            self.top_part.bot.btn_exit.bind('<Button-1>', reset)

        self.top_part = top_part(self, width=kwargs["width"]-80, height=kwargs["height"]-120, fg_color="#EEEEEE")
        
        self.back_btn = ctk.CTkButton(self.top_part.bot.bot_frame, 
                                      width=150, height=30, 
                                      text="返回",
                                      fg_color='#3B8ED0',
                                      font=("microsoft yahei", 14, "bold"))
        
        self.top_part.place(x=35,y=25)
        self.back_btn.place(x=kwargs["width"]-680, y=5)

        # event
        self.top_part.bot.btn_exit.bind('<Button-1>', reset)
        self.back_btn.bind("<Button-1>", back_to_order)
        