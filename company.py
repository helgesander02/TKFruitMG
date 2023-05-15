import customtkinter

class Company_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.btn_company = customtkinter.CTkButton(self ,text="Company" ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_company.place(x=300, y=160)

        