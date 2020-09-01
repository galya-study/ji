# Снежинка
# Дано нечетное число n. Создайте двумерный массив 
# из n×n элементов, заполнив его символами "." 
# (каждый элемент массива является строкой из одного 
# символа). Затем заполните символами "*" среднюю 
# строку массива, средний столбец массива, главную 
# диагональ и побочную диагональ. В результате единицы 
# в массиве должны образовывать изображение звездочки. 
# Выведите полученный массив на экран, разделяя элементы 
# массива пробелами.

def snowflake(n):
    n_list = [['.' for i in range(n)] for j in range(n)]
    mid_pos = n // 2
    row_index = 0
    column_index = n - 1

    for i in range(n):
        n_list[i][i] = '*'
        n_list[i][mid_pos] = '*'
        n_list[mid_pos][i] = '*'

        n_list[row_index][column_index] = '*'
        row_index += 1
        column_index -= 1

    return n_list

n = snowflake(int(input()))
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j], end=' ')
    print()