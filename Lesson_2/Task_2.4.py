# Иван Васильевич пришел на рынок и решил купить
# два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза

N = int(input("Введите число: "))
mi = 1000
ma = 0
for i in range(N):
    massa = int(input("Введите массу: "))
    if massa >= ma:
        ma = massa
    if massa <= mi:
        mi = massa
print(mi, ma)
