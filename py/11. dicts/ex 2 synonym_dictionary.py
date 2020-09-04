# Словарь синонимов
# Вам дан словарь, состоящий из пар слов. Каждое 
# слово является синонимом к парному ему слову. 
# Все слова в словаре различны.
# Для слова из словаря, записанного в последней 
# строке, определите его синоним.

n = int(input())
hello = dict()

for i in range(n):
    key, value = [str(i) for i in input().split()]
    hello[key] = value
    hello[value] = key

print(hello[str(input())])