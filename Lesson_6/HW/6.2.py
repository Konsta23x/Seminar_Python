# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [1, 3, -5, 19, 4, 9, -5, -19, 7, 3, 5, 2, 10, 30, 43, -15]
min_number= int(input('Введите минимальное значение: '))
max_number= int(input('Введите максимальное значение: '))
list_2=[]
for i in range(len(list_1)):
    if min_number< list_1[i]<max_number:
        list_2.append(list_1[i])
print(list_2)
list_2.sort()
print(list_2)