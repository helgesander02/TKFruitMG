import customtkinter as ctk

class Company_Main_Frame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def button_event_customer(event):
            self.label_right_2.grid_forget()
            self.label_right_2 = self.label_right_2
            self.label_right_2.grid(row=1,column=1,padx=10,pady=10)
        
        def button_event_item(event):
            self.label_right_2.grid_forget()
            self.label_right_bottom = self.label_right_
            self.label_right_2.grid(row=1,column=1,padx=10,pady=10)
        
        self.label = ctk.CTkLabel(self, width=200,height=800,fg_color="pink",text="")
        self.label_right_1 = ctk.CTkLabel(self, width=1680,height=200,fg_color="pink",text="right_top")
        self.label_right_2 = ctk.CTkLabel(self, width=1680,height=580,fg_color="pink",text="customer")
        self.bar_1 = ctk.CTkLabel(self.label_right_2, width=176, height=40,text="序號")
        self.bar_2 = ctk.CTkLabel(self.label_right_2, width=176, height=40,text="客戶編號")
        self.bar_3 = ctk.CTkLabel(self.label_right_2, width=176, height=40,text="客戶名稱")
        self.bar_4 = ctk.CTkLabel(self.label_right_2, width=176, height=40,text="手機")
        self.bar_5 = ctk.CTkLabel(self.label_right_2, width=176, height=40,text="住址")
        self.bar_6 = ctk.CTkLabel(self.label_right_2, width=800, height=40,text="備註")
        #self.label_right_3 = ctk.CTkLabel(self, width=1680,height=580,fg_color="green",text="item")

        self.botton_1 = ctk.CTkButton(self.label, width=160, 
                                      height=40, fg_color="white", 
                                      text="客戶管理", text_color="black")
        self.botton_2 = ctk.CTkButton(self.label, width=160, 
                                      height=40, fg_color="white", 
                                      text="品項管理", text_color="black")

        self.label.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        self.label_right_1.grid(row=0,column=1,padx=10,pady=10)
        self.label_right_2.grid(row=1,column=1,padx=10,pady=10)
        self.botton_1.place(x=20,y=20)
        self.botton_2.place(x=20,y=80)
        self.botton_1.bind("<Button-1>", button_event_customer)
        self.botton_2.bind("<Button-1>", button_event_item)
        self.bar_1.place(x=0,y=0)
        self.bar_2.place(x=176,y=0)
        self.bar_3.place(x=352,y=0)
        self.bar_4.place(x=528,y=0)
        self.bar_5.place(x=704,y=0)
        self.bar_6.place(x=880,y=0)
        

    