import customtkinter as ctk

from .customer import right_top_part_A
from .item import right_top_part_B

class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)

class Company_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def button_event_customer(event):
            self.right_top.grid_forget()
            self.right_top = right_top_part_A(self,width=kwargs["width"]-300,height=kwargs["height"]-90,fg_color="#EEEEEE")
            self.right_top.grid(row=0,column=1,padx=10,pady=10)
        
        def button_event_item(event):
            self.right_top.grid_forget()
            self.right_top = right_top_part_B(self,width=kwargs["width"]-300,height=kwargs["height"]-90,fg_color="#EEEEEE")
            self.right_top.grid(row=0,column=1,padx=10,pady=10)
               
        # left frame
        self.left = left_part(self, width=250,height=kwargs["height"]-90,fg_color="#EEEEEE")

        # right frame
        self.right_top = right_top_part_A(self,width=kwargs["width"]-300,height=kwargs["height"]-90,fg_color="#EEEEEE")

        # button
        self.botton_1 = ctk.CTkButton(self.left, width=200, height=40, 
                                      fg_color="white", 
                                      text="客戶管理", text_color="black",
                                      font=("microsoft yahei", 16, 'bold')
                                      )
        self.botton_2 = ctk.CTkButton(self.left, width=200, height=40, 
                                      fg_color="white", 
                                      text="品項管理", text_color="black",
                                      font=("microsoft yahei", 16, 'bold')
                                      )

        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        self.right_top.grid(row=0,column=1,padx=10,pady=10)

        self.botton_1.place(x=20,y=20)
        self.botton_2.place(x=20,y=80)
        self.botton_1.bind("<Button-1>", button_event_customer)
        self.botton_2.bind("<Button-1>", button_event_item)
        
        

    