# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

n = int(input('Введите размер 1 списка: '))
list_n = [random.randint(1,10) for _ in range(n)]
print(list_n)

m = int(input('Введите размер 2 списка: '))
list_m = [random.randint(1,10) for _ in range(m)]
print(list_m)

set_n, set_m  = set(list_n), set(list_m)

print(set_n, set_m, sep='\n')

print(*set_n.intersection(set_m))
