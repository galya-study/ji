# Самое частое слово
# Дан текст: в первой строке задано число строк, 
# далее идут сами строки. Выведите слово, которое 
# в этом тексте встречается чаще всего. Если 
# таких слов несколько, выведите то, которое 
# меньше в лексикографическом порядке.

count = int(input())
words = dict()

for i in range(count):
    string = [str(i) for i in input().split()]
    for j in string:
        if j in words:
            words[j] = words[j] + 1
        else:
            words[j] = 0

max_key = ''
max_count = -1

for i in reversed(sorted(words.keys())):
    if max_count <= words[i]:
        max_count = words[i]
        max_key = i

print(max_key)