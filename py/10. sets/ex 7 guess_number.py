# Угадай число
# Август и Беатриса играют в игру. Август загадал 
# натуральное число от 1 до n. Беатриса пытается 
# угадать это число, для этого она называет некоторые 
# множества натуральных чисел. Август отвечает 
# Беатрисе YES, если среди названных ей чисел есть 
# задуманное или NO в противном случае. После 
# нескольких заданныъх вопросов Беатриса запуталась 
# в том, какие вопросы она задавала и какие ответы 
# получила и просит вас помочь ей определить, какие 
# числа мог задумать Август.
# В первой строке задано n - максимальное число, 
# которое мог загадать Август. Далее каждая строка 
# содержит вопрос Беатрисы (множество чисел, разделенных 
# пробелом) и ответ Августа на этот вопрос.
# Вы должны вывести через пробел, в порядке возрастания, 
# все числа, которые мог задумать Август.

# это какой-то бред, а не задача -_-
n = int(input())

yes_set = set()
no_set = set()

num = input()
while num != 'HELP':
    if input() == 'YES':
        yes_set_temp = set()
        yes_set_temp.update([str(i) for i in num.split()])
        if len(yes_set) == 0:
            yes_set = yes_set_temp
        else:
            yes_set = yes_set_temp & yes_set
    else:
        no_set.update([str(i) for i in num.split()])
    num = input()

res_set = yes_set - (yes_set & no_set)

for i in res_set:
    print(i, end=' ')