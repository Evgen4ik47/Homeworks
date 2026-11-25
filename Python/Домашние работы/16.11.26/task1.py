import random

list1 = [random.randint(1, 10) for i in range(10)]
list2 = [random.randint(1, 10) for i in range(10)]

list_combined = list1 + list2
list_no_repeats = list1 + list2
list_repeats = list1 + list2
list_uniques = list1 + list2
list_min_max = [min(list1), max(list1), min(list2), max(list2)]

for i in range(len(list_no_repeats) - 1, -1, -1):
    if list_no_repeats[i] in list_no_repeats[:i]:
        list_no_repeats.pop(i)

for i in range(len(list_repeats) - 1, -1, -1):
    if (list_repeats[i] not in list1) or (list_repeats[i] not in list2) or (list_repeats[i] in list_repeats[:i]):
        list_repeats.pop(i)

for i in range(len(list_uniques) - 1, -1, -1):
    if (list_uniques[i] in list1 and list_uniques[i] in list2) or (list_uniques[i] in list_uniques[:i]):
        list_uniques.pop(i)


print(f"Список, содержащий элементы обоих списков: {list_combined}")
print(f"Список, содержащий элементы обоих списков без повторений: {list_no_repeats}")
print(f"Список, содержащий элементы общие для двух списков: {list_repeats}")
print(f"Список, содержащий только уникальные элементы для каждого из списков: {list_uniques}")
print(f"Список, содержащий только минимальное и максимальное значение каждого из списков: {list_min_max}")