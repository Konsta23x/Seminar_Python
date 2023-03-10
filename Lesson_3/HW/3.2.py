# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
list = []
n = int(input('Введите длину массива: '))
for i in range(n):
    list.append(random.randint(1, n))
print(list)

X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(X - list[0])
index = 0
for i in range(1, n):
        count = abs(X - list[i])
        if count < min:
            min = count 
            index = i
print(f'Число {list[index]} в списке list наиболее близко по величине к числу {X}, их разница составляет {abs(X - list[index])}')
        