import customtkinter as ctk

class Into_Account_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        test = ctk.CTkLabel(self,text="測試測試",fg_color="yellow")
        test.grid(row=0,column=0)