# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернут.

import random

list = []
n = int(input("Колличество монет: "))
for i in range(n):
    list.append(random.randint(0, 1))
print(list)
count_1 = 0
count_2 = 0
for i in list:
    if i == 1:
        count_1 += 1
    else:
        count_2 +=1
if count_1 > count_2:
    print(count_2)
else:
    print(count_1)
