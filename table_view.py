from operators_func import *
from operands_func import *
import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Метрика Холстеда")

    tree1 = ttk.Treeview(root, columns=("Операнд", "Количество"), show="headings")
    tree1.heading("Операнд", text="Количество")
    tree1.heading("Операнд", text="Количество")

    data1 = find_operands()

    for item in data1:
        tree1.insert("", "end", values=item)


    tree2 = ttk.Treeview(root, columns=("Оператор", "Количество"), show="headings")
    tree2.heading("Оператор", text="Количество")
    tree2.heading("Оператор", text="Количество")

    data2 = find_operators()

    for item in data2:
        tree2.insert("", "end", values=item)


    tree1.pack(side="left", fill="both", expand=True)
    tree2.pack(side="right", fill="both", expand=True)

    root.mainloop()
