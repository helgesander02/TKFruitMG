import customtkinter as ctk
import tkinter as tk
import tkcalendar as tkc
import psycopg2
from datetime import date
from .into_account import Into_Account_Main_Frame

class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.master = master
        self.customer_id_entry = ctk.CTkEntry(self,width=210, height=50,
                                                    fg_color="#EEEEEE",
                                                    text_color="#000000",
                                                    font=("microsoft yahei", 20, 'bold'),
                                                    placeholder_text="客戶編號" 
                                                    )     

        self.sell_date1_entry = tkc.DateEntry(self, selectmode='day',
                                                    font=("microsoft yahei", 20),year=2000,month=1,day=1,date_pattern="yyyy-mm-dd")
        self.sell_date2_entry = tkc.DateEntry(self, selectmode='day',
                                                    font=("microsoft yahei", 20),date_pattern="yyyy-mm-dd")

        self.finish_chk = ctk.CTkCheckBox(self,width=40,height=40, text="是否隱藏收帳完成的", 
                                                    font=("microsoft yahei", 16, 'bold'),
                                                    text_color=("#333333"),
                                                    )

        self.confirm_btn = ctk.CTkButton(self,width=200,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="確認查詢",
                                                    font=("microsoft yahei", 20, 'bold'),
                                                    )
        self.right_bot = right_bot_part(self,width=self.w-300,height=self.h-120,fg_color="#EEEEEE")
        
        self.customer_id_entry.place(x=25,y=50)
        self.sell_date1_entry.place(x=25,y=300)
        self.sell_date2_entry.place(x=25,y=350)
        self.finish_chk.place(x=25,y=120)
        self.finish_chk.select()
        self.confirm_btn.place(x=25,y=self.h-220)
        self.right_bot.place(x=270,y=5)

        self.right_bot.j_btn.bind("<Button-1>", self.master.open_into_account)
        self.confirm_btn.bind("<Button-1>", self.test)
        self.customer_id_entry.bind("<Return>", self.test)

    def reset(self):
            self.right_bot.destroy()
            self.right_bot = right_bot_part(self,width=self.w-300,height=self.h-120,fg_color="#EEEEEE")
            self.right_bot.place(x=270,y=5)

            self.right_bot.j_btn.bind("<Button-1>", self.master.open_into_account)

    def test(self, event):
        self.reset()
        c_id = self.customer_id_entry.get()

        self.right_bot.InsertData(c_id, 
                                    self.sell_date1_entry.get_date(), 
                                    self.sell_date2_entry.get_date(),
                                    self.finish_chk.get())

class once_enter(ctk.CTkToplevel):
    def __init__(self, master,overage,**kwargs):
        super().__init__(master, **kwargs)
        def insert_receipt():
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
            with con:
                cur = con.cursor()
                money = int(self.entry3.get())
                for i in range(len(overage)):
                    temp = 0
                    if money == 0:break
                    if int(overage[i][1]) <= money:
                        temp = int(overage[i][1])
                        money -= int(overage[i][1])
                    else:
                        temp = money
                        money = 0

                    ac_id = self.select_ac_id(overage[i][2])
                    cur.execute(f"INSERT INTO accounting VALUES('{ac_id}','{overage[i][0]}')")
                    cur.execute(f"INSERT INTO receipt VALUES('{ac_id}','{self.entry1.get()}','{self.entry2.get()}','{temp}','0','')")
                    con.commit()

            master.reload()
            self.destroy()

        self.geometry("300x200")
        self.lbl1 = ctk.CTkLabel(self,text="收款日期",width=100,height=40,font=("microsoft yahei", 14, 'bold'))
        self.lbl2 = ctk.CTkLabel(self,text="收款方式",width=100,height=40,font=("microsoft yahei", 14, 'bold'))
        self.lbl3 = ctk.CTkLabel(self,text="收款金額",width=100,height=40,font=("microsoft yahei", 14, 'bold'))
        self.entry1 = ctk.CTkEntry(self,width=150,height=40)
        if date.today().month<10:
            self.entry1.insert(0, f"{date.today().year}0{date.today().month}{date.today().day}")
        else:
            self.entry1.insert(0, f"{date.today().year}{date.today().month}{date.today().day}")
        self.entry2 = ctk.CTkEntry(self,placeholder_text="收款方式",width=150,height=40)
        self.entry3 = ctk.CTkEntry(self,placeholder_text="收款金額",width=150,height=40)
        self.confirm_btn = ctk.CTkButton(self,text="確認入賬",width=250,height=40,command=insert_receipt,font=("microsoft yahei", 14, 'bold'))
        self.confirm_btn.grid(row=3,column=0,columnspan=2,pady=5)
        self.lbl1.grid(row=0,column=0,padx=5,pady=5)
        self.lbl2.grid(row=1,column=0,padx=5,pady=5)
        self.lbl3.grid(row=2,column=0,padx=5,pady=5)
        self.entry1.grid(row=0,column=1,padx=5,pady=5)
        self.entry2.grid(row=1,column=1,padx=5,pady=5)
        self.entry3.grid(row=2,column=1,padx=5,pady=5)

    def select_ac_id(self,c_id):
        ac = f"ac{c_id}"
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        with con:
            cur = con.cursor()
            cur.execute(f"select ac_id from accounting join order_form on accounting.o_id = order_form.o_id where order_form.c_id = '{c_id}'")
            ac_all = cur.fetchall()    

        if len(ac_all) > 0:
            n_id = str(ac_all[-1][0]).rstrip()
            ac_id = str(int(n_id[len(ac):]) + 1)
            return f"{ac}{ac_id}"
        else:     
            return f"{ac}1"

class right_bot_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.master = master
        self.top = top_bar(self, width=self.w, height=40)
        self.toplevel = None
        self.mid = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-85, fg_color="#EEEEEE")
        self.select_order = []
        self.bot = ctk.CTkFrame(self, width=self.w, height=40, fg_color="#DDDDDD")
        self.nmb = ctk.CTkLabel(self.bot, height=40, text="總額：" ,font=("microsoft yahei", 20, 'bold'), text_color="#000000")
        self.j_btn = ctk.CTkButton(self.bot, width=150, height=30, text="入賬" ,fg_color='#3B8ED0',font=("microsoft yahei", 14, 'bold'))
        self.once_btn = ctk.CTkButton(self.bot, width=150, height=30, text="一次入帳多筆" ,fg_color='#3B8ED0',font=("microsoft yahei", 14, 'bold'),command=self.open_once_enter)
        self.j_text = ctk.CTkLabel(self.bot, width=50, height=40, text="" ,font=("microsoft yahei", 20, 'bold'), text_color="#FF0000")
        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=40)
        self.bot.place(x=0,y=self.h-40)
        self.once_btn.place(x=self.w-400,y=5)
        self.nmb.place(x=20)
        self.j_btn.place(x=self.w-200,y=5)
        self.j_text.place(x=self.w-600)

    def reload(self):
        self.mid.destroy()
        self.mid = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-100, fg_color="#EEEEEE") 
        self.mid.place(x=0,y=40)

        c_id = self.master.customer_id_entry.get()
        self.InsertData(c_id, self.master.sell_date1_entry.get_date(), 
                                    self.master.sell_date2_entry.get_date(),
                                    self.master.finish_chk.get())
        
    def open_once_enter(self):
        if len(self.select_order) == 0:
            tk.messagebox.showinfo(title='', message="請選擇訂單!!")
        else:
            overage = self.SelectOrder_test()
            if self.toplevel is None or not self.toplevel.winfo_exists():
                self.toplevel = once_enter(self,overage)
                self.toplevel.title("")
                self.toplevel.attributes('-topmost','true')
                self.toplevel.focus()
            else:
                self.toplevel.focus()
        
    def InsertData(self, c_id, date1, date2, chk):
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
        with con:
            cur = con.cursor()
            if c_id == "":
                cur.execute(f"SELECT goods.o_id, string_agg(goods.remark,' '), SUM(goods.sub_total) \
                                    FROM order_form JOIN goods \
                                    ON order_form.o_id = goods.o_id \
                                    WHERE goods.date BETWEEN SYMMETRIC '{date1}' AND '{date2}' \
                                    GROUP BY goods.o_id")
                result1 = cur.fetchall()
                cur.execute(f"SELECT accounting.o_id, SUM(receipt.money-receipt.discount) \
                                    FROM accounting JOIN receipt \
                                    ON accounting.ac_id = receipt.ac_id \
                                    WHERE accounting.o_id IN \
                                    ( \
                                    SELECT goods.o_id \
                                    FROM order_form JOIN goods \
                                    ON order_form.o_id = goods.o_id \
                                    WHERE goods.date BETWEEN SYMMETRIC '{date1}' AND '{date2}' \
                                    GROUP BY goods.o_id \
                                    ) \
                                    GROUP BY accounting.o_id")
                result2 = cur.fetchall()  

            else:
                cur.execute(f"SELECT goods.o_id, string_agg(goods.remark,' '), SUM(goods.sub_total) \
                                    FROM order_form JOIN goods \
                                    ON order_form.o_id = goods.o_id \
                                    WHERE order_form.c_id = '{c_id}' AND (goods.date BETWEEN SYMMETRIC '{date1}' AND '{date2}') \
                                    GROUP BY goods.o_id")
                result1 = cur.fetchall()
                cur.execute(f"SELECT accounting.o_id, SUM(receipt.money-receipt.discount) \
                                    FROM accounting JOIN receipt \
                                    ON accounting.ac_id = receipt.ac_id \
                                    WHERE accounting.o_id IN \
                                    ( \
                                    SELECT goods.o_id \
                                    FROM order_form JOIN goods \
                                    ON order_form.o_id = goods.o_id \
                                    WHERE order_form.c_id = '{c_id}' AND (goods.date BETWEEN SYMMETRIC '{date1}' AND '{date2}') \
                                    GROUP BY goods.o_id \
                                    ) \
                                    GROUP BY accounting.o_id")
                result2 = cur.fetchall()             

        s = 0
        for i in range(len(result1)):
            al = 0
            overage = result1[i][2]
            for j in range(len(result2)):
                if result2[j][0] == result1[i][0]:
                    al = result2[j][1]
                    overage -= result2[j][1]

            if overage == 0 and chk == 1: continue
            it = item(self.mid, width=self.w-20, fg_color="#EEEEEE")
            with con:
                cur = con.cursor()
                cur.execute(f"SELECT name FROM customer WHERE customer.c_id = (SELECT c_id FROM order_form WHERE order_form.o_id='{result1[i][0]}')")
                result3 = cur.fetchall()

            it.day.insert(0, f"{result1[i][0][:4]}/{result1[i][0][4:6]}/{result1[i][0][6:8]}")
            it.name.insert(0, f"{result3[0][0]}")
            it.dat.insert(0, f"{result1[i][0]}")
            it.remark.insert(0, f"{result1[i][1]}")
            it.sbtotal.insert(0, f"{result1[i][2]}")
            s+= int(result1[i][2])     
            it.al_total.insert(0, f"{al}")
            it.overage.insert(0, f"{overage}")
           
            self.select_order.append(it)              
            it.pack()
        self.nmb.configure(text=f"總額： {s:,}") 

    def SelectOrder(self):
        select_chkbox = []
        for so in self.select_order:
            if so.chk_box.get() == 1:
                select_chkbox.append(str(so.dat.get().rstrip()))
                
        return select_chkbox
    
    def SelectOrder_test(self):
        select_chkbox = []
        for so in self.select_order:
            if so.chk_box.get() == 1:
                #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
                con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
                with con:
                    cur = con.cursor()
                    cur.execute(f"select c_id from customer where name='{so.name.get()}'")
                    c_all = cur.fetchall() 

                select_chkbox.append([str(so.dat.get().rstrip()),str(so.overage.get().rstrip()), str(c_all[0][0].rstrip())])

        return select_chkbox

class top_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = (kwargs["width"]-100)/7

        self.bar_0 = ctk.CTkLabel(self, width=100, height=40, 
                                    text="選擇",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))
        
        self.bar_1 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="日期",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="客戶名稱",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="銷貨單編號",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="銷貨總計",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="已收金額",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_6 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="餘額",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_7 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="銷貨單備註",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_0.grid(row=0,column=0)
        self.bar_1.grid(row=0,column=1)
        self.bar_2.grid(row=0,column=2)
        self.bar_3.grid(row=0,column=3)
        self.bar_4.grid(row=0,column=4)
        self.bar_5.grid(row=0,column=5)
        self.bar_6.grid(row=0,column=6)
        self.bar_7.grid(row=0,column=7)

class item(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = (kwargs["width"]-100)/7

        self.chk_box = ctk.CTkCheckBox(self,width=100,height=40, fg_color="#FFFFFF", text_color=("#000000"), text="")
        self.day = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color=("#000000"))
        self.name = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color=("#000000"))
        self.dat = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color=("#000000"))
        self.sbtotal = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color=("#000000"))
        self.al_total = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color=("#000000"))
        self.overage = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color=("#000000"))
        self.remark = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color=("#000000"))
        
        self.chk_box.grid(row=0,column=0, sticky=tk.E)
        self.day.grid(row=0,column=1)
        self.name.grid(row=0,column=2)
        self.dat.grid(row=0,column=3)
        self.sbtotal.grid(row=0,column=4)
        self.al_total.grid(row=0,column=5)
        self.overage.grid(row=0,column=6)
        self.remark.grid(row=0,column=7)

class Accounting_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]        
        self.left = left_part(self, width=self.w, height=self.h, fg_color="#FFFFFF")
        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
    
    def open_into_account(self, event):
            order_id_select = self.left.right_bot.SelectOrder()
            if order_id_select == []: 
                self.left
                self.left.right_bot.j_text.configure(text="請選擇訂單")
            else:
                self.left.destroy()
                self.left = Into_Account_Main_Frame(self, order_id_select, width=self.w, height=self.h, fg_color="#FFFFFF")
                self.left.grid(row=0,column=0)