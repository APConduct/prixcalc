from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="black", fg="yellow", borderwidth=8)
e.pack()
e.insert(0, "Enter your Name")

def myClick():
    hello = "Hello " + e.get() + ". You are based."
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick, fg="yellow", bg="green") #padx=32, pady=32 padx=250, pady=400
myButton.pack()

root.mainloop()