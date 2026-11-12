# Пользователь вводит с клавиатуры два числа. Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    start, end = end, start

sum_even = 0
sum_odd = 0
sum_nine = 0

count_even = 0
count_odd = 0
count_nine = 0

for i in range(start, end+1):
    if i % 2 == 0:
        sum_even += i
        count_even += 1
    else:
        sum_odd += i
        count_odd += 1

    if i % 9 == 0:
        sum_nine += i
        count_nine += 1

if count_even > 0:
    avg_even = sum_even / count_even
else:
    avg_even = 0

if count_odd > 0:
    avg_odd = sum_odd / count_odd
else:
    avg_odd = 0

if count_nine > 0:
    avg_nine = sum_nine / count_nine
else:
    avg_nine = 0

print("Сумма чётных чисел:", sum_even, "Среднее арифметическое:", avg_even)
print("Сумма нечётных чисел:", sum_odd, "Среднее арифметическое:", avg_odd)
print("Сумма чисел кратных 9:", sum_nine, "Среднее арифметическое:", avg_nine)