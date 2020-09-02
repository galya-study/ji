# Кубики
# Аня и Боря любят играть в разноцветные кубики, причем 
# у каждого из них свой набор и в каждом наборе все 
# кубики различны по цвету. Однажды дети заинтересовались, 
# сколько существуют цветов таких, что кубики каждого 
# цвета присутствуют в обоих наборах. Для этого они 
# занумеровали все цвета случайными числами от 0 до 108. 
# На этом их энтузиазм иссяк, поэтому вам предлагается 
# помочь им в оставшейся части.
# В первой строке входных данных записаны числа N и M — 
# число кубиков у Ани и Бори. В следующих N строках заданы 
# номера цветов кубиков Ани. В последних M строках номера 
# цветов Бори.
# Найдите три множества: номера цветов кубиков, которые 
# есть в обоих наборах; номера цветов кубиков, которые 
# есть только у Ани и номера цветов кубиков, которые есть 
# только у Бори. Для каждого из множеств выведите сначала 
# количество элементов в нем, а затем сами элементы, 
# отсортированные по возрастанию.

N, M = [int(i) for i in input().split()]
N_set = set()
M_set = set()

for i in range(N):
    n = input()
    N_set.add(n)

for j in range(M):
    m = input()
    M_set.add(m)

N_and_M = N_set & M_set # номера в обоих наборах
NM_list = sorted([int(i) for i in N_and_M])
just_N = N_set - N_and_M # номера только у Ани
N_list = sorted([int(i) for i in just_N])
just_M = M_set - N_and_M # номера только у Бори
M_list = sorted([int(i) for i in just_M])

print(len(NM_list))
print(' '.join([str(i) for i in NM_list]))
print(len(N_list))
print(' '.join([str(i) for i in N_list]))
print(len(M_list))
print(' '.join([str(i) for i in M_list]))