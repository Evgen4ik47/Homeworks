days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
    day = int(input("Введите день недели (от 1 до 7): "))

    if 1 <= day <= 7:
        print(days[day - 1])
    else:
        raise IndexError

except ValueError:
    print("Ошибка: нужно ввести число")

except IndexError:
    print('Ошибка: число вне диапазона')