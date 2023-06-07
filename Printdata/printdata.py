import customtkinter as ctk

class Printdata_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.left = ctk.CTkFrame(self,width=1400,height=750,fg_color="yellow")
        
        self.left.grid(row=0,column=0,padx=10,pady=10)