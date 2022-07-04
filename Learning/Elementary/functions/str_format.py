# Имя файла : str_format.py
age= 18
name = 'Ramil'
print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name)) #Символическая замена

print('{name} написал код на {programm}'.format(name='Ramil', programm='Python')) #Команда с точной автозаменой
input()