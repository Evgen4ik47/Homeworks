try:
    num = int(input("Введите число: "))

    num = num * num

    print(num)

except ValueError:
    print("Ошибка: нужно ввести число")