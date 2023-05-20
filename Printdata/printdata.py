import customtkinter

class Printdata_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.btn_print = customtkinter.CTkButton(self ,text="Print" ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_print.place(x=540, y=480)
