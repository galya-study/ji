# Родословная: предки и потомки
# Даны два элемента в дереве. Определите, является ли 
# один из них потомком другого.
# Во входных данных записано дерево в том же формате, 
# что и в предыдущей задаче Далее идет число запросов K. 
# В каждой из следующих K строк, содержатся имена двух 
# элементов дерева.
# Для каждого такого запроса выведите одно из трех чисел: 
# 1, если первый элемент является предком второго, 
# 2, если второй является предком первого или 
# 0, если ни один из них не является предком другого.

def search1(g1, g2):
    out_search = 0
    if g2 in genealogy_dict.keys():
        if genealogy_dict[g2] == g1:
            return 1
        else:
            for i in genealogy_dict.keys():
                if genealogy_dict[i] == g1:
                    out_search = search1(i, g2)
                    if out_search == 1:
                        return 1
                        break
    if out_search == 0:
        return 0


genealogy_dict = dict()

for i in range(int(input())-1):
    child, parent = [str(i) for i in input().split()]
    genealogy_dict[child] = parent

for j in range(int(input())):
    gen1, gen2 = [str(i) for i in input().split()]
    out = 0

    if gen2 in genealogy_dict.keys():
        out = search1(gen1, gen2)
    elif gen1 in genealogy_dict.keys() and out == 0:
        out = search1(gen2, gen1)
        if out == 1:
            out = 2
    else:
        out = 0
    
    print(out)
    