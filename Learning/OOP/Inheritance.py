class Parent:
	# Конструктор класса
	def __init__(self, nationality):
		self.nationality = nationality
	def say_hi(self):
		print('Привет! Меня зовут', self.name)

	def say_gender(self):
		print(self.gender)

class Child(Parent):
    def __init__(self,param_1, age):
        super().__init__(param_1)
		self.age = age

	def child_method(self):
		return


p = Person('Swaroop', 'male')
p.say_hi()
print(p.name, p.gender)
p.say_gender()
