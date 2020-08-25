# Больше своих соседей
# Дан список чисел. Определите, сколько в этом 
# списке элементов, которые больше двух своих 
# соседей, и выведите количество таких элементов. 
# Крайние элементы списка никогда не учитываются, 
# поскольку у них недостаточно соседей.

a_list = [int (i) for i in input().split()]

count = 0

for i in range(1, len(a_list) - 1):
    if a_list[i] > a_list[i - 1] and a_list[i] > a_list[i + 1]:
        count += 1

print(count)