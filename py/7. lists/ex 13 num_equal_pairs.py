# Количество совпадающих пар
# Дан список чисел. Посчитайте, сколько в нем пар 
# элементов, равных друг другу. Считается, что 
# любые два элемента, равные друг другу образуют 
# одну пару, которую необходимо посчитать.

a_list = [int(i) for i in input().split()]
count = 0

for i in range(0, len(a_list)):
    for j in range(0, len(a_list)):
        if i != j and a_list[i] == a_list[j]:
            count += 1
count /= 2

print(count)