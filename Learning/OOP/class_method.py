class Person:
	# Конструктор класса
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

	# @ - декоратор, позволяет не использовать слово self
	@staticmethod
	def say_merry_cristmas():
		print('Merry Cristmas!!!')


	def say_hi(self):
		print('Привет! Меня зовут', self.name)

	def say_gender(self):
		print(self.gender)

p = Person('Swaroop', 'male')
p.say_hi()
print(p.name, p.gender)
p.say_gender()
