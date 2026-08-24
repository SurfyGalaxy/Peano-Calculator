import logic
import helper
import tkinter as tk
import tkinter.font as tkfont
import json

import playsound3 as ps

root = tk.Tk()
root.title("Peano Calculator")
root.geometry("500x310")

class Calculator:
    def __init__(self):
        self.mode = 2 # 0 = whole, 1 = int, 2 = rational
        self.original = "               "
        self.display = "               "
        self.string = ""
        self.display_font = tkfont.Font(family="DejaVu Sans Mono", size=40)
        for i in range(5):
            root.grid_columnconfigure(i, weight=1)

        with open("buttons.json") as f:
            self.buttons = json.load(f)

    def main(self):
        tk.Button(root, text=self.display, font=self.display_font).grid(column=0, row=0, columnspan=5, sticky="N")
        tk.Button(root, text="<-", command=lambda: self.inputs("<-")).grid(column=0, row=1, columnspan=2, sticky="NESW")
        tk.Button(root, text=":3c", command=lambda:self.inputs(":3c")).grid(column=2, row=1, sticky="NESW")
        tk.Button(root, text="->", command=lambda: self.inputs("->")).grid(column=3, row=1, columnspan=2, sticky="NESW")
        for name in self.buttons:
            data = self.buttons[name]

            button = tk.Button(
                root,
                text=data["text"],
                command=lambda text=data["text"]: self.inputs(text)
            )

            button.grid(
                column=data["col"],
                row=data["row"],
                sticky="NESW"
            )

            globals()[name] = button
        
    def inputs(self, value):
        if value in {"<-", "->", "AC", "C", "M+", "M-", "MR", "MS", ":3c"}:
            if value == ":3c":
                play_cats()
        
        else:
            self.string = self.string + value
            if len(self.string) - len(self.original) < 0:
                self.display = self.string + self.original[len(self.string):]
            else:
                self.display = "<" + self.string[-len(self.original):]
        print(self.string)
        self.main()

calc = Calculator()
calc.main()
tk.mainloop()