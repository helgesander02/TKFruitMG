import customtkinter as ctk
import os
from PIL import ImageTk,Image
import psycopg2

class Top_level_add_item(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.geometry("200x200")
        def confirm():
            con = psycopg2.connect(database='postgres', 
                                   user='postgres',
                                    password='admin')
            with con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO item(item_id, item_name) VALUES('{item_id_entry.get()}','{item_name_entry.get()}')")
            self.destroy()
        def cancel():
            self.destroy()
        item_id = ctk.CTkLabel(self,text="品項編號：")
        item_name = ctk.CTkLabel(self,text="品項名稱：")
        item_id_entry = ctk.CTkEntry(self)
        item_name_entry = ctk.CTkEntry(self)
        confirm = ctk.CTkButton(self,text="確認",command=confirm)
        cancel = ctk.CTkButton(self,text="取消",command=cancel)

        item_id.grid(row=0, column=0,padx=10,pady=10)
        item_name.grid(row=1, column=0,padx=10,pady=10)
        item_id_entry.grid(row=0, column=1,padx=10,pady=10)
        item_name_entry.grid(row=1, column=1,padx=10,pady=10)
        cancel.grid(row=2,column=1,padx=10,pady=10)
        confirm.grid(row=2,column=0,padx=10,pady=10)
class Top_level_edit_item(ctk.CTkToplevel):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        def confirm():
            con = psycopg2.connect(database='postgres', 
                                   user='postgres',
                                    password='admin')
            with con:
                cur = con.cursor()
                cur.execute(f"UPDATE item SET item_name = '{item_name_entry.get()}' \
                            WHERE item_id = '{item_id_entry.get()}'")
            self.destroy()
        def cancel():
            self.destroy()
        item_id = ctk.CTkLabel(self,text="品項編號：")
        item_name = ctk.CTkLabel(self,text="品項名稱：")
        item_id_entry = ctk.CTkEntry(self)
        item_name_entry = ctk.CTkEntry(self)
        confirm = ctk.CTkButton(self,text="確認",command=confirm)
        cancel = ctk.CTkButton(self,text="取消",command=cancel)

        item_id.grid(row=0, column=0,padx=10,pady=10)
        item_name.grid(row=1, column=0,padx=10,pady=10)
        item_id_entry.grid(row=0, column=1,padx=10,pady=10)
        item_name_entry.grid(row=1, column=1,padx=10,pady=10)
        cancel.grid(row=2,column=1,padx=10,pady=10)
        confirm.grid(row=2,column=0,padx=10,pady=10)
class Top_level_add_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def click():
            con = psycopg2.connect(database='postgres',
                                   user='postgres',
                                    password='admin')
            with con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO customer(c_id,name,phone,address,remark) \
                            VALUES('{id_entry.get()}', \
                            '{name_entry.get()}', \
                            '{phone_entry.get()}', \
                            '{address_entry.get()}' \
                            ,'{remark_entry.get(1.0,'end-1c')}') \
                            ")
            self.destroy()

        def cancel():
            self.destroy()

        self.geometry("250x325")
        confirm = ctk.CTkButton(self,width=80,height=15,text="確認",command=click)
        cancel = ctk.CTkButton(self,width=80,height=15,text="取消",command=cancel)
        customer_id = ctk.CTkLabel(self, text="客戶編號：")
        name = ctk.CTkLabel(self, text="　　名稱：")
        phone = ctk.CTkLabel(self, text="　　手機：")
        address = ctk.CTkLabel(self, text="　　住址：")
        remark = ctk.CTkLabel(self, text="　　備註：")

        id_entry = ctk.CTkEntry(self,border_width=0)
        name_entry = ctk.CTkEntry(self,border_width=0)
        phone_entry = ctk.CTkEntry(self,border_width=0)
        address_entry = ctk.CTkEntry(self,border_width=0)
        remark_entry = ctk.CTkTextbox(self,width=140,height=80)

        customer_id.place(x=20,y=20)
        name.place(x=20,y=60)
        phone.place(x=20,y=100)
        address.place(x=20,y=140)
        remark.place(x=20,y=180)

        confirm.place(x=25,y=280)
        cancel.place(x=145,y=280)

        id_entry.place(x=85,y=20)
        name_entry.place(x=85,y=60)
        phone_entry.place(x=85,y=100)
        address_entry.place(x=85,y=140)
        remark_entry.place(x=85,y=180)

class Top_level_edit_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def click():
            con = psycopg2.connect(database='postgres',
                                   user='postgres',
                                    password='admin')
            with con:
                cur = con.cursor()
                cur.execute(f"UPDATE customer SET name = '{name_entry.get()}', \
                            phone = '{phone_entry.get()}', \
                            address = '{address_entry.get()}', \
                            remark = '{remark_entry.get(1.0,'end-1c')}' \
                            WHERE c_id = '{id_entry.get()}'")
            self.destroy()

        def cancel():
            self.destroy()

        self.geometry("250x325")
        confirm = ctk.CTkButton(self,width=80,height=15,text="確認",command=click)
        cancel = ctk.CTkButton(self,width=80,height=15,text="取消",command=cancel)
        customer_id = ctk.CTkLabel(self, text="客戶編號：")
        name = ctk.CTkLabel(self, text="　　名稱：")
        phone = ctk.CTkLabel(self, text="　　手機：")
        address = ctk.CTkLabel(self, text="　　住址：")
        remark = ctk.CTkLabel(self, text="　　備註：")

        id_entry = ctk.CTkEntry(self,border_width=0)
        name_entry = ctk.CTkEntry(self,border_width=0)
        phone_entry = ctk.CTkEntry(self,border_width=0)
        address_entry = ctk.CTkEntry(self,border_width=0)
        remark_entry = ctk.CTkTextbox(self,width=140,height=80)

        customer_id.place(x=20,y=20)
        name.place(x=20,y=60)
        phone.place(x=20,y=100)
        address.place(x=20,y=140)
        remark.place(x=20,y=180)

        confirm.place(x=25,y=280)
        cancel.place(x=145,y=280)

        id_entry.place(x=85,y=20)
        name_entry.place(x=85,y=60)
        phone_entry.place(x=85,y=100)
        address_entry.place(x=85,y=140)
        remark_entry.place(x=85,y=180)

class right_top_part_A(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):

        def search():
            con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')
            with con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM customer WHERE id = '{text_1.get(1.0, 'end-1c')}'")
                result = cur.fetchall()
        super().__init__(master, **kwargs)
        
        img = Image.open(f"{os.getcwd()}\\img\\search.png")
        btn_image = ctk.CTkImage(img,size=(25,25))
        
        self.toplevel_window = None
        text_1 = ctk.CTkTextbox(self,width=250,height=50,font=("Arial",24))
        button_for_search = ctk.CTkButton(self,width=50,height=50,image=btn_image,text="",border_spacing=0,corner_radius=0,command=search)
        button_1 = ctk.CTkButton(self,width=200,height=50,text="新增客戶",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_add_customer)
        button_2 = ctk.CTkButton(self,width=200,height=50,text="編輯客戶",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_edit_customer)
        
        text_1.place(x=100,y=75)
        button_for_search.place(x=350,y=75)
        button_1.place(x=900,y=40)
        button_2.place(x=900,y=110)
        
    
    def open_toplevel_add_customer(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_add_customer(self)
            self.toplevel_window.attributes('-topmost','true')
        else:
            self.toplevel_window.focus()

    def open_toplevel_edit_customer(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_edit_customer(self)
            self.toplevel_window.attributes('-topmost','true')
        else:
            self.toplevel_window.focus()
    
class right_top_part_B(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        img = Image.open(f"{os.getcwd()}\\img\\search.png")
        btn_image = ctk.CTkImage(img,size=(25,25))

        text_1 = ctk.CTkTextbox(self,width=250,height=50,font=("Arial",24))
        button_for_search = ctk.CTkButton(self,width=50,height=50,image=btn_image,text="",border_spacing=0,corner_radius=0)
        button_1 = ctk.CTkButton(self,width=200,height=50,text="新增品項",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_add_item)
        button_2 = ctk.CTkButton(self,width=200,height=50,text="編輯品項",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_edit_item)
        self.toplevel_window = None
        text_1.place(x=100,y=75)
        button_for_search.place(x=350,y=75)
        button_1.place(x=900,y=40)
        button_2.place(x=900,y=110)

    def open_toplevel_add_item(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_add_item(self)
            self.toplevel_window.attributes('-topmost','true')
        else:
            self.toplevel_window.focus()
    
    def open_toplevel_edit_item(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_edit_item(self)
            self.toplevel_window.attributes('-topmost','true')
        else:
            self.toplevel_window.focus()
class left_part(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)


class right_bot_part_A(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # bar_1 = ctk.CTkLabel(self, width=176, height=40,text="序號")
        bar_2 = ctk.CTkLabel(self, width=176, height=40,text="客戶編號")
        bar_3 = ctk.CTkLabel(self, width=176, height=40,text="客戶名稱")
        bar_4 = ctk.CTkLabel(self, width=176, height=40,text="手機")
        bar_5 = ctk.CTkLabel(self, width=176, height=40,text="住址")
        bar_6 = ctk.CTkLabel(self, width=176, height=40,text="備註")
        
        # bar_1.place(x=0,y=0)
        bar_2.place(x=0,y=0)
        bar_3.place(x=176,y=0)
        bar_4.place(x=352,y=0)
        bar_5.place(x=528,y=0)
        bar_6.place(x=704,y=0)
        # 0 176 352 528 704 880
    def add(result):
        print(result)
class right_bot_part_C(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def search():
            con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')
            row = 1
            with con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM customer WHERE c_id = '{bar_7.get()}'")
                result = cur.fetchall()
            for i in result:
                x=0
                for j in i:
                    temp = ctk.CTkEntry(self)
                    temp.insert(0, str(j).rstrip())
                    temp.grid(row=row,column=x)
                    x+=1
                row += 1
            # print(result)
        bar_1 = ctk.CTkLabel(self, width=176, height=40,text="序號",fg_color='yellow')
        bar_2 = ctk.CTkLabel(self, width=176, height=40,text="客戶編號",fg_color='blue')
        bar_3 = ctk.CTkLabel(self, width=176, height=40,text="客戶名稱",fg_color='yellow')
        bar_4 = ctk.CTkLabel(self, width=176, height=40,text="手機",fg_color='blue')
        bar_5 = ctk.CTkLabel(self, width=176, height=40,text="住址",fg_color='green')
        bar_6 = ctk.CTkLabel(self, width=300, height=40,text="備註",fg_color='blue')
        bar_7 = ctk.CTkEntry(self,width=100,height=40)
        bar_8 = ctk.CTkButton(self,width=76,height=40,text="搜尋",command=search)
        bar_1.grid(row=0,column=0)
        bar_2.grid(row=0,column=1)
        bar_3.grid(row=0,column=2)
        bar_4.grid(row=0,column=3)
        bar_5.grid(row=0,column=4)
        bar_6.grid(row=0,column=5)
        bar_7.grid(row=0,column=6)
        bar_8.grid(row=0,column=7)

class right_bot_part_B(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def search():
            con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')
            row = 1
            with con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM item WHERE item_id = '{bar_4.get()}'")
                result = cur.fetchall()
            for i in result:
                x=0
                for j in i:
                    temp = ctk.CTkEntry(self)
                    temp.insert(0, str(j).rstrip())
                    temp.grid(row=row,column=x)
                    x+=1
                row += 1
        bar_1 = ctk.CTkLabel(self, width=176, height=40,text="序號")
        bar_2 = ctk.CTkLabel(self, width=176, height=40,text="品項編號")
        bar_3 = ctk.CTkLabel(self, width=176, height=40,text="品項名稱")
        bar_4 = ctk.CTkEntry(self,width=100,height=40)
        bar_5 = ctk.CTkButton(self,width=76,height=40,text="搜尋",command=search)
        bar_1.grid(row=0,column=0)
        bar_2.grid(row=0,column=1)
        bar_3.grid(row=0,column=2)
        bar_4.grid(row=0,column=3)
        bar_5.grid(row=0,column=4)
class Company_Main_Frame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def button_event_customer(event):
            self.right_bot.grid_forget()
            self.right_top.grid_forget()
            self.right_top = right_top_part_A(self,width=1400,height=200,fg_color="#EEEEEE")
            self.right_bot = right_bot_part_C(self,width=1380,height=500,fg_color="#EEEEEE")
            self.right_top.grid(row=0,column=1,padx=10,pady=10)
            self.right_bot.grid(row=1,column=1,padx=10,pady=10)
        
        def button_event_item(event):
            self.right_bot.grid_forget()
            self.right_top.grid_forget()
            self.right_top = right_top_part_B(self,width=1400,height=200,fg_color="#EEEEEE")
            self.right_bot = right_bot_part_B(self,width=1380,height=500,fg_color="#EEEEEE")
            self.right_top.grid(row=0,column=1,padx=10,pady=10)
            self.right_bot.grid(row=1,column=1,padx=10,pady=10)

        
        
        #left label
        self.left = left_part(self, width=250,height=750,fg_color="#EEEEEE")
        self.right_top = right_top_part_A(self,width=1400,height=200,fg_color="#EEEEEE")
        self.right_bot = right_bot_part_C(self,width=1380,height=500,fg_color="#EEEEEE")

        #button
        self.botton_1 = ctk.CTkButton(self.left, width=200, 
                                      height=40, fg_color="white", 
                                      text="客戶管理", text_color="black",
                                      font=("microsoft yahei", 16, 'bold')
                                      )
        self.botton_2 = ctk.CTkButton(self.left, width=200, 
                                      height=40, fg_color="white", 
                                      text="品項管理", text_color="black",
                                      font=("microsoft yahei", 16, 'bold')
                                      )

        self.left.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
        self.right_top.grid(row=0,column=1,padx=10,pady=10)
        self.right_bot.grid(row=1,column=1,padx=10,pady=10)

        self.botton_1.place(x=20,y=20)
        self.botton_2.place(x=20,y=80)
        self.botton_1.bind("<Button-1>", button_event_customer)
        self.botton_2.bind("<Button-1>", button_event_item)
        
        

    