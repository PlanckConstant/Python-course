###########  Цыклы while & for  ##########

#while True:
#    print('Hello')         # Бесконечный цыкл

i = 1
#while i <= 1:
#    print(i)               # Бесконечный цыкл

while i <= 10:
    print(i)               # Бесконечный цыкл
    i += 1                 # i = i + 1

z = 1
while z <= 10:
    print(z, sep='', end=' ')   #Печать в одну строку. sep - разделитель, end - окончание строки (стд.\n)
    z += 1

s = 'Hello word'
for l in s:                 # l это буква. Для каждой буквы в строке
    print(l, end=' ')       # Печатай буквы через пробел

t = 'Hello word'
for l in t:                 # l это буква. Для каждой буквы в строке
    print(l, end=' ')       # Печатай буквы через пробел