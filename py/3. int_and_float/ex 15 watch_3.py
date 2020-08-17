# Часы - 3
# С начала суток часовая стрелка повернулась на 
# угол в α градусов. Определите сколько полных 
# часов, минут и секунд прошло с начала суток, 
# то есть решите задачу, обратную задаче «Часы - 
# 1». Запишите ответ в три переменные и выведите 
# их на экран.

angle = float(input())

H = angle // 30
M = (angle - H * 30) // 0.5
S = (angle - H * 30 - M * 0.5) // 0.008333333

print(str(H), str(M), str(S))