from Tkinter import*

tk = Tk()
tk.title("Hello World!")
tk.geometry('300x40')
def button_clicked():
    print("Hello World!")

button=Button(tk,text="Press Me",command=button_clicked)
button.pack(fill=BOTH)

tk.mainloop()