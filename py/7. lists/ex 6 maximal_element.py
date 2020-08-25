# Наибольший элемент
# Дан список чисел. Выведите значение наибольшего 
# элемента в списке, а затем индекс этого элемента 
# в списке. Если наибольших элементов несколько, 
# выведите индекс первого из них.

a_list = [int(i) for i in input().split()]

max_a_list = max(a_list)
max_pos = -1

for i in range(len(a_list)):
    if a_list[i] == max_a_list:
        max_pos = i
        break

print(max_a_list, max_pos, sep=' ')