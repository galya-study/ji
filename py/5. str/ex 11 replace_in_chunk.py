# Замена внутри фрагмента
# Дана строка. Замените в этой строке все появления 
# буквы h на букву H, кроме первого и последнего вхождения.

s = input()

h1Pos = s.find('h')
hLPos = s.rfind('h')

sWithouth = s[h1Pos + 1:hLPos]
sWithH = sWithouth.replace('h', 'H')

sNew = s[0:h1Pos + 1] + sWithH + s[hLPos:len(s)]

print(sNew)