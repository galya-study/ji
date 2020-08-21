# Степень двойки
# По данному натуральному числу N найдите 
# наибольшую целую степень двойки, не 
# превосходящую N. Выведите показатель 
# степени и саму степень.
# Операцией возведения в степень пользоваться нельзя!

N = int(input())

power = 1
value = 2

if N == 1:
    power = 0
    value = 1
    print(power, value)
elif N == 2:
    print(power, value)
else:
    while value <= N:
        if value * 2 > N:
            print(power, value)
            break

        value *= 2
        power += 1