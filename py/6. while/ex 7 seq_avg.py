# Среднее значение последовательности
# Определите среднее значение всех элементов 
# последовательности, завершающейся числом 0.

count = 0
sum = 0
avg = 0
n = 0

while True:
    n = int(input()) 
    if n == 0:
        break
    sum += n
    count += 1

avg = sum / count

print(avg)