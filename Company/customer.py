import os
import customtkinter as ctk
import tkinter as tk    
from PIL import Image
import psycopg2

class right_part_A(ctk.CTkFrame):    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs) 
        self.w = kwargs["width"]  
        self.h = kwargs["height"]
        self.all_en = []
        self.toplevel_window = None

        # top frame
        self.text_1 = ctk.CTkEntry(self, width=250, height=50, 
                                     font=("microsoft yahei", 24, 'bold'), 
                                     fg_color="#FFFFFF",
                                     border_color="#FFFFFF", 
                                     text_color="#000000",
                                     corner_radius=0)

        img = Image.open(f"{os.getcwd()}\\icon\\search.png")
        btn_image = ctk.CTkImage(img,size=(25,25))
        self.button_for_search = ctk.CTkButton(self, width=50, height=50, 
                                               text="",
                                               image=btn_image,  
                                               border_spacing=0,
                                               fg_color='#3B8ED0', 
                                               corner_radius=0)   

        self.button_1 = ctk.CTkButton(self, width=200, height=50, 
                                      text="新增客戶", 
                                      fg_color='#3B8ED0', 
                                      font=("microsoft yahei", 14, 'bold'))
        
        self.text_1.place(x=100, y=75)
        self.button_for_search.place(x=350, y=75)
        self.button_1.place(x=self.w-300, y=75)
        
        # bot frame title
        self.right_bot_title = bot_title(self, width=self.w, height=40, fg_color="#EEEEEE")
        self.right_bot_title.place(x=0, y=200)

        # bot frame data
        self.right_bot_data = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-270, fg_color="#EEEEEE")
        self.right_bot_data.m = self
        self.right_bot_data.place(x=0, y=240)
        self.insert_data()

        # event
        self.text_1.bind("<Return>", self.search)
        self.button_for_search.bind("<Button-1>", self.search)
        self.button_1.bind("<Button-1>", self.open_toplevel_add_customer)
    
    def reload_bot_data(self):
        self.right_bot_data.destroy()
        self.right_bot_data = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-270, fg_color="#EEEEEE")
        self.right_bot_data.m = self
        self.right_bot_data.place(x=0, y=240)
        self.insert_data()
        
    def search(self, event):
        self.reload_bot_data()    

    def open_toplevel_add_customer(self, event):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_add_customer(self)
            self.toplevel_window.title("")
            self.toplevel_window.attributes('-topmost','true')
        else:
            self.toplevel_window.focus()
    
    def insert_data(self):
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")     
        with con:
            cur = con.cursor()
            if self.text_1.get() == '':
                cur.execute("SELECT * FROM customer ORDER BY c_id")
            else:
                cur.execute(f"SELECT * FROM customer WHERE c_id = '{self.text_1.get()}' ORDER BY c_id")
            result = cur.fetchall()
            
        for r in result:
            en = bot_data_entrybox(self.right_bot_data ,width=self.w, height=40, fg_color="#EEEEEE") 
            en.pack()                       
            en.c_id.insert(0, str(r[0]).rstrip())
            en.name.insert(0, str(r[1]).rstrip())
            en.phone.insert(0, str(r[2]).rstrip())
            en.address.insert(0, str(r[3]).rstrip())
            en.remark.insert(0, str(r[4]).rstrip())
            self.all_en.append(en)

class bot_title(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/7

        self.bar_1 = ctk.CTkLabel(self, width=w, height=40,
                                        text="客戶編號",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self, width=w, height=40,
                                        text="客戶名稱",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self, width=w, height=40,
                                        text="手機",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self, width=w, height=40,
                                        text="住址",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self, width=w, height=40,
                                        text="備註",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_6 = ctk.CTkLabel(self, width=w, height=40,
                                        text="編輯",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_7 = ctk.CTkLabel(self, width=w, height=40,
                                        text="刪除",
                                        fg_color='#3B8ED0',
                                        font=("microsoft yahei", 14, 'bold'), 
                                        text_color=("#FFFFFF"))

        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)
        self.bar_6.grid(row=0,column=5)
        self.bar_7.grid(row=0,column=6)  
  
class bot_data_entrybox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.toplevel_window = None
        w = (kwargs["width"])/7

        self.c_id = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.name = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.phone = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.address = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        self.remark = ctk.CTkEntry(self,width=w,height=40, fg_color="#FFFFFF", text_color="#000000")
        editimg = Image.open(f"{os.getcwd()}\\icon\\edit.png")
        Reeditimg = ctk.CTkImage(editimg,size=(30,30))
        self.edit = ctk.CTkButton(self, image=Reeditimg, width=w, height=40, fg_color="#EEEEEE", hover_color="#EEEEEE", text="")
        deleteimg = Image.open(f"{os.getcwd()}\\icon\\close.png")
        Redeleteimg = ctk.CTkImage(deleteimg,size=(35,35))
        self.delete = ctk.CTkButton(self, image=Redeleteimg, width=w, height=40, fg_color="#EEEEEE", hover_color="#EEEEEE", text="")

        self.c_id.grid(row=0,column=0)
        self.name.grid(row=0,column=1)
        self.phone.grid(row=0,column=2)
        self.address.grid(row=0,column=3)
        self.remark.grid(row=0,column=4)
        self.edit.grid(row=0,column=5)
        self.delete.grid(row=0,column=6)

        self.edit.bind("<Button-1>", self.enedit)
        self.delete.bind("<Button-1>", self.endelete)

    def enedit(self, event):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_edit_customer(self)
            self.toplevel_window.title("")
            self.toplevel_window.attributes('-topmost','true')      
        else:
            self.toplevel_window.focus()

    def endelete(self, event):
        if tk.messagebox.askokcancel(message="是否確定要刪除 !!", icon="warning"):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")   
            with con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM customer WHERE c_id = '{self.c_id.get()}'")
                cur.execute(f"DELETE FROM order_form WHERE c_id = '{self.c_id.get()}'")

                cur.execute(f"SELECT o_id FROM order_form WHERE c_id = '{self.c_id.get()}'")
                o_ids = cur.fetchall()
                for o_id in o_ids:
                    cur.execute(f"DELETE FROM goods WHERE o_id = '{o_id}'")
                    cur.execute(f"SELECT ac_id FROM accounting WHERE o_id = '{o_id}'")
                    ac_ids = cur.fetchall()
                    cur.execute(f"DELETE FROM accounting WHERE o_id = {o_id}")
                    for ac_id in ac_ids:
                        cur.execute(f"DELETE FROM receipt WHERE ac_id = {ac_id}")
            self.reload()


    def reload(self):
        self.master.m.reload_bot_data()

class Top_level_edit_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = args[0]
        def click(event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            cur = con.cursor()
            cur.execute(f"UPDATE customer SET name = '{self.name_entry.get()}', \
                            phone = '{self.phone_entry.get()}', \
                            address = '{self.address_entry.get()}', \
                            remark = '{self.remark_entry.get(1.0,'end-1c')}' \
                            WHERE c_id = '{self.id_entry.get()}'")

            con.commit()
            con.close()
            self.master.reload()      
            self.destroy()

        def cancel(event):
            self.destroy()
        
        self.geometry("250x325")
        self.confirm = ctk.CTkButton(self,width=100,height=25,text="確認", font=("microsoft yahei", 12, 'bold'))
        self.confirm.bind('<Button-1>', click)
        self.cancel = ctk.CTkButton(self,width=100,height=25,text="取消", font=("microsoft yahei", 12, 'bold'))
        self.cancel.bind('<Button-1>', cancel)
        self.customer_id = ctk.CTkLabel(self, text="客戶編號：", font=("microsoft yahei", 14, 'bold'))
        self.name = ctk.CTkLabel(self, text="客戶名稱：", font=("microsoft yahei", 14, 'bold'))
        self.phone = ctk.CTkLabel(self, text="　　手機：", font=("microsoft yahei", 14, 'bold'))
        self.address = ctk.CTkLabel(self, text="　　住址：", font=("microsoft yahei", 14, 'bold'))
        self.remark = ctk.CTkLabel(self, text="　　備註：", font=("microsoft yahei", 14, 'bold'))

        self.id_entry = ctk.CTkEntry(self,border_width=0)   
        self.name_entry = ctk.CTkEntry(self,border_width=0)
        self.phone_entry = ctk.CTkEntry(self,border_width=0)      
        self.address_entry = ctk.CTkEntry(self,border_width=0)
        self.remark_entry = ctk.CTkTextbox(self,width=140,height=80)      

        self.customer_id.place(x=20,y=20)
        self.name.place(x=20,y=60)
        self.phone.place(x=20,y=100)
        self.address.place(x=20,y=140)
        self.remark.place(x=20,y=180)

        self.confirm.place(x=15,y=280)
        self.cancel.place(x=135,y=280)

        self.id_entry.place(x=90,y=20)
        self.name_entry.place(x=90,y=60)
        self.phone_entry.place(x=90,y=100)
        self.address_entry.place(x=90,y=140)
        self.remark_entry.place(x=90,y=180)

        self.id_entry.insert(0, str(self.master.c_id.get()))
        self.name_entry.insert(0, str(self.master.name.get()))
        if str(self.master.phone.get()) != "":
            self.phone_entry.insert(0, str(self.master.phone.get()))
        if str(self.master.address.get()) != "":
            self.address_entry.insert(0, str(self.master.address.get()))
        if  str(self.master.remark.get()) != "":
            self.remark_entry.insert(0, str(self.master.remark.get()))

class Top_level_add_customer(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = args[0]
        def click(event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            cur = con.cursor()
            cur.execute(f"INSERT INTO customer (c_id, name, phone, address, remark) \
                            VALUES('{self.id_entry.get()}', \
                            '{self.name_entry.get()}', \
                            '{self.phone_entry.get()}', \
                            '{self.address_entry.get()}' \
                            ,'{self.remark_entry.get(1.0,'end-1c')}') \
                            ")

            con.commit()
            con.close()
            self.master.reload_bot_data()
            self.destroy()

        def cancel(event):
            self.destroy()

        self.geometry("250x325")
        self.confirm = ctk.CTkButton(self,width=100,height=25,text="確認", font=("microsoft yahei", 12, 'bold'))
        self.confirm.bind('<Button-1>', click)
        self.cancel = ctk.CTkButton(self,width=100,height=25,text="取消", font=("microsoft yahei", 12, 'bold'))
        self.cancel.bind('<Button-1>', cancel)
        self.customer_id = ctk.CTkLabel(self, text="客戶編號：", font=("microsoft yahei", 14, 'bold'))
        self.name = ctk.CTkLabel(self, text="客戶名稱：", font=("microsoft yahei", 14, 'bold'))
        self.phone = ctk.CTkLabel(self, text="　　手機：", font=("microsoft yahei", 14, 'bold'))
        self.address = ctk.CTkLabel(self, text="　　住址：", font=("microsoft yahei", 14, 'bold'))
        self.remark = ctk.CTkLabel(self, text="　　備註：", font=("microsoft yahei", 14, 'bold'))

        self.id_entry = ctk.CTkEntry(self,border_width=0)
        self.name_entry = ctk.CTkEntry(self,border_width=0)
        self.phone_entry = ctk.CTkEntry(self,border_width=0)
        self.address_entry = ctk.CTkEntry(self,border_width=0)
        self.remark_entry = ctk.CTkTextbox(self,width=140,height=80)

        self.customer_id.place(x=20,y=20)
        self.name.place(x=20,y=60)
        self.phone.place(x=20,y=100)
        self.address.place(x=20,y=140)
        self.remark.place(x=20,y=180)

        self.confirm.place(x=15,y=280)
        self.cancel.place(x=135,y=280)

        self.id_entry.place(x=90,y=20)
        self.name_entry.place(x=90,y=60)
        self.phone_entry.place(x=90,y=100)
        self.address_entry.place(x=90,y=140)
        self.remark_entry.place(x=90,y=180)