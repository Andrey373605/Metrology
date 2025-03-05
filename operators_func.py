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
        '?:': r'.+?.+:.+;',
        }


def foo(content, operand):
    pattern = data[operand]

    matches = re.findall(pattern, content)
    return matches


def find_operators(cs_code):
    table = {}
    for d in data.keys():
        table[d] = len(foo(cs_code, d))

    find_branches(table, cs_code)
    return table.items()


def find_branches(table, cs_code):
    pattern = r'\([^()]+\)'
    matches = len(re.findall(pattern, cs_code))
    count = matches - table['if'] - table['do'] - table['while'] - table['for'] - table['foreach']
    table['()'] = count

