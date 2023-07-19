import customtkinter as ctk
import os
import sv_dt
from PIL import ImageTk,Image
import psycopg2

from Company.company import Company_Main_Frame
from Order.order import Order_Main_Frame
from Accounting.accounting import Accounting_Main_Frame
from Printdata.printdata import Printdata_Main_Frame
from sql import createdatatable

class Select_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.copymsg = None
        homeimg = Image.open(f"{os.getcwd()}\\img\\home.png")
        Rehomeimg = ctk.CTkImage(homeimg,size=(50,50))
        self.btn_home = ctk.CTkButton(self ,text="" ,image=Rehomeimg ,width=160 ,height=160,
                                                                fg_color=("#5b5a5a"), corner_radius=0)
        self.btn_home.grid(row=0, column=0)

        copyimg = Image.open(f"{os.getcwd()}\\img\\copy.png")
        Recopyimg = ctk.CTkImage(copyimg,size=(50,50))
        self.btn_copy = ctk.CTkButton(self ,text="" ,image=Recopyimg ,width=160 ,height=160,
                                                                fg_color=("#5b5a5a"), corner_radius=0,
                                                                command=self.open_copy)
        self.btn_copy.grid(row=0, column=1)

        self.lab_other = ctk.CTkLabel(self, width = kwargs["width"]-320, height = kwargs["height"], 
                                                                fg_color=("#5b5a5a"), text="")

        self.lab_other.grid(row=0, column=2)

    def open_copy(self):        
            if self.copymsg is None or not self.copymsg.winfo_exists():
                self.copymsg = CopyMsg(self)
                self.copymsg.focus()
                self.copymsg.attributes('-topmost','true')
                sv_dt.sv()
            else:
                self.copymsg.focus()

class CopyMsg(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x100")

        self.label = ctk.CTkLabel(self, text="已成功儲存資料")
        self.label.pack(padx=20, pady=20)

class Home_Main_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        wedge = kwargs["width"]/13
        hedge = kwargs["height"]/6
        #self.frame = ctk.CTkFrame(self, width=kwargs["width"],height=kwargs["height"],fg_color="green")
        companyimg = Image.open(f"{os.getcwd()}\\img\\company.png")
        Recompanyimg = ctk.CTkImage(companyimg,size=(60,60))
        self.btn_company = ctk.CTkButton(self ,text="" ,image=Recompanyimg  ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_company.place(x=wedge*3, y=hedge)
        self.lab_company = ctk.CTkLabel(self, text="公司管理", font=("microsoft yahei", 20, 'bold'))
        self.lab_company.place(x=wedge*3+40, y=hedge*2+40)

        orderimg = Image.open(f"{os.getcwd()}\\img\\order.png")
        Reorderimg = ctk.CTkImage(orderimg,size=(60,60))
        self.btn_order = ctk.CTkButton(self ,text="" ,image=Reorderimg ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_order.place(x=wedge*3, y=hedge*3)
        self.lab_order = ctk.CTkLabel(self, text="訂貨單輸入", font=("microsoft yahei", 20, 'bold'))
        self.lab_order.place(x=wedge*3+30, y=hedge*4+40)

        accountingimg = Image.open(f"{os.getcwd()}\\img\\accounting.png")
        Reaccountingimg = ctk.CTkImage(accountingimg,size=(60,60))
        self.btn_accounting = ctk.CTkButton(self ,text="" ,image=Reaccountingimg ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_accounting.place(x=wedge*5, y=hedge)
        self.lab_accounting = ctk.CTkLabel(self, text="入賬管理", font=("microsoft yahei", 20, 'bold'))
        self.lab_accounting.place(x=wedge*5+40, y=hedge*2+40)

        printimg = Image.open(f"{os.getcwd()}\\img\\print.png")
        Reprintimg = ctk.CTkImage(printimg,size=(60,60))
        self.btn_print = ctk.CTkButton(self ,text="" ,image=Reprintimg ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_print.place(x=wedge*5, y=hedge*3)
        self.lab_print = ctk.CTkLabel(self, text="明細單列印", font=("microsoft yahei", 20, 'bold'))
        self.lab_print.place(x=wedge*5+30, y=hedge*4+40)

        self.btn_other1 = ctk.CTkButton(self ,text="" ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_other1.place(x=wedge*7, y=hedge)

        self.btn_other2 = ctk.CTkButton(self ,text="" ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_other2.place(x=wedge*7, y=hedge*3)

        self.btn_other3 = ctk.CTkButton(self ,text="" ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_other3.place(x=wedge*9, y=hedge)

        self.btn_other4 = ctk.CTkButton(self ,text="" ,width=160 ,height=160 ,
                                                                fg_color=("#DDDDDD"), text_color=("#5b5a5a"))
        self.btn_other4.place(x=wedge*9, y=hedge*3)
    
        #self.frame.grid(row=0,column=0,columnspan=3)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{0}+{0}")
        self.title("Management System")
        try:
            #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
            con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
            with con:
                cur = con.cursor()
                cur.execute(f"select * from customer")
        except:
            createdatatable()

        #Select_Frame
        self.Select_Frame = Select_Frame(self, width = w , height = 160, fg_color=("#5b5a5a"))
        self.Select_Frame.grid(row=0, column=0, sticky='nsew')
        #Main_Frame
        self.Main_Frame = Home_Main_Frame(self, width = w , height = h-160, fg_color=("#FFFFFF"))
        self.Main_Frame.grid(row=1, column=0, sticky='nsew')

        #關掉主要的Frame開啟對應btn的Frame
        #隱藏的方法 https://www.delftstack.com/zh-tw/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/
        def open_home (event):   
            self.Main_Frame.grid_forget()
            self.Main_Frame = Home_Main_Frame(self, width = w , height = h-160, fg_color=("#FFFFFF"))
            self.Main_Frame.grid(row=1, column=0,sticky='nsew')
            self.Main_Frame.btn_company.bind("<Button-1>", open_company)
            self.Main_Frame.btn_order.bind("<Button-1>", open_order)
            self.Main_Frame.btn_accounting.bind("<Button-1>", open_accounting)
            self.Main_Frame.btn_print.bind("<Button-1>", open_printdata)

        def open_company (event):   
            self.Main_Frame.grid_forget()
            self.Main_Frame = Company_Main_Frame(self, width = w , height = h-160, fg_color=("#FFFFFF"))
            self.Main_Frame.grid(row=1, column=0,sticky='nsew')

        def open_order (event):   
            self.Main_Frame.grid_forget()
            self.Main_Frame = Order_Main_Frame(self, width = w , height = h-160, fg_color=("#FFFFFF"))
            self.Main_Frame.grid(row=1, column=0,sticky='nsew')

        def open_accounting (event):   
            self.Main_Frame.grid_forget()
            self.Main_Frame = Accounting_Main_Frame(self, width = w , height = h-160, fg_color=("#FFFFFF"))
            self.Main_Frame.grid(row=1, column=0,sticky='nsew')

        def open_printdata (event):   
            self.Main_Frame.grid_forget()
            self.Main_Frame = Printdata_Main_Frame(self, width = w , height = h-160, fg_color=("#FFFFFF"))
            self.Main_Frame.grid(row=1, column=0,sticky='nsew')

        #切換功能
        #btn事件教學 https://ithelp.ithome.com.tw/articles/10275712?sc=iThomeR
        self.Select_Frame.btn_home.bind("<Button-1>", open_home)
        self.Main_Frame.btn_company.bind("<Button-1>", open_company)
        self.Main_Frame.btn_order.bind("<Button-1>", open_order)
        self.Main_Frame.btn_accounting.bind("<Button-1>", open_accounting)
        self.Main_Frame.btn_print.bind("<Button-1>", open_printdata)
    
        


app = App()
app.mainloop()