from tkinter import *
from tkinter import ttk
import re

win = Tk()
win.title("Sudoku Breaker")
win.geometry("500x600")

for c in range(9): win.columnconfigure(index=c, weight=1)
for r in range(10): win.rowconfigure(index=r, weight=1)

def is_valid(string):
    return re.match("^[1-9]?$", string) is not None

entry_list = [[] for _ in range(9)]
for r in range(9):
    for c in range(9):
        check = (win.register(is_valid), "%P")
        entry_list[r].append(ttk.Entry(justify="center", validate="key", validatecommand=check))
        entry_list[r][c].grid(row=r, column=c, sticky=NSEW)

win.mainloop()