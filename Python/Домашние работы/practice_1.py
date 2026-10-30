# создание списка
list1 = [123, "hello", True, 342, [1231]]
list2 = [] # пустой список
list3 = list() # пустой список
list4 = list("hello") # создание списка из строки
list5= list(range(1, 10)) # создание списка из диапазона 

# вывод списка
print(list1)
print(list4)
print(list5)

# перебор с помощью цикла
for element in list1:
    print(element)
    
# индексация списков
list1 = [123, "hello", True, 342, [1231]]
print(list1[0])
print(list1[0:3])
list1[0] = "world"
print(list1[0])

# методы
list5 = list(range(1, 5))

# добавление
list5.append(20) # добавление в конец
print(list5)

added_list = [1, 5]
# list5.extend(added_list) # добавление списка
list5 += added_list # добавление списка
print(list5)

list5.insert(0, "new") # добавить элемент под индекс
print(list5)

# удаление
list5.remove("new") # удалить по значению
print(list5)
list5.pop(0) # удалить по индексу
print(list5)

list5.reverse() # разворот
print(list5)

list5.sort() # сортировка
print(list5)

x = list5.count(1) # количество элементов со значением 1
print(x)

i = list5.index(20) # индекс элемента в списке
print(i)

list5.clear() # очистка списка
print(list5)

list5 = list(range(1, 5))
m = max(list5)
m1 = min(list5)
s = sum(list5)
l = len(list5)

print("максимум", m)
print("минимум", m1)
print("сумма", s)
print("длина", l)