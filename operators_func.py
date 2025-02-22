import re

data = {'+': r'[^+]([+])[^+=]',
        '-': r'[^-]([-])[^-=]',
        '*': r'[^*]([*])[^*=]',
        '/': r'[^/]([/])[^/=]',
        '%': r'[^%]([%])[^%=]',
        '|': r'[^|]([|])[^|]',
        '||': r'(||)',
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
        'if': r'if\s+\(.+\)[^{]+\{[^{]+\}'
        }


def foo():
    pattern = data['if']
    with open('example_code/example/example/Program.cs', 'r') as file:
        content = file.read()

    matches = re.findall(pattern, content)
    for m in matches:
        print(m)
