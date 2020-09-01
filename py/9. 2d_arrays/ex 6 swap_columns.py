# Поменять столбцы
# Дан двумерный массив и два числа: i и j. Поменяйте в 
# массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, 
# затем элементы массива, затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j).

def swap_columns(a, i, j):
    for z in range(len(a)):
        for x in range(len(a[z])):
            if x == i:
                a[z][i], a[z][j] = a[z][j], a[z][i]
            
    return a

n, m = [int(i) for i in input().split()]
a_list = []
for i in range(n):
    a_list.append([int(j) for j in input().split()])

i, j = [int(a) for a in input().split()]

a_list = swap_columns(a_list, i, j)
for row in a_list:
    print(' '.join([str(elem) for elem in row]))