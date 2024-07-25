from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked the button.")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, padx=32, pady=32, fg="yellow", bg="green") #padx=250, pady=400
myButton.pack()

root.mainloop()