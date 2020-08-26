# Количество различных элементов
# Дан список, упорядоченный по неубыванию элементов 
# в нем. Определите, сколько в нем различных элементов.

a_list = [int(i) for i in input().split()]

count_distinct = 0
distinct_el = []

for i in a_list:
    if i not in distinct_el:
        distinct_el.append(i)

print(len(distinct_el))