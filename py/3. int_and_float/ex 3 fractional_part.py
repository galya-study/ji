# Дробная часть
# Дано положительное действительное число X. 
# Выведите его дробную часть.

import math

x = float(input())

xInt = int(x)

div = float(x - xInt)

print(str(div))