import re

data = {'+': r'[^+]([+])[^+=]',
        '-': r'[^-]([-])[^-=]',
        '*': r'[^*]([*])[^*=]',
        '/': r'[^/]([/])[^/=]',
        '%': r'[^%]([%])[^%=]',
        '|': r'[^|](\|)[^|]',
        '||': r'(\|\|)',
        '&': r'[^&]([&])[^&]',
        '&&': r'(&&)',
        '~': '(~)',
        '^': r'(\^)',
        '>': r'([>])[^=]',
        '<': r'([<])[^=]',
        '>=': r'(>=)',
        '<=': r'(<=)',
        '==': r'(==)',
        '!=': r'(!=)',
        ';': r'(;)',
        '=': r'[^=+-/*%<>](=)[^=]',
        'is': r'\b(is)\b',
        'as': r'\b(as)\b',
        '>>': r'(>>)',
        '<<': r'(<<)',
        'goto': r'(goto)',
        'if': r'if\s+\(.+\)[^{]+\{[^{]+\}',
        'else': r'(else)',
        'while': r'(while)[\w\W]+\([\w\W]+\)\s+[^;]',
        'do': r'(do)[\w\W]+?while',
        'for': r'(for)\s*\(.*;.*;.*\)',
        'foreach': r'(foreach)\s*\(.\)',
        '?:': r'.+?.+:.+;'
        }


def foo(content, operand):
    pattern = data[operand]

    matches = re.findall(pattern, content)
    return matches


def find_operands():
    with open('example/example/Program.cs', 'r') as file:
        content = file.read()
    table = []
    for d in data.keys():
        table.append((d, len(foo(content, d))))
    return table