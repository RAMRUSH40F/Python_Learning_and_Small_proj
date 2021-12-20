class Person: # оздаем класс
	def __init__(self, name): # при создании переменной любое значение в скобках возьмется как name
		self.name = name # self.name становится именем name
	
	def say_hi(self):
		print('Привет! Меня зовут', self.name)

p = Person('Swaroop')
p.say_hi()
# Предыдущие 2 строки можно
# Person('Swaroop').say_hi()