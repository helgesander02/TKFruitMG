# -*- coding: utf-8 -*-
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
# from ttkthemes import ThemedStyle
import pandas as pd
def op():
    sfname = filedialog.askopenfilename(title='選擇', filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
    return sfname
def read(sfname):
    df = pd.read_excel(sfname,header=0)
    cols = list(df.columns)
    return df,cols
def show(frame,df,cols):
    tree = ttk.Treeview(frame)
    tree.pack()
    tree["columns"] = cols
    for i in cols:
        tree.column(i,anchor="center")
        tree.heading(i,text=i,anchor='center')
    for index, row in df.iterrows():
        tree.insert("",'end',text = index,values=list(row))
    return tree
def oas():
    global root
    filename = op()
    data,c = read(filename)
    tree = show(root,data,c)
    tree.place(relx=0,rely=0.1,relheight=0.7,relwidth=1)
# def main():
#     global root
#     root = tk.Tk()
#     # style = ThemedStyle(root)
#     # style.set_theme("breeze")
#     root.geometry("1600x1000")
#     B1 = tk.Button(root, text="打開",command = oas).pack()
#     root.mainloop()
# if __name__=='__main__':
#     main()