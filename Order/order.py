import customtkinter as ctk

class bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        serial = ctk.CTkLabel(self)
        serial = ctk.CTkLabel(self)
        serial = ctk.CTkLabel(self)
        serial = ctk.CTkLabel(self)
        serial = ctk.CTkLabel(self)
        serial = ctk.CTkLabel(self)
        serial = ctk.CTkLabel(self)
        serial = ctk.CTkLabel(self)
        serial = ctk.CTkLabel(self)
class Order_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        top_part = ctk.CTkFrame(self,width=1800,height=100)
        top_part.place(x=60,y=20)
        bot_part = ctk.CTkFrame(self,width=1800,height=600)
        bot_part.place(x=60,y=140)
        