# Яша плавает в бассейне
# Яша плавал в бассейне размером N × M метров и устал. 
# В этот момент он обнаружил, что находится на расстоянии 
# x метров от одного из длинных бортиков (не обязательно 
# от ближайшего) и y метров от одного из коротких бортиков. 
# Какое минимальное расстояние должен проплыть Яша, чтобы 
# выбраться из бассейна на бортик? Программа получает на 
# вход числа N, M, x, y. Программа должна вывести число 
# метров, которое нужно проплыть Яше до бортика.

N = int(input())
M = int(input())

x = int(input())
y = int(input())

if N >= M: # если N - длинный бортик, а M - короткий
    min1 = min(x, y, M - x, N - y)
elif N <= M:
    min1 = min(x, y, N - x, M - y)

print(str(min1))