# Родословная: подсчет уровней
# В генеалогическом древе у каждого человека, кроме 
# родоначальника, есть ровно один родитель.
# Каждом элементу дерева сопоставляется целое неотрицательное 
# число, называемое высотой. У родоначальника высота равна 0, 
# у любого другого элемента высота на 1 больше, чем у его 
# родителя.
# Вам дано генеалогическое древо, определите высоту всех его 
# элементов.
# Программа получает на вход число элементов в генеалогическом 
# древе N. Далее следует N−1 строка, задающие родителя для 
# каждого элемента древа, кроме родоначальника. Каждая строка 
# имеет вид имя_потомка имя_родителя.
# Программа должна вывести список всех элементов древа в 
# лексикографическом порядке. После вывода имени каждого 
# элемента необходимо вывести его высоту.
# Примечание
# Эта задача имеет решение сложности O(n), но вам достаточно 
# написать решение сложности O(n2) (не считая сложности 
# обращения к элементам словаря).

def search(parent, level_parent):
    for i in genealogy_dict.keys():
        if genealogy_dict[i] == parent:
            genealogy_level_dict[i] = int(level_parent) + 1
            search(i, genealogy_level_dict[i])


N = int(input())
genealogy_dict = dict()
genealogy_level_dict = dict()

for i in range(N-1):
    child, parent = [str(i) for i in input().split()]
    genealogy_dict[child] = parent

for i in genealogy_dict.values():
    if i not in genealogy_dict.keys():
        genealogy_level_dict[i] = int(0)
        search(i, 0)
        break

for i in sorted(genealogy_level_dict.keys()):
    print(i, genealogy_level_dict[i])