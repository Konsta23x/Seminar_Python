# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

li = []
user_in = (int(input("Input a number: ")))

def sum_dev(num):
    cou = 1
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            cou += i + num / i
    return cou

for j in range(10, user_in):
    first = sum_dev(j)
    second = sum_dev(first)
    if second == j and first < second:
        print(j, first)