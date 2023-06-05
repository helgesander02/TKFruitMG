import customtkinter as ctk
import tkcalendar as tkc
import psycopg2
from datetime import date
class bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bar_1 = ctk.CTkLabel(self,text="序號",font=("Arial",24))
        self.bar_2 = ctk.CTkLabel(self,text="品項代號",font=("Arial",24))
        self.bar_3 = ctk.CTkLabel(self,text="品項名稱",font=("Arial",24))
        self.bar_4 = ctk.CTkLabel(self,text="規格",font=("Arial",24))
        self.bar_5 = ctk.CTkLabel(self,text="大小",font=("Arial",24))
        self.bar_6 = ctk.CTkLabel(self,text="價錢",font=("Arial",24))
        self.bar_7 = ctk.CTkLabel(self,text="數量",font=("Arial",24))
        self.bar_8 = ctk.CTkLabel(self,text="小計",font=("Arial",24))
        self.bar_9 = ctk.CTkLabel(self,text="備註",font=("Arial",24))

        self.bar_1.place(x=20,y=10)
        self.bar_2.place(x=220,y=10)
        self.bar_3.place(x=420,y=10)
        self.bar_4.place(x=620,y=10)
        self.bar_5.place(x=820,y=10)
        self.bar_6.place(x=1020,y=10)
        self.bar_7.place(x=1220,y=10)
        self.bar_8.place(x=1420,y=10)
        self.bar_9.place(x=1620,y=10)

class entrybox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.serial = ctk.CTkEntry(self,width=200,height=40)
        self.item_id = ctk.CTkEntry(self,width=200,height=40)
        self.item_name = ctk.CTkEntry(self,width=200,height=40)
        self.specification = ctk.CTkEntry(self,width=200,height=40)
        self.size = ctk.CTkEntry(self,width=200,height=40)
        self.price = ctk.CTkEntry(self,width=200,height=40)
        self.quantity = ctk.CTkEntry(self,width=200,height=40)
        self.subtotal = ctk.CTkEntry(self,width=200,height=40)
        self.remark = ctk.CTkEntry(self,width=200,height=40)

        self.serial.grid(row=0,column=0)
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
        def select_od_id():
            con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')
            
            cur = con.cursor()
            cur.execute(f"select order_id from order_it where date='{date.today()}' order by order_id")
            dt_time = cur.fetchall()
            td = date.today()
            order_id = f"{td.year}{td.month}{td.day}"
            cur.close()
            con.close()
            if len(dt_time) == 0:
                return f"{order_id}0001"
            else:
                n_id = str(dt_time[-1][0]).rstrip()
                o_id = str(int(n_id[-4:]) + 1).zfill(4)
                # print(n_id,o_id)
                return f"{order_id}{o_id}"
        super().__init__(master, **kwargs)
        self.c_id = ctk.CTkEntry(self,width=250,height=50,placeholder_text="輸入客戶代號",font=("Arial",24))
        self.cal = tkc.DateEntry(self)
        self.order_id = ctk.CTkLabel(self)
        self.c_id.place(x=40,y=30)
        self.cal.place(x=310,y=30)
        self.order_id.place(x=310,y=60)
        self.c_id.focus()
        self.order_id.configure(text=select_od_id())
        self.bot = bot(self,width=1800,height=630,border_width=3,border_color="green",c_id=self.c_id,cal=self.cal,order_id=self.order_id.cget("text"))
        self.bot.place(x=0,y=120)
        
class bot(ctk.CTkFrame):
    def __init__(self, master, c_id, cal,order_id, **kwargs):
        super().__init__(master, **kwargs)
        def next_row(event):
            self.entry_1 = entrybox(self.mid_frame)
            self.entry_1.pack()
            self.entry_1.serial.focus()
            self.entry_1.remark.bind('<Return>',temp_data)
            self.entry_1.remark.bind('<Return>',next_row)
            self.entry_1.item_id.bind('<Tab>',item_name)
            self.entry_1.quantity.bind('<Tab>',total_price)
        def item_name(event):
            con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')

            cur = con.cursor()
            cur.execute(f"SELECT item_name from item where item_id = '{self.entry_1.item_id.get()}'")
            result = cur.fetchone()
            cur.close()
            self.entry_1.item_name.insert(0,str(result[0]).rstrip())
            self.entry_1.specification.focus()            
        def total_price(event):
            price = self.entry_1.price.get()
            quan = self.entry_1.quantity.get()
            total = int(price) * int(quan)
            self.totalsum += total
            self.entry_1.subtotal.insert(0,total)
            self.entry_1.remark.focus()
            self.total.configure(text="總計："+str(self.totalsum))
        def temp_data(event):
            self.temp = []
            self.temp.append(self.entry_1.item_id.get())
            self.temp.append(self.entry_1.item_name.get())
            self.temp.append(self.entry_1.specification.get())
            self.temp.append(self.entry_1.size.get())
            self.temp.append(self.entry_1.price.get())
            self.temp.append(self.entry_1.quantity.get())
            self.temp.append(self.entry_1.subtotal.get())
            self.temp.append(self.entry_1.remark.get())
            self.temp.append(c_id.get())
            self.temp.append(cal.get_date())
            self.temp.append(order_id)
            self.save_file.append(self.temp)
            print(order_id)
        def save_data():
            con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')
            cur = con.cursor()
            for i in self.save_file:
                cur.execute(f"insert into order_it(item_id, item_name, specification, size, price, quantity, subtotal, remark, c_id, date, order_id)\
                            values('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}','{i[8]}','{i[9]}','{i[10]}')")
            cur.close()
            con.commit()
            con.close()
            # print(self.save_file)
        self.top_bar = bar(self,width=1800,height=40,fg_color="#EEEEEE")
        self.top_bar.place(x=0,y=0)
        self.mid_frame = ctk.CTkScrollableFrame(self,width=1780,height=550)
        self.mid_frame.place(x=0,y=40)
        self.bot_frame = ctk.CTkFrame(self,width=1800,height=40,fg_color="#EEEEEE")
        self.bot_frame.place(x=0,y=590)
        self.btn_exit = ctk.CTkButton(self.bot_frame,width=120,height=20,text="離開")
        self.btn_save = ctk.CTkButton(self.bot_frame,width=120,height=20,text="存檔",command=save_data)
        self.btn_exit.place(x=1510,y=10)
        self.btn_save.place(x=1650,y=10)
        self.total = ctk.CTkLabel(self.bot_frame,text="總計：",font=("Arial",20))
        self.total.place(x=0,y=7)
        self.totalsum = 0
        self.save_file = []
        self.entry_1 = entrybox(self.mid_frame)
        self.entry_1.pack()
        # self.entry_1.serial.bind('<Tab>',)
        self.entry_1.item_id.bind('<Tab>',item_name)
        self.entry_1.remark.bind('<Return>',temp_data)
        self.entry_1.remark.bind('<Return>',next_row)
        self.entry_1.quantity.bind('<Tab>',total_price)
        
class Order_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        top_part = top(self,width=1800,height=750)
        top_part.place(x=60,y=60)
        