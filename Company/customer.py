import os
import customtkinter as ctk
from PIL import ImageTk,Image
import psycopg2

class Top_level_edit_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def click():
            conn = psycopg2.connect("postgres://su:7gpk4xkkNxGi7RqJOPKiNsQTLui0KrX5@dpg-choutv7dvk4goesube90-a.singapore-postgres.render.com/fruit")
            cur = conn.cursor()
            cur.execute(f"UPDATE Company SET NAME = '{name_entry.get()}', \
                            Phone = '{phone_entry.get()}', \
                            Adress = '{address_entry.get()}', \
                            Remark = '{remark_entry.get(1.0,'end-1c')}' \
                            WHERE ID = '{id_entry.get()}'")

            conn.commit()
            conn.close()
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

class Top_level_add_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def click():
            conn = psycopg2.connect("postgres://su:7gpk4xkkNxGi7RqJOPKiNsQTLui0KrX5@dpg-choutv7dvk4goesube90-a.singapore-postgres.render.com/fruit")
            cur = conn.cursor()
            cur.execute(f"INSERT INTO Company (ID, Name, Phone, Adress, Remark) \
                            VALUES('{id_entry.get()}', \
                            '{name_entry.get()}', \
                            '{phone_entry.get()}', \
                            '{address_entry.get()}' \
                            ,'{remark_entry.get(1.0,'end-1c')}') \
                            ")

            conn.commit()
            conn.close()
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

class right_bot_part_A(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        bar_1 = ctk.CTkLabel(self, width=160, height=40,text="序號",fg_color='yellow')
        bar_2 = ctk.CTkLabel(self, width=160, height=40,text="客戶編號",fg_color='blue')
        bar_3 = ctk.CTkLabel(self, width=160, height=40,text="客戶名稱",fg_color='yellow')
        bar_4 = ctk.CTkLabel(self, width=160, height=40,text="手機",fg_color='blue')
        bar_5 = ctk.CTkLabel(self, width=160, height=40,text="住址",fg_color='green')
        bar_6 = ctk.CTkLabel(self, width=160, height=40,text="備註",fg_color='blue')
        bar_1.grid(row=0,column=0)
        bar_2.grid(row=0,column=1)
        bar_3.grid(row=0,column=2)
        bar_4.grid(row=0,column=3)
        bar_5.grid(row=0,column=4)
        bar_6.grid(row=0,column=5)

    def InsertData(self, ID):
        conn = psycopg2.connect("postgres://su:7gpk4xkkNxGi7RqJOPKiNsQTLui0KrX5@dpg-choutv7dvk4goesube90-a.singapore-postgres.render.com/fruit")
        cur = conn.cursor()
        if ID == '':
            cur.execute(f"SELECT * FROM Company")
        else:
            cur.execute(f"SELECT * FROM Company WHERE ID = '{ID}'")
        result = cur.fetchall()
        row = 1
        for i in result:
                x=0
                for j in i:
                    temp = ctk.CTkEntry(self)
                    temp.insert(0, str(j).rstrip())
                    temp.grid(row=row,column=x)
                    x+=1
                row += 1

        conn.commit()
        conn.close()

class right_top_part_A(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)      
        img = Image.open(f"{os.getcwd()}\\img\\search.png")
        btn_image = ctk.CTkImage(img,size=(25,25))
        
        self.toplevel_window = None
        self.text_1 = ctk.CTkTextbox(self,width=250,height=50,font=("Arial",24))
        self.button_for_search = ctk.CTkButton(self,width=50,height=50,image=btn_image,text="",border_spacing=0,corner_radius=0,command=self.search)
        self.button_1 = ctk.CTkButton(self,width=200,height=50,text="新增客戶",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_add_customer)
        self.button_2 = ctk.CTkButton(self,width=200,height=50,text="編輯客戶",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_edit_customer)
        self.right_bot = right_bot_part_A(self,width=1380,height=500,fg_color="#EEEEEE")

        self.text_1.place(x=100,y=75)
        self.button_for_search.place(x=350,y=75)
        self.button_1.place(x=900,y=40)
        self.button_2.place(x=900,y=110)
        self.right_bot.place(x=0, y=200)
        
    def search(self):
        self.right_bot = right_bot_part_A(self,width=1380,height=500,fg_color="#EEEEEE")
        self.right_bot.place(x=0, y=200)
        ID = self.text_1.get(1.0, 'end-1c')
        self.right_bot.InsertData(ID)

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