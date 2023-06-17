import os
import customtkinter as ctk
from PIL import ImageTk,Image
import psycopg2

class Top_level_edit_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def click():
            conn = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            cur = conn.cursor()
            cur.execute(f"UPDATE customer SET name = '{name_entry.get()}', \
                            phone = '{phone_entry.get()}', \
                            address = '{address_entry.get()}', \
                            remark = '{remark_entry.get(1.0,'end-1c')}' \
                            WHERE c_id = '{id_entry.get()}'")

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

        self.id_entry = ctk.CTkEntry(self,border_width=0)
        self.name_entry = ctk.CTkEntry(self,border_width=0)
        self.phone_entry = ctk.CTkEntry(self,border_width=0)
        self.address_entry = ctk.CTkEntry(self,border_width=0)
        self.remark_entry = ctk.CTkTextbox(self,width=140,height=80)

        customer_id.place(x=20,y=20)
        name.place(x=20,y=60)
        phone.place(x=20,y=100)
        address.place(x=20,y=140)
        remark.place(x=20,y=180)

        confirm.place(x=25,y=280)
        cancel.place(x=145,y=280)

        self.id_entry.place(x=85,y=20)
        self.name_entry.place(x=85,y=60)
        self.phone_entry.place(x=85,y=100)
        self.address_entry.place(x=85,y=140)
        self.remark_entry.place(x=85,y=180)

class Top_level_add_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def click():
            conn = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
            cur = conn.cursor()
            cur.execute(f"INSERT INTO customer (c_id, name, phone, address, remark) \
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
        w = kwargs["width"]/6
        self.bar_1 = ctk.CTkLabel(self, width=w, height=40,
                                        text="序號",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self, width=w, height=40,
                                        text="客戶編號",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self, width=w, height=40,
                                        text="客戶名稱",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self, width=w, height=40,
                                        text="手機",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self, width=w, height=40,
                                        text="住址",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_6 = ctk.CTkLabel(self, width=w, height=40,
                                        text="備註",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))
                                        
        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)
        self.bar_6.grid(row=0,column=5)

    def InsertData(self, ID):
        conn = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
        cur = conn.cursor()
        if ID == '':
            cur.execute(f"SELECT * FROM customer")
        else:
            cur.execute(f"SELECT * FROM customer WHERE c_id = '{ID}'")
        result = cur.fetchall()
        row = 1
        for i in result:
                x=0
                for j in i:
                    temp = ctk.CTkEntry(self)
                    temp.insert(0, str(j).rstrip())
                    temp.grid(row=row,column=x)
                    temp.configure(state="disabled")
                    x+=1
                row += 1

        conn.commit()
        conn.close()

class right_top_part_A(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs) 
        self.w = kwargs["width"]  
        img = Image.open(f"{os.getcwd()}\\img\\search.png")
        btn_image = ctk.CTkImage(img,size=(25,25))
        self.toplevel_window = None
        self.text_1 = ctk.CTkTextbox(self,width=250,height=50,font=("Arial",24))
        self.button_for_search = ctk.CTkButton(self,width=50,height=50,image=btn_image,text="",border_spacing=0,corner_radius=0,command=self.search)
        self.button_1 = ctk.CTkButton(self,width=200,height=50,text="新增客戶",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_add_customer)
        self.button_2 = ctk.CTkButton(self,width=200,height=50,text="編輯客戶",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_edit_customer)
        self.right_bot = right_bot_part_A(self,width=self.w,height=500,fg_color="#EEEEEE")

        self.text_1.place(x=100,y=75)
        self.button_for_search.place(x=350,y=75)
        self.button_1.place(x=self.w-300,y=40)
        self.button_2.place(x=self.w-300,y=110)
        self.right_bot.place(x=0, y=200)
        
    def search(self):
        self.right_bot = right_bot_part_A(self,width=self.w,height=500,fg_color="#EEEEEE")
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
        conn = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
        with conn:
            cur = conn.cursor()
            cur.execute(f"select * from customer where c_id='{self.text_1.get(1.0, 'end-1c')}'")
            result = cur.fetchone()
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_edit_customer(self)
            self.toplevel_window.attributes('-topmost','true')
            try:
                self.toplevel_window.id_entry.insert(0, str(result[0]).rstrip())
                self.toplevel_window.name_entry.insert(0, str(result[1]).rstrip())
                self.toplevel_window.phone_entry.insert(0, str(result[2]).rstrip())
                self.toplevel_window.address_entry.insert(0, str(result[3]).rstrip())
                self.toplevel_window.remark_entry.insert(0, str(result[4]).rstrip())
            except TypeError as e:
                pass
        else:
            self.toplevel_window.focus()