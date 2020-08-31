# Отрицательная степень
# Дано действительное положительное число a и целоe число n.
# Вычислите a^n. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степень пользоваться нельзя.

def pow(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n > 1:
        return a * pow(a, n - 1)
    else:
        return 1 / (a * pow(a, abs(n) - 1))

a = float(input())
n = int(input())

print(pow(a, n))