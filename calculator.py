from tkinter import *

root = Tk()
root.title("Prix Calc")
root.config(background="black")
root.minsize(50, 50)

e = Entry(root, width=50, bg="green", fg="yellow", borderwidth=10)
e.grid(row=0, column=0, columnspan=3, pady=10)

#e.insert(0, "Enter your Name")

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="black", fg="lightGreen")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="black", fg="lightGreen")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="black", fg="lightGreen")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="black", fg="lightGreen")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="black", fg="lightGreen")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="black", fg="lightGreen")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="black", fg="lightGreen")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="black", fg="lightGreen")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="black", fg="lightGreen")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="black", fg="lightGreen")
button_add = Button(root, text="+", padx=39, pady=20, command=button_add, bg="black", fg="lightGreen")
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal, bg="black", fg="lightGreen")
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear, bg="black", fg="lightGreen")

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=3)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=3)


myButton = Button(root, text="Enter Your Name", fg="yellow", bg="green") #padx=32, pady=32 padx=250, pady=400


root.mainloop()