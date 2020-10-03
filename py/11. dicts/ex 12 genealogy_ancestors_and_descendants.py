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

def search(g1, g2):
    if g1 == g2:
        return True
    while g1 in genealogy_dict:
        g1 = genealogy_dict[g1]
        if g1 == g2:
            return True
    return False

genealogy_dict = dict()

for i in range(int(input())-1):
    child, parent = [str(i) for i in input().split()]
    genealogy_dict[child] = parent

for j in range(int(input())):
    gen1, gen2 = [str(i) for i in input().split()]
    
    if search(gen1, gen2):
        print(2)
    elif search(gen2, gen1):
        print(1)
    else:
        print(0)