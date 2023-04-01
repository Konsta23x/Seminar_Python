# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

count = 2
fibo_n = int(input('Input Fibonacci number: '))
a = 0
b = 1


while fibo_n >= b:
    if fibo_n == b:
        print(count)
        break
    a, b = b, a + b
    count += 1
else:
    print(-1)
