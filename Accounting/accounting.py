import customtkinter

class Accounting_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.btn_accounting = customtkinter.CTkButton(self ,text="Accounting" ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_accounting.place(x=540, y=160)