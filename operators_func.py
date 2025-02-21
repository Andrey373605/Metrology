import re

data = {'+': r'[^+][+][^+=]',
        '-': r'[^-][-][^-=]',
        '*': r'[^*][*][^*=]',
        '/': r'[^/][/][^/=]',
        '%': r'[^%][%][^%=]',
        '|': r'[^|][|][^|]',
        '^': r'^[|][^|]',
        '>': r'[>][^=]',
        '<': r'[<][^=]',
        '>=': r'>=',
        '<=': r'<=',
        '==': r'==',
        '!=': r'!=',
        ';': r';',
        '=': r'[^=+-/*%<>]=[^=]', }


def foo():
    pattern = data[';']
    string = '''
using System;

class Program
{
    static void Main()
    {
        int width = 10;
        int height = 5;
        int a = (width != height);

        int area = width * height;
        int perimeter = 2 * (width + height);

        width++;
        height--;

        bool isSquare = (width == height);
        bool isLarge = (area > 50);

        bool isWidthGreater = width > height;
        bool isHeightLessOrEqual = height <= 5;

        int bitwiseAnd = width & height;
        int bitwiseOr = width | height;
        int bitwiseXor = width ^ height;
        int bitwiseNot = ~width;

        int result = 0;
        result += area; 
        result -= perimeter; 
        result *= 2; 
        result /= 3; 
        result %= 5; 
        
        int a = 4;
        int b = a + 3;
        int b = a - 4;
        int b = a * 3;
        int b = a / 2;
        int b = a % 2;


        string sizeDescription = (area > 50) ? "a" : "b";
    }
}
    '''

    matches = re.findall(pattern, string)
    print(len(matches))


foo()
