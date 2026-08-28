import logic
import helper
import tkinter as tk
import tkinter.font as tkfont
import json
from pathlib import Path
import random

from playsound3 import playsound 

root = tk.Tk()
root.title("Peano Calculator")
root.geometry("500x310")



class Calculator:
    def __init__(self):
        self.mode = 2 # 0 = whole, 1 = int, 2 = rational
        self.original = "               "
        self.display = self.original
        self.string = ""
        self.offset = 0
        self.memory = (((), ()), (((),), ()))
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
        if value in {"<-", "->", "AC", "C", "M+", "M-", "MR", "MS", ":3c", '='}:
            if value == ":3c":
                self.play_cats()
            elif value == "AC":
                self.string = ""
                self.display = self.buffer(self.string, len(self.original))
            elif value == "C":
                self.string = self.string[:-1]
                self.display = self.buffer(self.string, len(self.original))
            elif value in {"<-", "->"}:
                self.do_offset = True
                if value == "->":
                    if self.offset:
                        self.offset -= 1
                elif len(self.string) >= len(self.original) + self.offset:
                    self.offset += 1
                
                if self.offset:
                    self.display = self.buffer(self.string[:-self.offset], len(self.original) - 1) + '>'
                else:
                    self.display = self.buffer(self.string, len(self.original))
            elif (not any(char in {"+", "-", "x", "÷", "ans", 'M'} for char in self.string)) and self.string:
                if value == "M+":
                    self.memory = logic.addition_rational(self.memory, helper.readable_peano_rational(float(self.string)))
                elif value == "M-":
                    self.memory = logic.subtraction_rational(self.memory, helper.readable_peano_rational(float(self.string)))
                else:
                    self.memory = helper.readable_peano_rational(float(self.string))
                print(helper.peano_readable_rational(self.memory))
            elif value == "MR":
                self.string = self.string + 'M'
                self.display = self.buffer(self.string, len(self.original))
            elif value == '=':
                self.evaluate(self.string)

            self.main()
        
        else:
            self.offset = 0
            self.string = self.string + value
            self.display = self.buffer(self.string, len(self.original))
            self.main()
    
    def buffer(self, string: str, target_size: int):
        str_size = len(string)
        if str_size == target_size:
            return string
        elif str_size < target_size:
            return string + (" " * (target_size - str_size))
        trail = string[-(target_size - 1):]
        return "<" + trail
    
    def play_cats(self):
        files = [f for f in Path("./cats").iterdir()]
        if not files:
            print("No cats found :(")
            return
        if random.randint(0, 50) == 0:
            for file in files:
                playsound(Path(file), False)
                return
        file = random.choice(files)
        playsound(Path(file), False)

calc = Calculator()
calc.main()
tk.mainloop()