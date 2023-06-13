import customtkinter as ctk
import psycopg2

class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.customer_id = ctk.CTkLabel(self, text="　　客戶：", font=("microsoft yahei", 16, 'bold'))

        self.order_id = ctk.CTkLabel(self, text="訂單編號：", font=("microsoft yahei", 16, 'bold'))

        self.information_btn = ctk.CTkButton(self,width=320,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="查看訂單細節",
                                                    font=("microsoft yahei", 16, 'bold'),
                                                    )

        self.location = ctk.CTkLabel(self, text="現在位置是第", font=("microsoft yahei", 16, 'bold'))

        self.forwark_btn = ctk.CTkButton(self,width=155,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="下一筆",
                                                    font=("microsoft yahei", 16, 'bold')
                                                    )
        
        self.backward_btn = ctk.CTkButton(self,width=155,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="上一筆",
                                                    font=("microsoft yahei", 16, 'bold')
                                                    )


        self.right_top = right_top_part(self,width=self.w-450,height=330,fg_color="#EEEEEE")
        self.right_bot = right_bot_part(self,width=self.w-450,height=self.h-450,fg_color="#EEEEEE")
        
        self.customer_id.place(x=25,y=25)
        self.order_id.place(x=25,y=80)
        self.information_btn.place(x=25,y=150)
        self.location.place(x=25,y=self.h-230)
        self.forwark_btn.place(x=25,y=self.h-160)
        self.backward_btn.place(x=200,y=self.h-160)
             
        self.right_top.place(x=400,y=0)
        self.right_bot.place(x=400,y=340)

class right_top_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.bar = top_bar(self,width=self.w,height=40,fg_color="#EEEEEE")

        self.bar.place(x=0,y=0)

class top_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/6

        self.bar_1 = ctk.CTkLabel(self,text="序號",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self,text="收款日期",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self,text="收款方式",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self,text="折讓",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self,text="收款金額",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_6 = ctk.CTkLabel(self,text="收款備註",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)
        self.bar_6.grid(row=0,column=5)

class right_bot_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]
        self.bar = bot_bar(self,width=self.w,height=40,fg_color="#EEEEEE")

        self.bar.place(x=0,y=0)

class bot_bar(ctk.CTkFrame):
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

        self.bar_3 = ctk.CTkLabel(self,text="折讓",width=w, height=40,
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self,text="收款金額",width=w, height=40,
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

class Into_Account_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.left = left_part(self, width=kwargs["width"], height=kwargs["height"], fg_color="#FFFFFF")
        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)