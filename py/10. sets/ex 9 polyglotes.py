# Полиглоты
# Каждый из некоторого множества школьников некоторой 
# школы знает некоторое количество языков. Нужно 
# определить сколько языков знают все школьники, и 
# сколько языков знает хотя бы один из школьников.
# В первой строке задано количество школьников. Для 
# каждого из школьников сперва записано количество 
# языков, которое он знает, а затем - названия языков, 
# по одному в строке.
# В первой строке выведите количество языков, которые 
# знают все школьники. Начиная со второй строки - 
# список таких языков. Затем - количество языков, 
# которые знает хотя бы один школьник, на следующих 
# строках - список таких языков. Языки нужно выводить 
# в лексикографическом порядке, по одному на строке.

students_count = int(input())
all_know_lang_mas = []
one_know_lang_mas = []
one_know_lang = set()

for i in range(students_count):
    count_lang_stud = int(input())
    temp_list = set()
    for j in range(count_lang_stud):
        temp = str(input())
        temp_mas = []
        temp_mas.append(temp)
        temp_list.update(temp_mas)

        if temp not in all_know_lang_mas:
            all_know_lang_mas.append(temp)

    if i == 0:
        one_know_lang.update(temp_list)
    else:
        one_know_lang = one_know_lang & temp_list

all_know_lang_mas.sort()
one_know_lang_mas = [str(i) for i in one_know_lang]
one_know_lang_mas.sort()

print(len(one_know_lang_mas))
print(' '.join([str(i) for i in one_know_lang_mas]))
print(len(all_know_lang_mas))
print(' '.join([str(i) for i in all_know_lang_mas]))