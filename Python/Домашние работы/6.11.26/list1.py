import random

list1 = []
for i in range(10):
    list1.append(random.randint(-10, 10))
    
print("Список:", list1)

negatives = []
evens = []
odds = []

for j in list1:
    if j < 0:
        negatives.append(j)
    if j % 2 == 0:
        evens.append(j)
    else:
        odds.append(j)
        
negative_sum = sum(negatives)
even_sum = sum(evens)
odd_sum = sum(odds)

index3 = 1
for i in range(0, len(list1), 3):
    index3 *= list1[i]
    
min_value = min(list1)
max_value = max(list1)
min_index = list1.index(min_value)
max_index = list1.index(max_value)

start = min(min_index, max_index)
end = max(min_index, max_index)

between = 1
for i in range(start + 1, end):
    between *= list1[i]
    
if start + 1 == end:
    between = 0
    
first_index_pos = -1
last_index_pos = -1
for i in range(len(list1)):
    if list1[i] > 0:
        first_index_pos = i
        break
    
for i in range(len(list1) - 1, -1, -1):
    if list1[i] > 0:
        last_index_pos = i
        break
    
between_pos_sum = 0
if first_index_pos != -1 and last_index_pos != -1 and first_index_pos < last_index_pos:
    slice = list1[first_index_pos + 1 : last_index_pos]
    between_pos_sum = sum(slice)
    
print("1. Сумма отрицательных:", negative_sum)
print("2. Сумма четных:", even_sum)
print("3. Сумма нечетных:", odd_sum)
print("4. Произведение индексов кратных 3:", index3)
print("5. Произведение между минимальным и максимальным:", between)
print("6. Сумма между положительными:", between_pos_sum)