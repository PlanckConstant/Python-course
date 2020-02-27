name = 'John'
age = 30

print('My name is ' + name + '. I\'m ' + str(age) + '.')
print('My name is %(name)s. I\'m %(age)d.' % {'name': name, 'age': age})
print('My name is %s. I\'m %d.' % (name, age))

print('Title: %s, Prise: %f' % ('Sony', 40))     # 40,000000   float отображает сного знаков  после запятой
print('Title: %s, Prise: %.2f' % ('Sony', 40))   #40.00        %.2f ознасает 2 знака  после запятой

######  format  #######

print('My name is {}. I\'m {}.'.format(name, age))               # более современное написание
print('My name is {0}. I\'m {2}.'.format(name, age, 40))         # Можно вручную проставлять аргументы меняя порядок
print('My name is {x}. I\'m {z}.'.format(x=name, y=age, z=50))   # Именоованные аргументы
print('5 + 2 = {}'.format(5+2))


###### f-strings #######
print(f'My name is {name}. I\'m {age}.')              #f--strings позволяет подставлять непосрественно переменную
print(f'My name is {name}. I\'m {age+4}.')            #и проводить вычислления
print(f'5 + 2 = {5+6}')