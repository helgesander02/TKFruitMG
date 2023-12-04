import os
import customtkinter as ctk
from PIL import ImageTk,Image
import psycopg2

class right_top_part_B(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.w = kwargs["width"]
        self.h = kwargs["height"]  
        img = Image.open(f"{os.getcwd()}\\icon\\search.png")
        btn_image = ctk.CTkImage(img,size=(25,25))
        self.all_en = []
        self.toplevel_window = None
        self.text_1 = ctk.CTkTextbox(self,width=250,height=50, font=("microsoft yahei", 24, 'bold'), fg_color="#FFFFFF", corner_radius=0)
        self.button_for_search = ctk.CTkButton(self,width=50,height=50,image=btn_image,text="",border_spacing=0,corner_radius=0,fg_color='#3B8ED0',command=self.search)
        self.button_1 = ctk.CTkButton(self,width=200,height=50,text="新增品項", fg_color='#3B8ED0', font=("microsoft yahei", 14, 'bold'))
        self.right_bot_title = right_bot_title_part_B(self, width=self.w, height=40, fg_color="#EEEEEE")
        self.right_bot_data = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-270, fg_color="#EEEEEE")
        self.right_bot_data.m = self
        self.InsertData()

        self.text_1.place(x=100,y=75)
        self.button_for_search.place(x=350,y=75)       
        self.button_1.place(x=self.w-300,y=75)
        self.right_bot_title.place(x=0, y=200)
        self.right_bot_data.place(x=0, y=240)
        
        self.button_for_search.bind("<Button-1>", self.search)
        self.button_1.bind("<Button-1>", self.open_toplevel_add_item)

    def reload_botdata(self):
        self.right_bot_data.destroy()
        self.right_bot_data = ctk.CTkScrollableFrame(self, width=self.w-20, height=self.h-270, fg_color="#EEEEEE")
        self.right_bot_data.m = self
        self.right_bot_data.place(x=0, y=240)
        self.InsertData()

    def search(self, event):
        self.reload_botdata()

    def open_toplevel_add_item(self, event):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_add_item(self)
            self.toplevel_window.title("")
            self.toplevel_window.attributes('-topmost','true')
        else:
            self.toplevel_window.focus()
    
    def InsertData(self):
        con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")     
        with con:
            cur = con.cursor()
            if self.text_1.get(1.0, 'end-1c') == '':
                cur.execute("SELECT * FROM item ORDER BY item_id")
            else:
                cur.execute(f"SELECT * FROM item WHERE item_id = '{self.text_1.get(1.0, 'end-1c')}' ORDER BY item_id")
            result = cur.fetchall()
            
        for r in result:
            en = entrybox(self.right_bot_data ,width=self.w, height=40, fg_color="#EEEEEE") 
            en.pack()                       
            en.item_id.insert(0, str(r[0]).rstrip())
            en.item_name.insert(0, str(r[1]).rstrip())
        
            self.all_en.append(en)

class right_bot_title_part_B(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        w = kwargs["width"]/7
        self.bar_1 = ctk.CTkLabel(self, width=w, height=40,text="品項編號",
                                    fg_color='#3B8ED0', 
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_2 = ctk.CTkLabel(self, width=w, height=40,text="品項名稱",
                                    fg_color='#3B8ED0', 
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_3 = ctk.CTkLabel(self, width=w, height=40,text="編輯",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_4 = ctk.CTkLabel(self, width=w, height=40,text="刪除",
                                    fg_color='#3B8ED0',
                                    font=("microsoft yahei", 14, 'bold'), 
                                    text_color=("#FFFFFF"))

        self.bar_5 = ctk.CTkLabel(self, width=w+w+w, height=40,text="",fg_color='#3B8ED0')

        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)
        self.bar_4.grid(row=0,column=3)
        self.bar_5.grid(row=0,column=4)

class entrybox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.toplevel_window = None
        w = (kwargs["width"])/7
        self.item_id = ctk.CTkEntry(self,width=w, height=40, fg_color="#FFFFFF", text_color="#000000")
        self.item_name = ctk.CTkEntry(self,width=w, height=40, fg_color="#FFFFFF", text_color="#000000")

        editimg = Image.open(f"{os.getcwd()}\\icon\\edit.png")
        Reeditimg = ctk.CTkImage(editimg,size=(30,30))
        self.edit = ctk.CTkButton(self, image=Reeditimg, width=w, height=40, fg_color="#EEEEEE", hover_color="#EEEEEE", text="")

        deleteimg = Image.open(f"{os.getcwd()}\\icon\\close.png")
        Redeleteimg = ctk.CTkImage(deleteimg,size=(35,35))
        self.delete = ctk.CTkButton(self, image=Redeleteimg, width=w, height=40, fg_color="#EEEEEE", hover_color="#EEEEEE", text="")

        self.space = ctk.CTkLabel(self, text="", width=w+w+w, height=40, fg_color="#EEEEEE")

        self.item_id.grid(row=0,column=0)
        self.item_name.grid(row=0,column=1)
        self.edit.grid(row=0,column=2)
        self.delete.grid(row=0,column=3)
        self.space.grid(row=0,column=4)

        self.edit.bind("<Button-1>", self.enedit)
        self.delete.bind("<Button-1>", self.endelete)

    def enedit(self, event):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_edit_item(self)
            self.toplevel_window.title("")
            self.toplevel_window.attributes('-topmost','true')      
        else:
            self.toplevel_window.focus()

    def endelete(self, event):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Top_level_check_delete(self)
            self.toplevel_window.title("")
            self.toplevel_window.attributes('-topmost','true')    
        else:
            self.toplevel_window.focus()

    def reload(self):
        self.master.m.reload_botdata()

class Top_level_check_delete(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x150")
        self.master = args[0]
        def click(event):
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")     
            with con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM item WHERE item_id = '{self.master.item_id.get()}'")
            self.master.reload()
            self.destroy()

        def cancel(event):
            self.destroy()

        self.msg = ctk.CTkLabel(self, text="是否確定要刪除 !!", font=("microsoft yahei", 20, 'bold'))
        self.confirm = ctk.CTkButton(self,width=100,height=25,text="確認", font=("microsoft yahei", 14, 'bold'))
        self.confirm.bind('<Button-1>', click)
        self.cancel = ctk.CTkButton(self,width=100,height=25,text="取消", font=("microsoft yahei", 14, 'bold'))
        self.cancel.bind('<Button-1>', cancel)
        self.msg.place(x=50,y=40)
        self.confirm.place(x=25,y=110)
        self.cancel.place(x=135,y=110)

class Top_level_add_item(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = args[0]
        def confirm(event):
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            with con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO item(item_id, item_name) VALUES('{self.item_id_entry.get()}','{self.item_name_entry.get()}')")
            self.master.reload_botdata()
            self.destroy()

        def cancel(event):
            self.destroy()

        self.item_id = ctk.CTkLabel(self,text="品項編號：", font=("microsoft yahei", 14, 'bold'))
        self.item_name = ctk.CTkLabel(self,text="品項名稱：", font=("microsoft yahei", 14, 'bold'))
        self.item_id_entry = ctk.CTkEntry(self)
        self.item_name_entry = ctk.CTkEntry(self)
        self.confirm = ctk.CTkButton(self,text="確認", font=("microsoft yahei", 14, 'bold'))
        self.confirm.bind('<Button-1>', confirm)
        self.cancel = ctk.CTkButton(self,text="取消", font=("microsoft yahei", 14, 'bold'))
        self.cancel.bind('<Button-1>', cancel)

        self.item_id.grid(row=0, column=0,padx=10,pady=10)
        self.item_name.grid(row=1, column=0,padx=10,pady=10)
        self.item_id_entry.grid(row=0, column=1,padx=10,pady=10)
        self.item_name_entry.grid(row=1, column=1,padx=10,pady=10)
        self.cancel.grid(row=2,column=1,padx=10,pady=10)
        self.confirm.grid(row=2,column=0,padx=10,pady=10)

class Top_level_edit_item(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = args[0]
        def confirm(event):
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            with con:
                cur = con.cursor()
                cur.execute(f"UPDATE item SET item_name = '{self.item_name_entry.get()}' \
                            WHERE item_id = '{self.item_id_entry.get()}'")
            self.master.reload()
            self.destroy()

        def cancel(event):
            self.destroy()

        self.item_id = ctk.CTkLabel(self,text="品項編號：", font=("microsoft yahei", 14, 'bold'))
        self.item_name = ctk.CTkLabel(self,text="品項名稱：", font=("microsoft yahei", 14, 'bold'))
        self.item_id_entry = ctk.CTkEntry(self)
        self.item_name_entry = ctk.CTkEntry(self)
        self.confirm = ctk.CTkButton(self,text="確認", font=("microsoft yahei", 14, 'bold'))
        self.confirm.bind('<Button-1>', confirm)
        self.cancel = ctk.CTkButton(self,text="取消", font=("microsoft yahei", 14, 'bold'))
        self.cancel.bind('<Button-1>', cancel)

        self.item_id.grid(row=0, column=0,padx=10,pady=10)
        self.item_name.grid(row=1, column=0,padx=10,pady=10)
        self.item_id_entry.grid(row=0, column=1,padx=10,pady=10)
        self.item_name_entry.grid(row=1, column=1,padx=10,pady=10)
        self.cancel.grid(row=2,column=1,padx=10,pady=10)
        self.confirm.grid(row=2,column=0,padx=10,pady=10)
        self.item_id_entry.insert(0, str(self.master.item_id.get()))
        self.item_name_entry.insert(0, str(self.master.item_name.get()))
