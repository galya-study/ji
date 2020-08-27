# Переставить соседние
# Переставьте соседние элементы списка (A[0] c A[1], 
# A[2] c A[3] и т. д.). Если элементов нечетное число, 
# то последний элемент остается на своем месте.

a_list = [int(i) for i in input().split()]
a_new_list = []

for i in range(0, len(a_list), 2):
    if i != len(a_list) - 1:
        a_new_list.append(a_list[i + 1])
    a_new_list.append(a_list[i])

for i in a_new_list:
    print(i, end=' ')