# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# Пример:
#
# 2 4
# 2



def rec_sum(a,b):
    if(a>b):
       return sum(a,b)
    return sum(b,a)
def sum(a,b):
    elem = a
    if b==0:
        return elem
    elem = sum(a+1, b-1)
    return elem


print(rec_sum(7,2))