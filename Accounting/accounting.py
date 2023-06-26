import customtkinter as ctk
import tkcalendar as tkc
import psycopg2

from .into_account import Into_Account_Main_Frame

class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def search(event):            
            customer_id = self.customer_id_entry.get()
            # con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            cur = con.cursor()
            cur.execute(f"SELECT name, phone, address, remark \
                            FROM customer \
                            WHERE c_id='{'abc' if customer_id == '' else customer_id}'")
            result = cur.fetchone()
            try:
                self.left.right_top.name_entry.configure(text=f"{str(result[0]).rstrip()}")
                self.left.right_top.phone_entry.configure(text=f"{str(result[1]).rstrip()}")
                self.left.right_top.address_entry.configure(text=f"{str(result[2]).rstrip()}")
                self.left.right_top.remark_entry.configure(text=f"{str(result[3]).rstrip()}")
            except Exception as e:
                pass
            cur.close()
            con.close()
            # self.customer_id_entry.delete(0, 'end')
            self.right_bot.InsertData(customer_id, 
                                        self.sell_date1_entry.get_date(), 
                                        self.sell_date2_entry.get_date(),
                                        self.finish_chk.get())
            
            


        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.customer_id_entry = ctk.CTkEntry(self,width=210, height=50,
                                                    fg_color="#EEEEEE",
                                                    placeholder_text="客戶編號" 
                                                    )
        self.customer_id_entry.bind("<Return>", search)

        self.sell_date1_entry = tkc.DateEntry(self, selectmode='day',
                                                    font=("microsoft yahei", 20),year=2000,month=1,day=1,date_pattern="yyyy-mm-dd")
        self.sell_date2_entry = tkc.DateEntry(self, selectmode='day',
                                                    font=("microsoft yahei", 20),date_pattern="yyyy-mm-dd")

        self.finish_chk = ctk.CTkCheckBox(self,width=40,height=40, text="是否隱藏收帳完成的", 
                                                    font=("microsoft yahei", 16, 'bold'),
                                                    )

        self.confirm_btn = ctk.CTkButton(self,width=200,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="確認查詢",
                                                    font=("microsoft yahei", 20, 'bold'),
                                                    )

        self.reset_btn = ctk.CTkButton(self,width=200,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="重設查詢",
                                                    font=("microsoft yahei", 20, 'bold'),
                                                    )
        # self.confirm_btn.bind("<Button-1>", search)
        self.right_top = right_top_part(self,width=self.w-300,height=200,fg_color="#EEEEEE")
        self.right_bot = right_bot_part(self,width=self.w-300,height=self.h-320,fg_color="#EEEEEE")
        
        self.customer_id_entry.place(x=25,y=50)
        self.sell_date1_entry.place(x=25,y=300)
        self.sell_date2_entry.place(x=25,y=350)
        self.finish_chk.place(x=25,y=120)
        self.finish_chk.select()
        self.confirm_btn.place(x=25,y=self.h-220)
        self.reset_btn.place(x=25,y=self.h-160)
             
        self.right_top.place(x=270,y=5)
        self.right_bot.place(x=270,y=220)

class right_top_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.customer_name = ctk.CTkLabel(self,text="客戶名稱：", font=("microsoft yahei", 20, 'bold'))
        self.address = ctk.CTkLabel(self,text="地址：", font=("microsoft yahei", 20, 'bold'))
        self.phone = ctk.CTkLabel(self,text="　　手機：", font=("microsoft yahei", 20, 'bold'))
        self.remark = ctk.CTkLabel(self,text="備註：", font=("microsoft yahei", 20, 'bold'))

        self.name_entry = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20))
        self.phone_entry = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20))
        self.address_entry = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20))
        self.remark_entry = ctk.CTkLabel(self, text="", font=("microsoft yahei", 20))

        self.customer_name.place(x=60,y=50)
        self.name_entry.place(x=170,y=50)

        self.phone.place(x=60,y=110)
        self.phone_entry.place(x=170,y=110)

        self.address.place(x=450,y=50)
        self.address_entry.place(x=530,y=50)

        self.remark.place(x=450,y=110)
        self.remark_entry.place(x=530,y=110)

class once_enter(ctk.CTkToplevel):
    def __init__(self, master,overage, c_id,**kwargs):
        super().__init__(master, **kwargs)
        def insert_receipt():
            con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            with con:
                cur = con.cursor()
                money = int(self.entry3.get())
                for i in range(len(overage)):
                    temp = 0
                    if money == 0:break
                    if int(overage[i][1]) <= money:
                        temp = int(overage[i][1])
                        money -= int(overage[i][1])
                    elif int(overage[i][1]) > money:
                        temp = money
                        money = 0
                    cur.execute(f"INSERT INTO accounting VALUES('{overage[i][0]}','{self.select_ac_id(c_id_=c_id)}')")
                    cur.execute(f"INSERT INTO receipt VALUES('{self.select_ac_id(c_id_=c_id)}','{self.entry1.get()}','{self.entry2.get()}','{temp}','0','')")
                    con.commit()
            self.destroy()
        self.geometry("300x200")
        self.lbl1 = ctk.CTkLabel(self,text="收款日期",width=100,height=40,font=("microsoft yahei", 14, 'bold'))
        self.lbl2 = ctk.CTkLabel(self,text="收款方式",width=100,height=40,font=("microsoft yahei", 14, 'bold'))
        self.lbl3 = ctk.CTkLabel(self,text="收款金額",width=100,height=40,font=("microsoft yahei", 14, 'bold'))
        self.entry1 = ctk.CTkEntry(self,placeholder_text="收款日期",width=150,height=40)
        self.entry2 = ctk.CTkEntry(self,placeholder_text="收款方式",width=150,height=40)
        self.entry3 = ctk.CTkEntry(self,placeholder_text="收款金額",width=150,height=40)
        self.confirm_btn = ctk.CTkButton(self,text="確認入賬",width=100,height=40,command=insert_receipt)
        self.confirm_btn.grid(row=3,column=0,columnspan=2)
        self.lbl1.grid(row=0,column=0,padx=5,pady=5)
        self.lbl2.grid(row=1,column=0,padx=5,pady=5)
        self.lbl3.grid(row=2,column=0,padx=5,pady=5)
        self.entry1.grid(row=0,column=1,padx=5,pady=5)
        self.entry2.grid(row=1,column=1,padx=5,pady=5)
        self.entry3.grid(row=2,column=1,padx=5,pady=5)
        # print(c_id)
        # print(data)
        # print(overage)
    def select_ac_id(self,c_id_):
        ac = f"ac{c_id_}"
        con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
        # con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        cur = con.cursor()
        cur.execute(f"select ac_id from accounting order by ac_id")
        ac_all = cur.fetchall()    
        cur.close()
        con.close()
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
        self.top = top_bar(self, width=self.w, height=40)
        self.toplevel = None
        self.mid = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-80, fg_color="#EEEEEE")
        self.select_order = []
        self.bot = ctk.CTkFrame(self, width=self.w, height=40)
        self.j_btn = ctk.CTkButton(self.bot, width=150, height=30, text="入賬" ,font=("microsoft yahei", 14, 'bold'))
        self.once_btn = ctk.CTkButton(self.bot, width=150, height=30, text="一次輸入" ,font=("microsoft yahei", 14, 'bold'),command=self.open_once_enter)
        self.j_text = ctk.CTkLabel(self.bot, width=50, height=40, text="" ,font=("microsoft yahei", 20, 'bold'), text_color="#FF0000")
        self.top.place(x=0,y=0)
        self.mid.place(x=0,y=40)
        self.bot.place(x=0,y=self.h-40)
        self.once_btn.place(x=self.w-400,y=5)
        self.j_btn.place(x=self.w-200,y=5)
        
    def open_once_enter(self):
        overage = self.SelectOrder_test()
        w = self.winfo_parent()
        m = self.master.nametowidget(w)
        c_id = m.customer_id_entry.get()
        if self.toplevel is None or not self.toplevel.winfo_exists():
            self.toplevel = once_enter(self,overage,c_id)
            self.toplevel.attributes('-topmost','true')
            self.toplevel.focus()
        else:
            self.toplevel.focus()
        
    def InsertData(self, c_id, date1, date2, chk):
        # con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
        cur = con.cursor()
        if c_id == "":
            cur.execute(f"SELECT goods.o_id, goods.remark, SUM(goods.sub_total) \
                                FROM order_form JOIN goods \
                                ON order_form.o_id = goods.o_id \
                                WHERE goods.date BETWEEN SYMMETRIC '{date1}' AND '{date2}' \
                                GROUP BY goods.o_id, goods.remark")
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
            cur.close()
            con.close()
        else:
            cur.execute(f"SELECT goods.o_id, goods.remark, SUM(goods.sub_total) \
                                FROM order_form JOIN goods \
                                ON order_form.o_id = goods.o_id \
                                WHERE order_form.c_id = '{c_id}' AND (goods.date BETWEEN SYMMETRIC '{date1}' AND '{date2}') \
                                GROUP BY goods.o_id, goods.remark")
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
            cur.close()
            con.close()

        for i in range(len(result1)):
            al = 0
            overage = result1[i][2]
            for j in range(len(result2)):
                if result2[j][0] == result1[i][0]:
                    al = result2[j][1]
                    overage -= result2[j][1]

            if overage == 0 and chk == 1: continue
            it = item(self.mid, width=self.w-20, fg_color="#EEEEEE")
            it.dat.insert(0, f"{result1[i][0]}")
            it.remark.insert(0, f"{result1[i][1]}")
            it.sbtotal.insert(0, f"{result1[i][2]}")      
            it.al_total.insert(0, f"{al}")
            it.overage.insert(0, f"{overage}")
           
            self.select_order.append(it)              
            it.pack()

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
                select_chkbox.append([str(so.dat.get().rstrip()),str(so.overage.get().rstrip())])

        return select_chkbox

class top_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/6
        self.bar_1 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="選擇",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="銷貨單編號",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="銷貨總計",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="已收金額",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="餘額",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_6 = ctk.CTkLabel(self, width=w, height=40, 
                                    text="銷貨單備註",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)
        self.bar_6.grid(row=0,column=5)

class item(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/6
        self.chk_box = ctk.CTkCheckBox(self,width=w,height=40, text="")
        self.dat = ctk.CTkEntry(self,width=w,height=40)
        self.sbtotal = ctk.CTkEntry(self,width=w,height=40)
        self.al_total = ctk.CTkEntry(self,width=w,height=40)
        self.overage = ctk.CTkEntry(self,width=w,height=40)
        self.remark = ctk.CTkEntry(self,width=w,height=40)
        
        self.chk_box.grid(row=0,column=0)
        self.dat.grid(row=0,column=1)
        self.sbtotal.grid(row=0,column=2)
        self.al_total.grid(row=0,column=3)
        self.overage.grid(row=0,column=4)
        self.remark.grid(row=0,column=5)

class Accounting_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def open_into_account(event):
            order_id_select = self.left.right_bot.SelectOrder()
            menber_id = self.left.customer_id_entry.get()
            if order_id_select == []: 
                self.left
                self.left.right_bot.j_text.configure(text="請選擇訂單")
            else:
                self.left.grid_forget()
                self.left = Into_Account_Main_Frame(self, order_id_select, menber_id, width=kwargs["width"], height=kwargs["height"], fg_color="#FFFFFF")
                self.left.grid(row=0,column=0,padx=10,pady=10)

        def reset(event):
            self.left.right_bot.place_forget()
            self.left.right_bot = right_bot_part(self.left,width=self.left.w-300,height=self.left.h-320,fg_color="#EEEEEE")
            self.left.right_bot.place(x=270,y=220)

            self.left.right_top.place_forget()
            self.left.right_top = right_top_part(self.left,width=self.left.w-300,height=200,fg_color="#EEEEEE")
            self.left.right_top.place(x=270,y=5)

            self.left.right_bot.j_btn.bind("<Button-1>",open_into_account)
            self.left.reset_btn.bind("<Button-1>", reset)

        def test(event):
            c_id = self.left.customer_id_entry.get()
            # print(type(c_id))
            con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            cur = con.cursor()
            cur.execute(f"SELECT name, phone, address, remark \
                            FROM customer \
                            WHERE c_id='{'abc' if c_id == '' else c_id}'")
            result = cur.fetchone()
            try:
                self.left.right_top.name_entry.configure(text=f"{str(result[0]).rstrip()}")
                self.left.right_top.phone_entry.configure(text=f"{str(result[1]).rstrip()}")
                self.left.right_top.address_entry.configure(text=f"{str(result[2]).rstrip()}")
                self.left.right_top.remark_entry.configure(text=f"{str(result[3]).rstrip()}")
            except Exception as e:
                pass
            cur.close()
            con.close()
            # self.left.customer_id_entry.delete(0, 'end')
            self.left.right_bot.InsertData(c_id, 
                                        self.left.sell_date1_entry.get_date(), 
                                        self.left.sell_date2_entry.get_date(),
                                        self.left.finish_chk.get())
        
        self.left = left_part(self, width=kwargs["width"], height=kwargs["height"], fg_color="#FFFFFF")
        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        self.left.right_bot.j_btn.bind("<Button-1>",open_into_account)
        self.left.reset_btn.bind("<Button-1>", reset)
        # self.left.confirm_btn.bind("<Button-1>",reset)
        # self.left.confirm_btn.bind("<Button-1>",test)
        