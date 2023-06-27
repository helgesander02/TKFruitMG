import customtkinter as ctk
import psycopg2
from datetime import date
from .into_top_level import Top_level_view_information, Top_level_item
# from .accounting import Accounting_Main_Frame

class left_part(ctk.CTkFrame):
    def __init__(self, master, o_id, m_id, **kwargs):
        super().__init__(master, **kwargs)
        def viewinformation(event):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Top_level_view_information(self)
                self.toplevel_window.attributes('-topmost','true')
                con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
                #con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
                cur = con.cursor()
                cur.execute(f"SELECT item_name, specification, size, price, quantity, sub_total, remark FROM goods WHERE o_id = '{self.o_id}'")
                result = cur.fetchall()
                cur.close()
                con.close()

                for r in result:
                    it = Top_level_item(self.toplevel_window.mid, width=700-20, fg_color="#EEEEEE")
                    it.pack()
                    it.item_name_entry.insert(0, str(r[0]).rstrip())
                    it.norm_entry.insert(0, str(r[1]).rstrip())
                    it.size_entry.insert(0, str(r[2]).rstrip())
                    it.price_entry.insert(0, str(r[3]).rstrip())
                    it.quantity_entry.insert(0, str(r[4]).rstrip())
                    it.total_entry.insert(0, str(r[5]).rstrip())
                    it.remark_entry.insert(0, str(r[6]).rstrip())
         
            else:
                self.toplevel_window.focus()

        def rightbot_reset(event):
            self.right_bot.grid_forget()
            self.right_bot = right_bot_part(self,width=self.w-450,height=self.h-450,fg_color="#EEEEEE")
            self.right_bot.bot.reset_btn.bind("<Button-1>", rightbot_reset)
            self.right_bot.bot.confirm_btn.bind("<Button-1>", rightbot_confirm)
            self.right_bot.place(x=400,y=340)
        
        def rightbot_confirm(event):
            if len(self.right_bot.mid.all_entry) != 0:
                con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
                #con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
                cur = con.cursor()
                cur.execute(f"insert into accounting(ac_id, o_id) \
                        values('{self.ac_id}','{self.o_id}')")
                for en in self.right_bot.mid.all_entry:
                    cur.execute(f"insert into receipt(ac_id, date, m_way, money, discount, remark)\
                            values('{self.ac_id}','{en.bar_1.get()}','{en.bar_2.get()}','{en.bar_3.get()}','{en.bar_4.get()}','{en.bar_5.get()}')")      
                con.commit()
                con.close()
                self.right_bot.bot.save.configure(text="已儲存")
            else:
                self.right_bot.bot.save.configure(text="未按下Enter")

        def reload_right_top_mid(event):
            self.right_top.mid.place_forget()
            self.right_top = right_top_part(self,width=self.w-450,height=330,fg_color="#EEEEEE")
            self.right_top.mid.insertdata(self.o_id)
            self.right_top.bot.sum.configure(text=f"收款總額：{self.right_top.mid.sum}")
            self.right_top.place(x=400,y=0)

        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.o_id = o_id
        self.m_id = m_id
        self.ac_id = self.select_ac_id()
        self.toplevel_window = None
        self.customer_id = ctk.CTkLabel(self, text=f"客戶編號：{self.m_id}", font=("microsoft yahei", 20, 'bold'))

        self.order_id = ctk.CTkLabel(self, text=f"訂單編號：{self.o_id}", font=("microsoft yahei", 20, 'bold'))

        self.information_btn = ctk.CTkButton(self,width=320,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="查看訂單細節",
                                                    font=("microsoft yahei", 16, 'bold'),
                                                    )
        self.information_btn.bind("<Button-1>", viewinformation) 

        self.location = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20, 'bold'))

        self.forwark_btn = ctk.CTkButton(self,width=155,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="下一筆",
                                                    font=("microsoft yahei", 16, 'bold'),
                                                    )
        
        self.backward_btn = ctk.CTkButton(self,width=155,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="上一筆",
                                                    font=("microsoft yahei", 16, 'bold'),
                                                    )


        self.right_top = right_top_part(self,width=self.w-450,height=330,fg_color="#EEEEEE")
        self.right_top.mid.insertdata(self.o_id)
        self.right_top.bot.sum.configure(text=f"收款總額：{self.right_top.mid.sum}")

        self.right_bot = right_bot_part(self,width=self.w-450,height=self.h-450,fg_color="#EEEEEE")
        self.right_bot.bot.reset_btn.bind("<Button-1>", rightbot_reset)
        self.right_bot.bot.confirm_btn.bind("<Button-1>", rightbot_confirm)
        self.right_bot.bot.confirm_btn.bind("<Button-1>", reload_right_top_mid)
        
        self.customer_id.place(x=25,y=25)
        self.order_id.place(x=25,y=80)
        self.information_btn.place(x=25,y=150)
        self.location.place(x=25,y=self.h-230)
        self.forwark_btn.place(x=200,y=self.h-160)
        self.backward_btn.place(x=25,y=self.h-160)
             
        self.right_top.place(x=400,y=0)
        self.right_bot.place(x=400,y=340)

    def select_ac_id(self):
        ac = f"ac{self.m_id}"
        #con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        cur = con.cursor()
        cur.execute(f"select ac_id from accounting")
        ac_all = cur.fetchall()    
        cur.close()
        con.close()
        if len(ac_all) > 0:     
            n_id = str(ac_all[-1][0]).rstrip()
            ac_id = str(int(n_id[len(ac):]) + 1)
            return f"{ac}{ac_id}"
        else:     
            return f"{ac}1"     

class right_top_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.top = right_top_topbar(self,width=self.w,height=40,fg_color="#EEEEEE")
        self.mid = right_top_mid(self,width=self.w-20,height=self.h-80,fg_color="#EEEEEE")
        self.bot = right_top_botbar(self,width=self.w,height=40,fg_color="#DDDDDD")

        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=40)
        self.bot.place(x=0,y=self.h-40)

class right_top_topbar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/5

        self.bar_1 = ctk.CTkLabel(self,text="收款日期",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self,text="收款方式",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self,text="收款金額",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self,text="折讓",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self,text="收款備註",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)

class right_top_mid(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.sum = 0

    def insertdata(self, o_id):
        #con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        cur = con.cursor()
        cur.execute(f"SELECT receipt.ac_id, receipt.date, receipt.m_way, SUM(receipt.money), SUM(receipt.discount), receipt.remark \
                            FROM accounting JOIN receipt \
                            ON accounting.ac_id = receipt.ac_id \
                            WHERE accounting.o_id = '{o_id}' \
                            GROUP BY receipt.ac_id, receipt.date, receipt.m_way, receipt.remark")
        result = cur.fetchall()    
        cur.close()
        con.close()

        for row in range(len(result)):
            entry = entrybox(self ,width=self.w)
            entry.pack()

            entry.bar_1.insert(0, str(result[row][1]).rstrip())
            entry.bar_2.insert(0, str(result[row][2]).rstrip())
            entry.bar_3.insert(0, str(result[row][3]).rstrip())
            entry.bar_4.insert(0, str(result[row][4]).rstrip())
            entry.bar_5.insert(0, str(result[row][5]).rstrip())
            self.sum += int(result[row][3])-int(result[row][4])
        
class right_top_botbar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.sum = ctk.CTkLabel(self,text="收款總額：", font=("microsoft yahei", 14, 'bold'))
        self.sum.place(x=kwargs["width"]-200,y=5)

class right_bot_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.top = right_bot_topbar(self,width=self.w,height=40,fg_color="#EEEEEE")
        self.mid = right_bot_mid(self,width=self.w-20,height=self.h-80,fg_color="#EEEEEE")
        self.bot = right_bot_botbar(self,width=self.w,height=40,fg_color="#DDDDDD")

        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=40)
        self.bot.place(x=0,y=self.h-40)

class right_bot_topbar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/5

        self.bar_1 = ctk.CTkLabel(self,text="收款日期",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self,text="收款方式",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self,text="收款金額",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self,text="折讓",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self,text="收款備註",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)

class entrybox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/5
        self.bar_1 = ctk.CTkEntry(self,width=w,height=40)
        self.bar_2 = ctk.CTkEntry(self,width=w,height=40)
        self.bar_3 = ctk.CTkEntry(self,width=w,height=40)
        self.bar_4 = ctk.CTkEntry(self,width=w,height=40)
        self.bar_5 = ctk.CTkEntry(self,width=w,height=40)

        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)

class right_bot_mid(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def next_row(event):
            self.entry_1 = entrybox(self, width=kwargs["width"])
            self.entry_1.pack()
            self.entry_1.bar_1.focus()
            self.entry_1.bar_5.bind('<Return>',temp_data)
            self.entry_1.bar_5.bind('<Return>',next_row)

        def temp_data(event):
            self.all_entry.append(self.entry_1)

        self.all_entry = []
        self.entry_1 = entrybox(self ,width=kwargs["width"])
        if date.today().month < 10:
            self.entry_1.bar_1.insert(0, f"{date.today().year}0{date.today().month}{date.today().day}")
        else:
            self.entry_1.bar_1.insert(0, f"{date.today().year}{date.today().month}{date.today().day}")
        self.entry_1.pack()

        self.entry_1.bar_5.bind('<Return>',temp_data)
        self.entry_1.bar_5.bind('<Return>',next_row)

class right_bot_botbar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.reset_btn = ctk.CTkButton(self,width=150,height=30,
                                                    fg_color="#3B8ED0",
                                                    text="重設入賬",
                                                    font=("microsoft yahei", 14, 'bold'),
                                                    )

        self.confirm_btn = ctk.CTkButton(self,width=150,height=30,
                                                    fg_color="#3B8ED0",
                                                    text="確認入賬",
                                                    font=("microsoft yahei", 14, 'bold'),
                                                    )

        self.save = ctk.CTkLabel(self, text="", font=("microsoft yahei", 14, 'bold'), text_color="#FF0000")

        self.reset_btn.place(x=kwargs["width"]-400,y=5)
        self.confirm_btn.place(x=kwargs["width"]-200,y=5) 
        self.save.place(x=kwargs["width"]-1000,y=5)   

class Into_Account_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, order_id_select, menber_id, **kwargs):
        super().__init__(master, **kwargs)
        def orderforwark(event):
            if self.location+1 < len(self.order_id_select):
                self.location += 1
                self.o_id = self.order_id_select[self.location]

                self.left.grid_forget()
                self.left = left_part(self, self.o_id, self.m_id, 
                                        width=self.w, height=self.h, fg_color="#FFFFFF")
                self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
                self.left.location.configure(text=f"總共選擇{len(self.order_id_select)}筆訂單   現在位置第{self.location+1}筆")
                self.left.forwark_btn.bind("<Button-1>", orderforwark)
                self.left.backward_btn.bind("<Button-1>", orderbackward)
    
        def orderbackward(event):
            if self.location-1 > -1:
                self.location -= 1
                self.o_id = self.order_id_select[self.location]
                
                self.left.grid_forget()
                self.left = left_part(self, self.o_id, self.m_id, 
                                        width=self.w, height=self.h, fg_color="#FFFFFF")
                self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
                self.left.location.configure(text=f"總共選擇{len(self.order_id_select)}筆訂單   現在位置第{self.location+1}筆")
                self.left.forwark_btn.bind("<Button-1>", orderforwark)
                self.left.backward_btn.bind("<Button-1>", orderbackward)
        def back_to_accounting(event):
            from .accounting import Accounting_Main_Frame
            self.left.grid_forget()
            self.left = Accounting_Main_Frame(self, width=kwargs["width"]-20, height=kwargs["height"]-20, fg_color="#FFFFFF")
            self.left.grid(row=0,column=0,padx=10,pady=10)

        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.location = 0
        self.order_id_select = order_id_select
        self.o_id = self.order_id_select[self.location]
        self.m_id = menber_id

        self.left = left_part(self, self.o_id, self.m_id, 
                                        width=self.w, height=self.h, fg_color="#FFFFFF")
        self.back_btn = ctk.CTkButton(self.left.right_bot.bot,width=150,height=30,text="返回",font=("microsoft yahei", 14, "bold"),)
        self.back_btn.place(x=kwargs["width"]-1050,y=5)
        self.back_btn.bind("<Button-1>", back_to_accounting)
        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        self.left.location.configure(text=f"總共選擇{len(self.order_id_select)}筆訂單   現在位置第{self.location+1}筆")
        self.left.forwark_btn.bind("<Button-1>", orderforwark)
        self.left.backward_btn.bind("<Button-1>", orderbackward)

    
    
          
