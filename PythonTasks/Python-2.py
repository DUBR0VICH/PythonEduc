string = input("Введите строку: ")
length = len(string)

for i in range(length):
    if i == 2:  # Пропускаем 3-й символ
        continue
    elif string[i] == "c":  # Если есть символ "c", выводим сообщение
        print("В строке есть символ 'c'!")
    print(string[i], end="")  # Выводим символ без перевода строки

print("\nДлина строки:", length)
print("Строка без последнего символа:", string[:-1])
