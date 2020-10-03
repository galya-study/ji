# Угадай число - 2
# Август и Беатриса продолжают играть в игру, но Август 
# начал жульничать. На каждый из вопросов Беатрисы он 
# выбирает такой вариант ответа YES или NO, чтобы множество 
# возможных задуманных чисел оставалось как можно больше. 
# Например, если Август задумал число от 1 до 5, а Беатриса 
# спросила про числа 1 и 2, то Август ответит NO, а если 
# Беатриса спросит про 1, 2, 3, то Август ответит YES.
# Если же Бетриса в своем вопросе перечисляет ровно половину 
# из задуманных чисел, то Август из вредности всегда отвечает 
# NO. Наконец, Август при ответе учитывает все предыдущие 
# вопросы Беатрисы и свои ответы на них, то есть множество 
# возможных задуманных чисел уменьшается.
# Первая строка содержит наибольшее число, которое мог 
# загадать Август. Каждая следующая строка содержит очередной 
# вопрос Беатрисы: набор чисел, разделенных пробелами. Последняя 
# строка входных данных содержит одно слово HELP.
# Для каждого вопроса Беатрисы выведите ответ Августа на этот 
# вопрос. После этого выведите через пробел, в порядке возрастания, 
# все числа, которые мог загадать Август после ответа на все 
# вопросы Беатрисы.

n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    if len(possible_nums & guess) > len(possible_nums) / 2:
        print('YES')
        possible_nums &= guess
    else:
        print('NO')
        possible_nums &= all_nums - guess
         
print(' '.join([str(x) for x in sorted(possible_nums)]))