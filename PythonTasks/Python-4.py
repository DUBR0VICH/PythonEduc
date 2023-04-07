import math
import random

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Деление на ноль недопустимо!")
        return None
    else:
        return x / y

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

def rand(x, y):
    return random.randint(x, y)

def factorial(x):
    if x < 0:
        print("Факториал отрицательного числа не определен!")
        return None
    elif x == 0:
        return 1
    else:
        return x * factorial(x-1)

def arccos(x):
    if x > 1 or x < -1:
        print("Арккосинус не определен вне интервала [-1, 1]!")
        return None
    else:
        return math.acos(x)

while True:
    print("Выберите операцию.")
    print("+")
    print("-")
    print("*")
    print("/")
    print("^")
    print("%")
    print("rand")
    print("!")
    print("arccos")

    operation = input()

    if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "^" or operation == "%" or operation == "rand":
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))

        if operation == "+":
            print(x, "+", y, "=", add(x, y))

        elif operation == "-":
            print(x, "-", y, "=", subtract(x, y))

        elif operation == "*":
            print(x, "*", y, "=", multiply(x, y))

        elif operation == "/":
            result = divide(x, y)
            if result is not None:
                print(x, "/", y, "=", result)

        elif operation == "^":
            print(x, "^", y, "=", power(x, y))

        elif operation == "%":
            print(x, "%", y, "=", mod(x, y))

        elif operation == "rand":
            print("Случайное число в интервале [", x, ",", y, "] =", rand(x, y))

    elif operation == "!":
        x = int(input("Введите число: "))
        print(x, "! =", factorial(x))

    elif operation == "arccos":
        x = float(input("Введите число: "))
        print("arccos(", x, ") =", arccos(x))

    else:
        print("Операция не распознана!")
