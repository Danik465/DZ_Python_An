# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

lst = [a]

for i in range(1,n):
    lst.append(a+i*d)

print(lst)