# Максимум
# Найдите индексы первого вхождения максимального 
# элемента. Выведите два числа: номер строки и 
# номер столбца, в которых стоит наибольший элемент 
# в двумерном массиве. Если таких элементов несколько, 
# то выводится тот, у которого меньше номер строки, 
# а если номера строк равны то тот, у которого меньше 
# номер столбца.
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.

n, m = [int(i) for i in input().split()]
a_list = []
for i in range(n):
    a_list.append([int(j) for j in input().split()])

max_value = a_list[0][0]
max_n = 0
max_m = 0

for i in range(n):
    for j in range(m):
        if a_list[i][j] > max_value:
            max_value = a_list[i][j]
            max_n = i
            max_m = j
        elif a_list[i][j] == max_value:
            if max_n > i:
                max_n = i
                max_m = j
            elif max_n == i and max_m > j:
                max_n = i
                max_m = j

print(max_n, max_m, sep=' ')