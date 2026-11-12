# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум, введенных чисел. Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»

summ = 0
count = 0
maximum = None
minimum = None

while True:
    number = int(input("Введите число: "))

    if number == 7:
        print("Good Bye!")
        break

    count += number
    if maximum is None or number > maximum:
        maximum = number
    if minimum is None or number < minimum:
        minimum = number

    if maximum is not None:
        print("Сумма чисел:", count)
        print("Максимум из чисел:", maximum)
        print("Минимум из чисел:", minimum)
    else:
        print("Вы не ввели ни одного числа")