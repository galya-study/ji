# Сумма цифр
# Дано трехзначное число. Найдите сумму его цифр.

i = int(input())

i1 = int(i // 100)
i2 = int((i - i1 * 100) // 10)
i3 = int(i - (i1 * 100) - (i2 * 10))

print(str(i1 + i2 + i3))