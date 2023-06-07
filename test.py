import tkinter as tk

root = tk.Tk()
root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
# root.iconbitmap('heart_green.ico')
root.geometry('350x200')

def fruitselect():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection = selection +fruits[i] + "\t"
    print(selection)
        
lF=tk.LabelFrame(root,text="Choise your favirot fruit.",fg="#FFAAD5", bg="#7AFEC6",font=("Ravie",10,"bold"),width=30)
lF.pack(ipadx=5,ipady=5,pady=10)

fruits = {0:"Strawberry",1: "Peach",2:"mango",3:"Cherry"}

checkboxes = {}

for i in range(len(fruits)):
    checkboxes[i] = tk.BooleanVar()
    cb=tk.Checkbutton(lF,text=fruits[i],variable=checkboxes[i])
    cb.grid(row=i+1,sticky='w')
    print(checkboxes[i])



btn = tk.Button (root,text="DOWN",width=10,command=fruitselect)
btn.pack()

root.mainloop()