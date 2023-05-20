from typing import Optional, Tuple, Union
import customtkinter as ctk
from PIL import ImageTk,Image

class Top_level_add_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("200x300")

        label = ctk.CTkLabel(self, text="add customer", font=("Arial", 25))
        label.pack(padx=20,pady=20)

class Top_level_edit_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("200x300")

        label = ctk.CTkLabel(self, text="edit customer", font=("Arial", 25))
        label.pack(padx=20,pady=20)

class right_top_part_A(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        img = Image.open("C:\\Users\\User\\Desktop\\TKFruitMG\\search-icon-free-vector.jpg")
        btn_image = ctk.CTkImage(img,size=(48,48))
        
        self.toplevel_window = None
        text_1 = ctk.CTkTextbox(self,width=150,height=50,font=("Arial",24))
        button_for_search = ctk.CTkButton(self,width=50,image=btn_image,text="",border_spacing=0,corner_radius=0)
        button_1 = ctk.CTkButton(self,width=100,height=40,text="新增客戶",command=self.open_toplevel_add_customer)
        button_2 = ctk.CTkButton(self,width=100,height=40,text="編輯客戶",command=self.open_toplevel_edit_customer)
        
        text_1.place(x=100,y=75)
        button_for_search.place(x=255,y=75)
        button_1.place(x=1550,y=45)
        button_2.place(x=1550,y=95)
    def open_toplevel_add_customer(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_add_customer(self)
        else:
            self.toplevel_window.focus()

    def open_toplevel_edit_customer(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_edit_customer(self)
        else:
            self.toplevel_window.focus()
class right_top_part_B(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        img = Image.open("C:\\Users\\User\\Desktop\\TKFruitMG\\search-icon-free-vector.jpg")
        btn_image = ctk.CTkImage(img,size=(48,48))
        text_1 = ctk.CTkTextbox(self,width=150,height=50,font=("Arial",24))
        button_for_search = ctk.CTkButton(self,width=50,image=btn_image,text="",border_spacing=0,corner_radius=0)
        button_1 = ctk.CTkButton(self,width=100,height=40,text="新增品項")
        button_2 = ctk.CTkButton(self,width=100,height=40,text="編輯品項")

        text_1.place(x=100,y=75)
        button_for_search.place(x=255,y=75)
        button_1.place(x=1550,y=45)
        button_2.place(x=1550,y=95)

class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)


class right_bot_part_A(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        bar_1 = ctk.CTkLabel(self, width=176, height=40,text="序號")
        bar_2 = ctk.CTkLabel(self, width=176, height=40,text="客戶編號")
        bar_3 = ctk.CTkLabel(self, width=176, height=40,text="客戶名稱")
        bar_4 = ctk.CTkLabel(self, width=176, height=40,text="手機")
        bar_5 = ctk.CTkLabel(self, width=176, height=40,text="住址")
        bar_6 = ctk.CTkLabel(self, width=800, height=40,text="備註")

        bar_1.place(x=0,y=0)
        bar_2.place(x=176,y=0)
        bar_3.place(x=352,y=0)
        bar_4.place(x=528,y=0)
        bar_5.place(x=704,y=0)
        bar_6.place(x=880,y=0)

class right_bot_part_B(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        bar_1 = ctk.CTkLabel(self, width=176, height=40,text="序號")
        bar_2 = ctk.CTkLabel(self, width=176, height=40,text="品項編號")
        bar_3 = ctk.CTkLabel(self, width=176, height=40,text="品項名稱")
        bar_1.place(x=0,y=0)
        bar_2.place(x=176,y=0)
        bar_3.place(x=352,y=0)

class Company_Main_Frame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def button_event_customer(event):
            self.right_bot.grid_forget()
            self.right_top.grid_forget()
            self.right_top = right_top_part_A(self,width=1680,height=200,fg_color="pink")
            self.right_bot = right_bot_part_A(self,width=1680,height=580,fg_color="pink")
            self.right_top.grid(row=0,column=1,padx=10,pady=10)
            self.right_bot.grid(row=1,column=1,padx=10,pady=10)
        
        def button_event_item(event):
            self.right_bot.grid_forget()
            self.right_top.grid_forget()
            self.right_top = right_top_part_B(self,width=1680,height=200,fg_color="pink")
            self.right_bot = right_bot_part_B(self,fg_color="pink",width=1680,height=580)
            self.right_top.grid(row=0,column=1,padx=10,pady=10)
            self.right_bot.grid(row=1,column=1,padx=10,pady=10)

        
        
        #left label
        self.left = left_part(self, width=200,height=800,fg_color="pink")
        self.right_top = right_top_part_A(self,width=1680,height=200,fg_color="pink")
        self.right_bot = right_bot_part_A(self,width=1680,height=580,fg_color="pink")

        #button
        self.botton_1 = ctk.CTkButton(self.left, width=160, 
                                      height=40, fg_color="white", 
                                      text="客戶管理", text_color="black"
                                      )
        self.botton_2 = ctk.CTkButton(self.left, width=160, 
                                      height=40, fg_color="white", 
                                      text="品項管理", text_color="black"
                                      )

        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        self.right_top.grid(row=0,column=1,padx=10,pady=10)
        self.right_bot.grid(row=1,column=1,padx=10,pady=10)

        self.botton_1.place(x=20,y=20)
        self.botton_2.place(x=20,y=80)
        self.botton_1.bind("<Button-1>", button_event_customer)
        self.botton_2.bind("<Button-1>", button_event_item)
        
        

    