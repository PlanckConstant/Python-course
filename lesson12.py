'''
if выражение 1
    блок кода 2
elif выражение 2
    блок кода 2
else выражение 3
    блок кода 3
'''

x = 0
if x:
    print('Истина')
else:
    print('Ложь')

light = 'red'
if light == 'red':
    print('stop')
elif light == 'yellow':
    print('weit')
elif light == 'green':
    print('go')
else:
    print('what?')


age = int(input('Сколько Вам лет? '))
if age >= 18:
    print("Добро пожаловать!")
else:
    print(f'Вам {age} лет, не хватает {18-age}' )

time = 11
if time < 12 or time > 13:      #Не строгое или
    print('Open')
else:
    print('Close')

time = 11
day = 'st'
if time >= 8 and day != 'su':    # И
    print('Open')
else:
    print('Close')
x = 0
if not x:                        #Отрицание условия _not_
    print('OK')
else:
    print('NO')

y = 1
res = 'OK' if y else 'NO'        #Сокращённая запись условий
print(res)

print('OK' if y else 'NO')       #То же самое, но сразу с принтом