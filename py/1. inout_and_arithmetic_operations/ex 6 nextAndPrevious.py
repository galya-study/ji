#Следующее и предыдущее
#Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
#Пример:
#The next number for the number 1534 is 1535.
#The previous number for the number 1534 is 1533.

n = int(input())

next = n + 1
previous = n - 1

print('The next number for the number ' + str(n) + ' is ' + str(next) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(previous) + '.')