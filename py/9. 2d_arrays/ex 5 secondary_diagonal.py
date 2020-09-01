# Побочная диагональ
# Дано число n. Создайте массив размером n×n и заполните 
# его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый 
# нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке 
# разделяйте одним пробелом.

def diag(n):
    n_list = []
    for i in range(n):
        n_list.append([])
        for j in range(n):
            if i + j < n - 1:
                n_list[i].append(0)
            elif i + j == n - 1:
                n_list[i].append(1)
            elif i + j > n - 1:
                n_list[i].append(2)
    return n_list

n_list = diag(int(input()))
for row in n_list:
    print(' '.join([str(elem) for elem in row]))