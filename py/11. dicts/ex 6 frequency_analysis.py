# Частотный анализ
# Дан текст: в первой строке записано количество строк 
# в тексте, а затем сами строки. Выведите все слова, 
# встречающиеся в тексте, по одному на каждую строку. 
# Слова должны быть отсортированы по убыванию их 
# количества появления в тексте, а при одинаковой 
# частоте появления — в лексикографическом порядке.
# Указание. После того, как вы создадите словарь 
# всех слов, вам захочется отсортировать его по 
# частоте встречаемости слова. Желаемого можно 
# добиться, если создать список, элементами которого 
# будут кортежи из двух элементов: частота встречаемости 
# слова и само слово. Например, [(2, 'hi'), (1, 'what'), 
# (3, 'is')]. Тогда стандартная сортировка будет 
# сортировать список кортежей, при этом кортежи 
# сравниваются по первому элементу, а если они равны — 
# то по второму. Это почти то, что требуется в задаче.

count_str = int(input())
words_dict = dict()

for i in range(count_str):
    string = [str(i) for i in input().split()]
    for j in string:
        if j in words_dict:
            words_dict[j] = words_dict[j] + 1
        else:
            words_dict[j] = 1

words_list = list()

for i in words_dict.keys():
    words_list.append([words_dict[i], i])

words_list.sort(reverse=True)

for i in words_list:
    print(i[1])