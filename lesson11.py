name = 'John'
age = 30
# Следующие команды выведут одинаковый результат.
print('My name is ' + name + '. i\'m ' + str(age) + '.')                #Подстановка с разрывом строк. Стандартная.
print('My name is %(name)s. i\'m %(age)d.' %{'name': name, 'age': age}) #Именные маркеры. именованная подстановка переменных с прописыванием маркеров
print('My name is %s. i\'m %d.' %(name, age))                           #Позиционные маркеры. позиционная подстановка, порядок маркеров в моответствии со скобками