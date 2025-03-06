using System;

namespace ComplexCodeExample
{
    class Program
    {
        static void Main(string[] args)
        {
            // Инициализация переменных
            int a = 10;
            int b = 20;
            int c = a + b;
            int d = a * b;
            int e = b / a;
            int f = b % a;

            // Логические операции
            bool isGreater = a > b;
            bool isEqual = a == b;
            bool isNotEqual = a != b;
            bool logicalAnd = isGreater && isEqual;
            bool logicalOr = isGreater || isEqual;
            bool logicalNot = !isGreater;

            // Работа с массивами
            int[] numbers = { 1, 2, 3, 4, 5 };
            int[] copiedNumbers = new int[numbers.Length];
            Array.Copy(numbers, copiedNumbers, numbers.Length);

            // Работа со строками
            string hello = "Hello";
            string world = "World";
            string helloWorld = hello + " " + world;
            string substring = helloWorld.Substring(0, 5);

            // Циклы
            for (int i = 0; i < numbers.Length; i++)
            {
                Console.WriteLine($"Number[{i}] = {numbers[i]}");
            }

            int counter = 0;
            while (counter < 5)
            {
                Console.WriteLine($"Counter: {counter}");
                counter++;
            }

            do
            {
                Console.WriteLine($"Counter: {counter}");
                counter--;
            } while (counter > 0);

            // Условия
            if (a > b)
            {
                Console.WriteLine("a is greater than b");
            }
            else if (a < b)
            {
                Console.WriteLine("a is less than b");
            }
            else
            {
                Console.WriteLine("a is equal to b");
            }

            // Switch-case
            switch (a)
            {
                case 10:
                    Console.WriteLine("a is 10");
                    break;
                case 20:
                    Console.WriteLine("a is 20");
                    break;
                default:
                    Console.WriteLine("a is neither 10 nor 20");
                    break;
            }

            // Методы
            int sum = AddNumbers(a, b);
            Console.WriteLine($"Sum of {a} and {b} is {sum}");

            // Классы и объекты
            Person person = new Person("John", 30);
            person.Introduce();

            // Работа с исключениями
            try
            {
                int zero = 0;
                int result = a / zero;
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine($"Exception caught: {ex.Message}");
            }
            finally
            {
                Console.WriteLine("Finally block executed");
            }

            // Лямбда-выражения
            Func<int, int, int> multiply = (x, y) => x * y;
            int product = multiply(a, b);
            Console.WriteLine($"Product of {a} and {b} is {product}");

            // Работа с коллекциями
            System.Collections.Generic.List<int> numberList = new System.Collections.Generic.List<int> { 1, 2, 3, 4, 5 };
            numberList.Add(6);
            numberList.RemoveAt(0);

            foreach (var number in numberList)
            {
                Console.WriteLine($"Number: {number}");
            }

            // Работа с делегатами
            Action<string> printMessage = (message) => Console.WriteLine(message);
            printMessage("Hello from delegate!");

            // Работа с событиями
            EventExample eventExample = new EventExample();
            eventExample.OnEvent += (sender, e) => Console.WriteLine("Event triggered!");
            eventExample.TriggerEvent();

            // Работа с LINQ
            var evenNumbers = from num in numberList
                              where num % 2 == 0
                              select num;

            foreach (var num in evenNumbers)
            {
                Console.WriteLine($"Even number: {num}");
            }

            // Работа с анонимными типами
            var anonymousType = new { Name = "Alice", Age = 25 };
            Console.WriteLine($"Anonymous type: Name = {anonymousType.Name}, Age = {anonymousType.Age}");

            // Работа с nullable типами
            int? nullableInt = null;
            if (nullableInt.HasValue)
            {
                Console.WriteLine($"Nullable int has value: {nullableInt.Value}");
            }
            else
            {
                Console.WriteLine("Nullable int is null");
            }

            // Работа с кортежами
            (string, int) tuple = ("Bob", 40);
            Console.WriteLine($"Tuple: Name = {tuple.Item1}, Age = {tuple.Item2}");

            // Работа с динамическими типами
            dynamic dynamicVar = "This is a string";
            Console.WriteLine($"Dynamic variable: {dynamicVar}");
            dynamicVar = 42;
            Console.WriteLine($"Dynamic variable: {dynamicVar}");

            // Работа с рефлексией
            Type type = typeof(Person);
            Console.WriteLine($"Type of Person: {type.Name}");

            // Работа с атрибутами
            var attributes = type.GetCustomAttributes(false);
            foreach (var attr in attributes)
            {
                Console.WriteLine($"Attribute: {attr}");
            }

            // Работа с потоками
            System.Threading.Thread thread = new System.Threading.Thread(() => Console.WriteLine("Hello from another thread!"));
            thread.Start();
            thread.Join();

            // Работа с асинхронными методами
            AsyncMethod().Wait();

            Console.WriteLine("Program finished.");
        }

        static int AddNumbers(int x, int y)
        {
            return x + y;
        }

        static async System.Threading.Tasks.Task AsyncMethod()
        {
            await System.Threading.Tasks.Task.Delay(1000);
            Console.WriteLine("Async method completed.");
        }
    }

    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }

        public Person(string name, int age)
        {
            Name = name;
            Age = age;
        }

        public void Introduce()
        {
            Console.WriteLine($"Hello, my name is {Name} and I am {Age} years old.");
        }
    }

    class EventExample
    {
        public event EventHandler OnEvent;

        public void TriggerEvent()
        {
            OnEvent?.Invoke(this, EventArgs.Empty);
        }
    }
}