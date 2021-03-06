# Количество слов в тексте
# Дан текст: в первой строке записано число строк, 
# далее идут сами строки. Определите, сколько 
# различных слов содержится в этом тексте.
# Словом считается последовательность непробельных 
# символов идущих подряд, слова разделены одним или 
# большим числом пробелов или символами конца строки.

N = int(input())
all_str = []
all_set = set()

for i in range(N):
    all_str.append([str(j) for j in input().split()])

for i in range(N):
    for j in all_str[i]:
        all_set.add(j)

print(len(all_set))