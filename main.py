import logic
import helper
import tkinter as tk
import tkinter.font as tkfont
import json

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

        with open("buttons.json") as f:
            self.buttons = json.load(f)

    def main(self):
        tk.Button(root, text=self.value, font=self.display_font).grid(column=0, row=0, columnspan=5, sticky="N")
        for name in self.buttons:
            data = self.buttons[name]
            
            button = tk.Button(root, text=data["text"], command=lambda: add(data["text"]))
            button.grid(column=data["col"], row=data["row"], sticky="NESW")

calc = Calculator()
calc.main()
tk.mainloop()