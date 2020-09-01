# Шахматная доска
# Даны два числа n и m. Создайте двумерный массив 
# размером # n×m и заполните его символами "." и 
# "*" в шахматном порядке. В левом верхнем углу 
# должна стоять точка.

n, m = [int(i) for i in input().split()]

l_list = [['*' for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            l_list[i][j] = '.'

for row in l_list:
    print(' '.join([str(elem) for elem in row]))