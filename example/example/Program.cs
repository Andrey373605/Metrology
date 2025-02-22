using System;

class Program
{
    static void Main()
    {
        int width = 10;
        int height = 5;
        bool check = (width != height);

        int area = width * height;
        int perimeter = 2 * (width + height);

        width++;
        height--;
        //Hello world youoopppppp

        /*

        rfej
        sssoooooooooosiiiiiiiiiiiiiiiiii

        ffjfjffj
        */
        bool w1 = width > height;
        bool w2 = height <= 5;
        bool w3 = width >= height;
        bool w4 = width < height;
        bool w5 = width == height;
        bool w6 = width != height;
        bool w7 = w1 && w2;
        bool w8 = w1  w2;

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

        int a = 7, b = 3;
        int c;
        c = a + b;
        c = a - b;
        c = a * b;
        c = a / b;
        c = a % b;
        c = a | b;
        c = a & b;
        c = a >> b;
        c = a << b;
        c = a ^ b;
        c = ~a;

        if (c > b && c < a)
        {
            c = a;
        }
        else if (c < b || c > a)
        {
            c = b;
        }
        else
        {
            c = 0;
        }

        do
        {
            c--;
            continue;
        } while (c > 0);

        while (c < 10)
        {
            c++;
            break;
        }

        goto jump;

    jump:

        object f = "A";
        string g = f as string;

        if (g is int)
        {
            a += b;
        }

        string sizeDescription = (area > 50) ? "a" : "b";
    }
}