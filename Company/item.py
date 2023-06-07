import os
import customtkinter as ctk
from PIL import ImageTk,Image
import psycopg2

class Top_level_add_item(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.geometry("200x200")
        def confirm():
            con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
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
            con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
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

class right_bot_part_B(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bar_1 = ctk.CTkLabel(self, width=176, height=40,text="序號")
        self.bar_2 = ctk.CTkLabel(self, width=176, height=40,text="品項編號")
        self.bar_3 = ctk.CTkLabel(self, width=176, height=40,text="品項名稱")
        self.bar_1.grid(row=0,column=0)
        self.bar_2.grid(row=0,column=1)
        self.bar_3.grid(row=0,column=2)

    def InsertData(self, ID):
        con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
        cur = con.cursor()
        if ID == '':
            cur.execute(f"SELECT * FROM item")
        else:
            cur.execute(f"SELECT * FROM item WHERE item_id = '{ID}'")
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

        con.commit()
        con.close()

class right_top_part_B(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        img = Image.open(f"{os.getcwd()}\\img\\search.png")
        btn_image = ctk.CTkImage(img,size=(25,25))

        self.toplevel_window = None
        self.text_1 = ctk.CTkTextbox(self,width=250,height=50,font=("Arial",24))
        self.button_for_search = ctk.CTkButton(self,width=50,height=50,image=btn_image,text="",border_spacing=0,corner_radius=0,command=self.search)
        self.button_1 = ctk.CTkButton(self,width=200,height=50,text="新增品項",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_add_item)
        self.button_2 = ctk.CTkButton(self,width=200,height=50,text="編輯品項",font=("microsoft yahei", 14, 'bold'),command=self.open_toplevel_edit_item)
        self.right_bot = right_bot_part_B(self,width=1380,height=500,fg_color="#EEEEEE")


        self.text_1.place(x=100,y=75)
        self.button_for_search.place(x=350,y=75)
        self.button_1.place(x=900,y=40)
        self.button_2.place(x=900,y=110)
        self.right_bot.place(x=0, y=200)

    def search(self):
        self.right_bot = right_bot_part_B(self,width=1380,height=500,fg_color="#EEEEEE")
        self.right_bot.place(x=0, y=200)
        ID = self.text_1.get(1.0, 'end-1c')
        self.right_bot.InsertData(ID)

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

