# Диагонали, параллельные главной
# Дано число n. Создайте массив размером n×n и 
# заполните его по следующему правилу. На главной 
# диагонали должны быть записаны числа 0. На двух 
# диагоналях, прилегающих к главной, числа 1. На 
# следующих двух диагоналях числа 2, и т.д.

def diag(n):
    n_list = []
    for i in range(n):
        n_list.append([])
        for j in range(n):
            n_list[i].append(abs(i - j))
    return n_list

n_list = diag(int(input()))
for row in n_list:
    print(' '.join([str(elem) for elem in row]))