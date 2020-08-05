#Дележ яблок
#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. 
#Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? 
#Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).

schoolchild = int(input())
amountOfApples = int(input())

amountForChild = amountOfApples // schoolchild
modulo = amountOfApples % schoolchild

print(amountForChild)
print(modulo)