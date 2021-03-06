# Шахматная доска
# Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а 
# если в разные цвета — то NO. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

col1 = int(input())
line1 = int(input())

col2 = int(input())
line2 = int(input())

cell1 = (col1 + line1) % 2
cell2 = (col2 + line2) % 2

if cell1 == cell2:
    print('YES')
else:
    print('NO')