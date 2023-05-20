import customtkinter

class Order_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.btn_order = customtkinter.CTkButton(self ,text="Order" ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_order.place(x=300, y=480)