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

    data1 = find_operators()

    for item in data1:
        tree1.insert("", "end", values=item)


    # Вторая таблица
    tree2 = ttk.Treeview(root, columns=("Колонка 1", "Колонка 2"), show="headings")
    tree2.heading("Колонка 1", text="Колонка 1")
    tree2.heading("Колонка 2", text="Колонка 2")

    # Пример данных для второй таблицы
    data2 = [("Элемент A", "Значение A"), ("Элемент B", "Значение B")]

    for item in data2:
        tree2.insert("", "end", values=item)

    # Размещение таблиц на странице
    tree1.pack(side="left", fill="both", expand=True)
    tree2.pack(side="right", fill="both", expand=True)

    root.mainloop()
