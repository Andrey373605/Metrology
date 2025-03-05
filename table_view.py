from operators_func import *
from operands_func import *
import tkinter as tk
from tkinter import ttk
import math

def main():
    root = tk.Tk()
    root.title("Метрика Холстеда")

    with open('example/example/Program.cs', 'r') as file:
        content = file.read()

    tree1 = ttk.Treeview(root, columns=("Операнд", "Количество"), show="headings")
    tree1.heading("Операнд", text="Операнд")
    tree1.heading("Количество", text="Количество")

    data1 = find_operands(content)

    for item in data1:
        tree1.insert("", "end", values=item)


    tree2 = ttk.Treeview(root, columns=("Оператор", "Количество"), show="headings")
    tree2.heading("Оператор", text="Оператор")
    tree2.heading("Количество", text="Количество")

    data2 = find_operators(content)

    for item in data2:
        tree2.insert("", "end", values=item)


    tree1.pack(side="left", fill="both", expand=True)
    tree2.pack(side="right", fill="both", expand=True)

    sum_operands = sum(value for _, value in data1)
    sum_operators = sum(value for _, value in data2)
    total_sum = sum_operands + sum_operators

    count_operands = len(data1)
    count_operators = len(data2)
    total_count = count_operators + count_operands

    label = tk.Label(root, text=
                f"Словарь программы n = {count_operands} + {count_operators} = {total_count}\n"
                f"Длина программы N = {sum_operands} + {sum_operators} = {total_sum}\n"
                f"Объем программы V =  {total_sum}log2({total_count}) = {int(total_sum*math.log(total_count, 2))}"
    )


    # Размещение меток под таблицами
    label.pack(side="bottom", anchor="w", padx=10, pady=5)

    root.mainloop()
