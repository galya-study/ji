# Переставить min и max
# В списке все элементы различны. Поменяйте местами 
# минимальный и максимальный элемент этого списка.

a_list = [int(i) for i in input().split()]
min_el = min(a_list)
max_el = max(a_list)

min_pos = -1
max_pos = -1

for i in range(len(a_list)):
    if a_list[i] == max_el:
        max_pos = i
    elif a_list[i] == min_el:
        min_pos = i

a_list[max_pos], a_list[min_pos] = a_list[min_pos], a_list[max_pos]

for i in a_list:
    print(i, end=' ')