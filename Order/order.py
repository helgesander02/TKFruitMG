import customtkinter as ctk
import tkcalendar as tkc
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

class top(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.c_id = ctk.CTkEntry(self,width=160,height=40,placeholder_text="輸入客戶代號",font=("Arial",24))
        self.cal = tkc.DateEntry(self,)
        self.c_id.place(x=40,y=30)
        self.cal.place(x=220,y=30)
        self.bot = bot(self,width=1800,height=630,fg_color="#EEEEEE")
        self.bot.place(x=0,y=120)

class bot(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.top_bar = bar(self,width=1800,height=40)
        self.top_bar.place(x=0,y=40)

class Order_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        top_part = top(self,width=1800,height=750)
        top_part.place(x=60,y=60)