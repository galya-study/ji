# Ход слона
# Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, 
# определите, может ли слон попасть с первой клетки на вторую одним ходом.

col1 = int(input()) # первая клетка
line1 = int(input()) # первая клетка

col2 = int(input()) # вторая клетка
line2 = int(input()) # вторая клетка

if (col1 + line1) == (col2 + line2):
    print('YES')
elif (col1 / line1) == (col2 / line2):
    print('YES')
elif (col1 - col2) == (line1 - line2):
    print('YES')
else:
    print('NO')