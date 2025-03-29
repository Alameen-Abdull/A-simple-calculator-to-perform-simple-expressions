import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Entry widget to display the result
        self.display = ttk.Entry(root, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Add buttons to the calculator
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(root, text=button, command=cmd).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Add clear button
        ttk.Button(root, text='C', command=self.clear).grid(row=row, column=col, padx=2, pady=2)
        
        self.equation = ""
    
    def click(self, value):
        if value == '=':
            try:
                result = eval(self.equation)
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.equation = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.equation = ""
        else:
            self.equation += value
            self.display.delete(0, tk.END)
            self.display.insert(0, self.equation)
    
    def clear(self):
        self.equation = ""
        self.display.delete(0, tk.END)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
