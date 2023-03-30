string = input("Введите строку: ")
length = len(string)

for i in range(length):
    if i == 2:
        continue
    elif string[i] == "c":
        print("В строке есть символ 'c'!")
    print(string[i], end="")

print("\nДлина строки:", length)
print("Строка без последнего символа:", string[:-1])
