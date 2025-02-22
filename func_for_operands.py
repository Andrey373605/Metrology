import re
from collections import Counter


def find_operands(csharp_code):
    pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b|-?\d+\.?\d*'

    matches = re.findall(pattern, csharp_code)

    keywords = {
        "int", "float", "double", "var", "string", "bool", "char", "if", "else",
        "while", "for", "foreach", "switch", "case", "default", "break", "continue",
        "return", "public", "private", "protected", "static", "void", "class",
        "using", "namespace", "new", "true", "false", "null", "this", "base", "WriteLine",
        "Console", "is", "as"
    }

    filtered_operands = [match for match in matches if match not in keywords]

    operand_counts = Counter(filtered_operands)

    result = list(operand_counts.items())

    return result


csharp_code1 = """
int x = 10;
double y = 5.5;
var result = x + y * z;
if (result > threshold) {
    Console.WriteLine("Success");
}
"""
operands1 = find_operands(csharp_code1)
print("Операнд/кол-во повторений:", operands1)




