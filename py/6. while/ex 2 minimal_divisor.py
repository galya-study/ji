# Минимальный делитель
# Дано целое число, не меньшее 2. Выведите 
# его наименьший натуральный делитель, отличный от 1.

n = int(input())

i = 2

while i <= n:
    if n % i == 0:
        print(i)
        break
    i += 1