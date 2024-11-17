from tkinter import *
from tkinter import ttk
import re

win = Tk()
win.title("Sudoku Breaker")
win.geometry("500x600")

for c in range(9): win.columnconfigure(index=c, weight=1)
for r in range(9): win.rowconfigure(index=r, weight=1)
def is_valid(string):
    return re.match("^[1-9]?$", string) is not None
for r in range(9):
    for c in range(9):
        check = (win.register(is_valid), "%P")
        entry = ttk.Entry(validate="key", validatecommand=check)
        entry.grid(row=r, column=c, sticky=NSEW)

win.mainloop()