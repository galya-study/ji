# Соседи одного знака
# Дан список чисел. Если в нем есть два соседних 
# элемента одного знака, выведите эти числа. Если 
# соседних элементов одного знака нет — не выводите 
# ничего. Если таких пар соседей несколько — выведите 
# первую пару.

a_list = [int(i) for i in input().split()]

for i in range(len(a_list) - 1):
    if a_list[i + 1] > 0 and a_list[i] > 0:
        print(a_list[i], a_list[i + 1], sep=' ')
        break
    elif a_list[i + 1] < 0 and a_list[i] < 0:
        print(a_list[i], a_list[i + 1], sep=' ')
        break