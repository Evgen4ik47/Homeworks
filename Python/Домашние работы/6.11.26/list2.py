import random

original_list = []
for i in range(10):
    original_list.append(random.randint(-10, 10))
    
print("Первый список:", original_list)

even_list = []
odd_list = []
negative_list = []
positive_list = []

for j in original_list:
    if j % 2 == 0:
        even_list.append(j)
    else:
        odd_list.append(j)
        
    if j < 0:
        negative_list.append(j)
    elif j > 0:
        positive_list.append(j)
    
print("1. Список с четными числами:", even_list)
print("2. Список с нечетными числами:", odd_list)
print("3. Список с отрицательными числами:", negative_list)
print("4. Список с положительными числами:", positive_list)