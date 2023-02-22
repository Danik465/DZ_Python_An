# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

max_el = 10
min_el = 1
n = int(input("Введите количество элементов: "))
lst = [randint(1,randint(1,10)) for i in range(n)]
print(lst)

lst_index = []
for i in range(len(lst)):
    if lst[i] >= min_el and lst[i]<= max_el:
        lst_index.append(i)
print(lst_index)
