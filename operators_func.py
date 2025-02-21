import re

def foo():
    pattern = r'\W'
    string = "Пример (с (вложенными 3 (парами скобок)) и еще одной парой (скобок))."

    matches = re.findall(pattern, string)
    print(matches)

foo()

