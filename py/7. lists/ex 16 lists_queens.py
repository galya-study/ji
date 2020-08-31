# Ферзи
# Известно, что на доске 8×8 можно расставить 
# 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, 
# определите, есть ли среди них пара бьющих 
# друг друга.
# Программа получает на вход восемь пар чисел, 
# каждое число от 1 до 8 — координаты 8 ферзей. 
# Если ферзи не бьют друг друга, выведите слово 
# NO, иначе выведите YES.

col_list = []
line_list = []
f = 'NO'

for i in range(8):
    col, line = [int(i) for i in input().split()]
    col_list.append(col)
    line_list.append(line)

for i in range(8):
    for j in range(8):
        if i != j and (col_list[i] == col_list[j] or line_list[i] == line_list[j]):
            f = 'YES'
        elif i != j and (abs(col_list[i] - col_list[j]) == abs(line_list[i] - line_list[j])):
            f = 'YES'

print(f)