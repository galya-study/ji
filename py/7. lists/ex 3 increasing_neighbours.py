# Больше предыдущего
# Дан список чисел. Выведите все элементы 
# списка, которые больше предыдущего элемента.

a_list = input().split()

for i in range(len(a_list) - 1):
    if a_list[i + 1] > a_list[i]:
        print(a_list[i + 1])