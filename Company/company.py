import customtkinter as ctk
from .customer import right_top_part_A
from .item import right_top_part_B

class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class Company_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  
        self.w = kwargs["width"]
        self.h = kwargs["height"]  

        # left frame
        self.left = left_part(self, width=250, height=kwargs["height"]-90, fg_color="#EEEEEE")
        self.left.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

        # right frame
        self.right_top = right_top_part_A(self, width=kwargs["width"]-300, height=kwargs["height"]-90, fg_color="#EEEEEE")
        self.right_top.grid(row=0, column=1, padx=10, pady=10)

        # button
        self.botton_1 = ctk.CTkButton(self.left, width=200, height=40, 
                                      fg_color="white", 
                                      text="客戶管理", 
                                      text_color="black",
                                      font=("microsoft yahei", 16, 'bold'))
        self.botton_1.place(x=20, y=20)
        self.botton_1.bind("<Button-1>", self.button_event_customer)
        
        self.botton_2 = ctk.CTkButton(self.left, width=200, height=40, 
                                      fg_color="white", 
                                      text="品項管理", 
                                      text_color="black",
                                      font=("microsoft yahei", 16, 'bold'))       
        self.botton_2.place(x=20, y=80)
        self.botton_2.bind("<Button-1>", self.button_event_item)

    def button_event_customer(self, event):
        self.right_top.destroy()
        self.right_top = right_top_part_A(self, width=self.w-300, height=self.h-90, fg_color="#EEEEEE")
        self.right_top.grid(row=0, column=1, padx=10, pady=10)

        
    def button_event_item(self, event):
        self.right_top.destroy()
        self.right_top = right_top_part_B(self, width=self.w-300, height=self.h-90, fg_color="#EEEEEE")
        self.right_top.grid(row=0, column=1, padx=10, pady=10)
        
        

    