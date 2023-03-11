# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random
array = []
for i in range(5):
    array.append(random.randint(1 , 5))
print(array)

num_min = min(array)
num_max = max(array)
result = [num_min if i == num_max or i == num_max -1 else i for i in array]
print(result)