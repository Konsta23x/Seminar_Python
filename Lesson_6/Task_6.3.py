# Дан список чисел. Посчитайте,
# сколько в нем пар элементов,
# равных друг другу.

# Считается, что любые два элемента,
# равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел.
# Все числа списка находятся на разных строках.

li = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3, 3, 3]
sum = 0
for i in li:
    if li.count(i) > 1:
        if li.count(i) % 2 != 0:
            sum += (li.count(i) - 1) / 2
            li.pop(i)
        else:
            sum += li.count(i) / 2
        print(f'i = {li.count(i) / 2}, sum = {-(-sum// (4))}')