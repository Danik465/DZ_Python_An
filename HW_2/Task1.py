from random import  randint
# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
# Пример:
#
# 5 -> 1 0 1 1 0
# 2

n = int(input("Введите количенство монеток на столе: \n"))
lst = list()

count = 0
for i in range(0, n):
    lst.append(randint(0, 1))
    if lst[i] == 0:
        count += 1

print(count)
print(lst)