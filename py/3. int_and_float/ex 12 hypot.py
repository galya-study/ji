# Гипотенуза
# Дано два числа a и b. Выведите гипотенузу треугольника 
# с заданными катетами.

import math

a = int(input())
b = int(input())

c = math.sqrt(a**2 + b**2)

print(str(c))