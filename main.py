import logic
import helper
import tkinter as tk
import tkinter.font as tkfont

root = tk.Tk()
root.title("Peano Calculator")
root.geometry("500x800")

class Calculator:
    def __init__(self):
        self.mode = 2 # 0 = whole, 1 = int, 2 = rational
        self.value = "126789ABCDEF"
        self.display_font = tkfont.Font(family="TkFixedFont", size=50)
        for i in range(5):
            root.grid_columnconfigure(i, weight=1)
    
    def main(self):
        tk.Label(root, text=self.value, font=self.display_font).grid(column=0, row=0, columnspan=5, sticky="N")

calc = Calculator()
calc.main()
tk.mainloop()