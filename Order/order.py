import customtkinter as ctk
import tkcalendar as tkc
import psycopg2
from datetime import date

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
        self.item_id = ctk.CTkEntry(self,width=w,height=40)
        self.item_name = ctk.CTkEntry(self,width=w,height=40)
        self.specification = ctk.CTkEntry(self,width=w,height=40)
        self.size = ctk.CTkEntry(self,width=w,height=40)
        self.price = ctk.CTkEntry(self,width=w,height=40)
        self.quantity = ctk.CTkEntry(self,width=w,height=40)
        self.subtotal = ctk.CTkEntry(self,width=w,height=40)
        self.remark = ctk.CTkEntry(self,width=w,height=40)

        # self.serial.grid(row=0,column=0)
        self.item_id.grid(row=0,column=1)
        self.item_name.grid(row=0,column=2)
        self.specification.grid(row=0,column=3)
        self.size.grid(row=0,column=4)
        self.price.grid(row=0,column=5)
        self.quantity.grid(row=0,column=6)
        self.subtotal.grid(row=0,column=7)
        self.remark.grid(row=0,column=8)

# class ToplevelWindow(ctk.CTkToplevel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.geometry("150x80")

#         self.label = ctk.CTkLabel(self, text="您已經存檔",font=("Arial", 20))
#         self.label.pack(padx=20, pady=20)


class top(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def select_od_id():
            con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            
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

        self.order_id = ctk.CTkLabel(self)
        self.order_id.place(x=kwargs["width"]-400,y=50)

        self.c_id = ctk.CTkEntry(self,width=250,height=50,placeholder_text="輸入客戶代號",font=("microsoft yahei", 24))
        self.c_id.place(x=40,y=40)

        self.cal = tkc.DateEntry(self, font=("microsoft yahei", 20))
        self.cal.place(x=450,y=40)

        self.c_id.focus()
        self.order_id.configure(text=f"訂貨單編號：{select_od_id()}", font=("microsoft yahei", 24, 'bold'))
        self.bot = bot(self,width=kwargs["width"],height=kwargs["height"],c_id=self.c_id,cal=self.cal,order_id=self.order_id.cget("text"))
        self.bot.place(x=0,y=120)
        
class bot(ctk.CTkFrame):
    def __init__(self, master, c_id, cal,order_id, **kwargs):
        super().__init__(master, **kwargs)
        def next_row(event):
            self.allbar += 1
            self.entry_1 = entrybox(self.mid_frame, width=self.w)
            self.entry_1.pack()
            self.entry_1.item_id.focus()
            self.entry_1.remark.bind('<Return>',temp_data)
            self.entry_1.remark.bind('<Return>',next_row)
            self.entry_1.item_id.bind('<Tab>',item_name)
            self.entry_1.quantity.bind('<Tab>',total_price)

        def item_name(event):
            con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")

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
        def exit():
            pass
        self.w = kwargs["width"]
        self.top_bar = bar(self,width=self.w,height=40,fg_color="#EEEEEE")
        self.top_bar.place(x=0,y=0)

        self.mid_frame = ctk.CTkScrollableFrame(self,width=self.w,height=kwargs["height"]-200)
        self.mid_frame.place(x=0,y=40)

        self.bot_frame = ctk.CTkFrame(self,width=self.w,height=40,fg_color="#EEEEEE")
        self.bot_frame.place(x=0,y=kwargs["height"]-160)       
        self.btn_exit = ctk.CTkButton(self.bot_frame,width=120,height=20,text="重設訂單", font=("microsoft yahei", 12, 'bold'))
        self.btn_save = ctk.CTkButton(self.bot_frame,width=120,height=20,text="存檔", font=("microsoft yahei", 12, 'bold') ,command=self.save_data)
        self.btn_exit.place(x=self.w-300,y=10)
        self.btn_save.place(x=self.w-150,y=10)
        self.total = ctk.CTkLabel(self.bot_frame,text="總計：",font=("microsoft yahei", 20, 'bold'))
        self.total.place(x=10,y=7)

        self.remind = ctk.CTkLabel(self.bot_frame,text="",font=("microsoft yahei", 20, 'bold'))
        self.remind.place(x=kwargs["width"]-400,y=7)


        self.toplevel_window = None

        self.totalsum = 0
        self.allbar = 1
        self.save_file = []

        self.entry_1 = entrybox(self.mid_frame ,width=self.w)
        self.entry_1.pack()
        # self.entry_1.serial.bind('<Tab>',)
        self.entry_1.item_id.bind('<Tab>',item_name)
        self.entry_1.remark.bind('<Return>',temp_data)
        self.entry_1.remark.bind('<Return>',next_row)
        self.entry_1.quantity.bind('<Tab>',total_price)

    def save_data(self):
        con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
        cur = con.cursor()
        for i in self.save_file:
            cur.execute(f"insert into order_it(item_id, item_name, specification, size, price, quantity, subtotal, remark, c_id, date, order_id)\
                            values('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}','{i[8]}','{i[9]}','{i[10]}')")
        cur.close()
        con.commit()
        con.close()
        self.remind.configure(text="已存檔")

    
    # def open_toplevel(self,event):
    #     if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
    #         self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
    #         self.toplevel_window.attributes('-topmost','true')
    #     else:
    #         self.toplevel_window.focus()  # if window exists focus it
        
class Order_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def reset(event):
            self.top_part.place_forget()
            self.top_part = top(self,width=kwargs["width"]-80,height=kwargs["height"]-120)
            self.top_part.place(x=35,y=25)
            self.top_part.bot.btn_exit.bind('<Button-1>', reset)

        self.top_part = top(self,width=kwargs["width"]-80,height=kwargs["height"]-120)
        self.top_part.place(x=35,y=25)
        self.top_part.bot.btn_exit.bind('<Button-1>', reset)