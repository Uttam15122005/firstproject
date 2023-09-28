from tkinter import*
root=Tk()
root_label=Label(text="WELCOME TO MY MINIPROJECT")
root_label.pack()
def Name():
    print("hii i am uttam kumar")
def Information():
    print("my name is uttam kumar i am from bihar dist- Sitamarhi,Capital-BHARAT")
root.geometry("540x345")
root["bg"]="yellow"
root.title=("WELCOME TO MY TKINTER PROJECT")
frame = Frame(root,borderwidth=6,bg="red",relief=SUNKEN)
frame.pack()
b1 = Button(frame,fg="red",text="print",command=Name)
b1.pack(side=LEFT,padx=22)
b2 = Button(frame,fg="black",text="information",bg="green" ,command=Information)
b2.pack(side=LEFT)


root.mainloop()

