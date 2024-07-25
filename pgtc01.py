import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(0, 0)

        self.expression = ""

        # Entry box for displaying the expression
        self.entry_text = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_text, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_value = 1
        col_value = 0
        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda button=button: self.on_button_click(button)).grid(row=row_value, column=col_value)
            col_value += 1
            if col_value > 3:
                col_value = 0
                row_value += 1

        # Clear button
        tk.Button(self, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear).grid(row=row_value, column=0, columnspan=4, sticky='nsew')

    def on_button_click(self, button):
        if button == "=":
            try:
                # Evaluate the expression and display the result
                result = str(eval(self.expression))
                self.entry_text.set(result)
                self.expression = result
            except:
                self.entry_text.set("Error")
                self.expression = ""
        else:
            # Update the expression
            self.expression += button
            self.entry_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.entry_text.set("")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
