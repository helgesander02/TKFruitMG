import customtkinter as ctk
import tkinter as tk
import tkcalendar as tkc
import psycopg2

class bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/8
        # self.bar_1 = ctk.CTkLabel(self,text="序號", width=w, height=40,
        #                             fg_color='#3B8ED0',
        #                             font=("microsoft yahei", 14, 'bold'), 
        #                             text_color=("#FFFFFF"))

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

        self.bar_6 = ctk.CTkLabel(self,text="價錢",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_7 = ctk.CTkLabel(self,text="數量",width=w, height=40,
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

        # self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)
        self.bar_6.grid(row=0,column=5)
        self.bar_7.grid(row=0,column=6)
        self.bar_8.grid(row=0,column=7)
        self.bar_9.grid(row=0,column=8)

class entrybox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = (kwargs["width"]-20)/8
        # self.serial = ctk.CTkEntry(self,width=w,height=40)
        self.item_id = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.item_name = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.specification = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.size = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.price = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.quantity = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.subtotal = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.remark = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")

        # self.serial.grid(row=0,column=0)
        self.item_id.grid(row=0,column=1)
        self.item_name.grid(row=0,column=2)
        self.specification.grid(row=0,column=3)
        self.size.grid(row=0,column=4)
        self.price.grid(row=0,column=5)
        self.quantity.grid(row=0,column=6)
        self.subtotal.grid(row=0,column=7)
        self.remark.grid(row=0,column=8)

class top(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def ch_date(*args):
            self.order_id.configure(text=f"訂貨單編號：{self.select_od_id(date_in=self.sel.get())}", font=("microsoft yahei", 24, 'bold'), text_color="#000000")
            try:
                self.bot.order_id = self.order_id.cget("text")[6:]
            except:
                pass

        self.order_id = ctk.CTkLabel(self)
        self.order_id.place(x=kwargs["width"]-400,y=50)

        self.c_id = ctk.CTkEntry(self,width=250,height=50,placeholder_text="輸入客戶代號",font=("microsoft yahei", 24), fg_color="#DDDDDD", text_color="#000000")
        self.c_id.place(x=40,y=40)

        self.sel = ctk.StringVar()
        self.sel.trace('w',ch_date)
        self.cal = tkc.DateEntry(self, font=("microsoft yahei", 20),textvariable=self.sel,date_pattern="yyyy-mm-dd")
        self.cal.place(x=450,y=40)

        self.c_id.focus()
        self.order_id.configure(text=f"訂貨單編號：{self.select_od_id(date_in=self.cal.get_date())}", font=("microsoft yahei", 24, 'bold'), text_color="#000000")
        self.bot = bot(self,width=kwargs["width"],height=kwargs["height"],c_id=self.c_id,cal=self.cal, order_id=self.order_id.cget("text")[6:], fg_color="#EEEEEE")
        self.bot.place(x=0,y=120)

    def select_od_id(self,date_in):
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        with con:
            cur = con.cursor()
            cur.execute(f"select o_id,date from goods where date='{date_in}' order by o_id")
            dt_time = cur.fetchall()
            order_id = f"{str(date_in)[:4]}{str(date_in)[5:7]}{str(date_in)[8:]}"

        if len(dt_time) == 0:
            return f"{order_id}0001"
        else:
            n_id = str(dt_time[-1][0]).rstrip()
            o_id = str(int(n_id[-4:]) + 1).zfill(4)
            return f"{order_id}{o_id}"
        
class bot(ctk.CTkFrame):
    def __init__(self, master, c_id, cal,order_id, **kwargs):
        super().__init__(master, **kwargs)
        def next_row(event):
            self.allbar += 1
            self.entry_1 = entrybox(self.mid_frame, width=self.w, fg_color="#EEEEEE")
            self.entry_1.pack()
            self.entry_1.item_id.focus()
            self.save_file.append(self.entry_1)
            self.entry_1.remark.bind('<Tab>',next_row)
            self.entry_1.item_id.bind('<Tab>',item_name)
            self.entry_1.quantity.bind('<Tab>',total_price)

        def item_name(event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
            with con:
                cur = con.cursor()
                cur.execute(f"SELECT item_name from item where item_id = '{self.entry_1.item_id.get()}'")
                result = cur.fetchone()

            if self.entry_1.item_name.get() == "":
                self.entry_1.item_name.insert(0,str(result[0]).rstrip())
                self.entry_1.specification.focus()
            else:
                 self.entry_1.specification.focus()

        def total_price(event):
            price = self.entry_1.price.get()
            quan = self.entry_1.quantity.get()
            
            if price=="" or quan=="":
                total = 0
                self.totalsum += total

            elif self.entry_1.subtotal.get() == "":
                total = int(price) * int(quan)
                self.totalsum += total
                self.entry_1.subtotal.insert(0,total)
                self.entry_1.remark.focus()

            else:
                total = int(price) * int(quan)
                self.totalsum += (total-int(self.entry_1.subtotal.get()))
                self.entry_1.subtotal.delete(0, len(self.entry_1.subtotal.get()))
                self.entry_1.subtotal.insert(0,total)
                self.entry_1.remark.focus()

            self.total.configure(text="總計："+str(self.totalsum))
            

        self.w = kwargs["width"]
        self.order_id = order_id
        self.c_id = c_id
        self.cal = cal
        self.top_bar = bar(self,width=self.w,height=40,fg_color="#EEEEEE")
        self.top_bar.place(x=0,y=0)

        self.mid_frame = ctk.CTkScrollableFrame(self,width=self.w,height=kwargs["height"]-200, fg_color="#EEEEEE")
        self.mid_frame.place(x=0,y=40)

        self.bot_frame = ctk.CTkFrame(self,width=self.w,height=40, fg_color="#DDDDDD")
        self.bot_frame.place(x=0,y=kwargs["height"]-160)       
        self.btn_exit = ctk.CTkButton(self.bot_frame,width=150,height=30,text="重設訂單", font=("microsoft yahei", 14, 'bold'))
        self.btn_save = ctk.CTkButton(self.bot_frame,width=150,height=30,text="存檔", font=("microsoft yahei", 14, 'bold') ,command=self.save_data)
        self.btn_exit.place(x=self.w-400,y=5)
        self.btn_save.place(x=self.w-200,y=5)
        self.total = ctk.CTkLabel(self.bot_frame,text="總計：",font=("microsoft yahei", 20, 'bold'), text_color="#000000")
        self.total.place(x=10,y=7)

        self.toplevel_window = None

        self.totalsum = 0
        self.allbar = 1
        self.save_file = []

        self.entry_1 = entrybox(self.mid_frame ,width=self.w, fg_color="#EEEEEE")
        self.entry_1.pack()
        self.entry_1.item_id.bind('<Tab>',item_name)
        self.save_file.append(self.entry_1)
        self.entry_1.remark.bind('<Tab>',next_row)
        self.entry_1.price.bind('<Tab>',total_price)
        self.entry_1.quantity.bind('<Tab>',total_price)

    def save_data(self):
        for i in range(len(self.save_file)):
            if self.save_file[i].item_id.get() == "":
                self.save_file.pop(i)

        try:
            if len(self.save_file) == 0:
                tk.messagebox.showinfo(title='儲存銷貨單', message="未輸入資料!!")
                
            else: 
                con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
                #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
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

class Into_Order_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def back_to_order(event):
            from .order import Order_Main_Frame
            self.top_part.place_forget()
            self.top_part = Order_Main_Frame(self, width=kwargs["width"], height=kwargs["height"], fg_color="#FFFFFF")
            self.top_part.grid(row=0,column=0)

        def reset(event):
            self.top_part.place_forget()
            self.top_part = top(self, width=kwargs["width"]-80, height=kwargs["height"]-120, fg_color="#EEEEEE")
            self.top_part.place(x=35,y=25)
            self.back_btn = ctk.CTkButton(self.top_part.bot.bot_frame, width=150,height=30,text="返回",font=("microsoft yahei", 14, "bold"))
            self.back_btn.place(x=kwargs["width"]-680, y=5)
            self.back_btn.bind("<Button-1>", back_to_order)
            self.top_part.bot.btn_exit.bind('<Button-1>', reset)

        self.top_part = top(self, width=kwargs["width"]-80, height=kwargs["height"]-120, fg_color="#EEEEEE")
        self.top_part.place(x=35,y=25)
        self.top_part.bot.btn_exit.bind('<Button-1>', reset)
        self.back_btn = ctk.CTkButton(self.top_part.bot.bot_frame, width=150,height=30,text="返回",font=("microsoft yahei", 14, "bold"))
        self.back_btn.place(x=kwargs["width"]-680, y=5)
        self.back_btn.bind("<Button-1>", back_to_order)