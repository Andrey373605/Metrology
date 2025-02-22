import re
from collections import Counter


def find_operands(csharp_code):
    pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b|-?\d+\.?\d*'
    text_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b|//|\n'
    csharp_code = re.sub(r'//.*', '', csharp_code)
    csharp_code = re.sub(r'/\*.*?\*/', '', csharp_code, flags=re.DOTALL)
    csharp_code = re.sub(r'\bclass\s+([a-zA-Z_][a-zA-Z0-9_]*)', '', csharp_code)
    csharp_code = re.sub(r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*\(', '(', csharp_code)
    matches = re.findall(pattern, csharp_code)

    keywords = {
        "int", "float", "double", "var", "string", "bool", "char", "if", "else",
        "while", "for", "foreach", "switch", "case", "default", "break", "continue",
        "return", "public", "private", "protected", "static", "void", "class",
        "using", "namespace", "new", "true", "false", "null", "this", "base", "WriteLine",
        "Console", "is", "as", "Main", "goto", "do"
    }

    filtered_operands = [match for match in matches if match not in keywords]

    operand_counts = Counter(filtered_operands)

    result = list(operand_counts.items())

    return result


with open('example/example/Program.cs', 'r') as file:
    content = file.read()
print("Операнд/кол-во повторений:", find_operands(content))




