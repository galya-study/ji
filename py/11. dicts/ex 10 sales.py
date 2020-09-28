# Продажи
# Дана база данных о продажах некоторого интернет-магазина.
# Каждая строка входного файла представляет собой запись
# вида Покупатель товар количество, где Покупатель — имя
# покупателя (строка без пробелов), товар — название товара
# (строка без пробелов), количество — количество приобретенных
# единиц товара.
# Создайте список всех покупателей, а для каждого покупателя
# подсчитайте количество приобретенных им единиц каждого вида
# товаров. Список покупателей, а также список товаров для
# каждого покупателя нужно выводить в лексикографическом порядке.

from sys import stdin

all_mas = []

for line in stdin.readlines():
    buyer, buy, count = [str(i) for i in line.split()]
    flag = 0

    if len(all_mas) == 0:
        temp_dict = dict()
        temp_dict[buy] = int(count)

        temp_mas = [buyer, temp_dict]
        all_mas.append(temp_mas)
        flag = 1
    else:
        for i in range(len(all_mas)):
            if all_mas[i][0] == buyer:
                if buy in all_mas[i][1]:
                    all_mas[i][1][buy] = all_mas[i][1][buy] + int(count)
                else:
                    all_mas[i][1][buy] = int(count)
                flag = 1
                break

    if flag == 0:
        temp_dict = dict()
        temp_dict[buy] = int(count)

        temp_mas = [buyer, temp_dict]
        all_mas.append(temp_mas)

for i in all_mas:
    print(i[0], ':', sep='')
    temp_dict = i[1]
    for j in sorted(temp_dict.keys()):
        print(j, temp_dict[j], sep=' ')