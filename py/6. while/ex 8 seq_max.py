# Максимум последовательности
# Последовательность состоит из натуральных чисел 
# и завершается числом 0. Определите значение 
# наибольшего элемента последовательности.

max = 0
n = 0

while True:
    n = int(input()) 
    if n == 0:
        break
    if max == 0:
        max = n
    elif max < n:
        max = n

print(max)