try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    result = num1 / num2
    print(result)

except ValueError:
    print("Ошибка: введите два целых числа")

except ZeroDivisionError:
    print("Ошибка: деление на ноль")
