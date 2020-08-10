# Конец уроков
# В некоторой школе занятия начинаются в 9:00. Продолжительность 
# урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 
# минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.
# Дан номер урока (число от 1 до 10). Определите, когда заканчивается 
# указанный урок.
# Выведите два целых числа: время окончания урока в часах и минутах.

num = int(input())

minuteLesson = num * 45 # находим количество минут только уроков

if num % 2 == 1:
    minuteBreak = (5 + 15) * (num // 2)
else:
    minuteBreak = (5 + 15) * (num // 2 - 1) + 5

minute = (minuteBreak + minuteLesson) % 60
hour = 9 + ((minuteBreak + minuteLesson) // 60)

print(str(hour))
print(str(minute))