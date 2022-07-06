
class Vector:

	def __init__(self, *args):
		self.projections = args

		try:
			self.x = self.projections[0]
			self.y = self.projections[1]
			self.z = self.projections[2]
		except IndexError :
			print('Минимальная длина вектора - 3 ')

 
	def __add__(self, other):
		if self.dim() == other.dim():
			if self.dim() <= 3 :
				return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

		else: print('Sorry, the vectors you are trying to sum are not the same length')


	def __sub__(self, other):
		if self.dim() == other.dim():
			if self.dim() <= 3 :
				return Vector(self.x-other.x, self.y-other.y, self.z-other.z)


	def __mul__(self, argument):
		if type(argument) == int :
			return Vector(self.x *argument, self.y*argument,self.z*argument)
		if type(argument) == Vector :
			return f'Скалярное произведение {self.x*argument.x + self.y*argument.y + self.z*argument.z}'

	def __rmul__(self, argument):
		if type(argument) == int:
			return Vector(self.x * argument, self.y * argument, self.z * argument)
		if type(argument) == Vector:
			return f'Скалярное произведение {self.x * argument.x + self.y * argument.y + self.z * argument.z}'

	def __neg__(self):
		return Vector(-self.x, -self.y, -self.z)


	def dim(self):
		# Get vectors dimension
		return len(self.projections)


	def give_info(self):
		print('dimension:', self.dim(), 'projections:', self.projections)



# TESTS
v_1 = Vector(5, 6, 5)
v_2 = Vector(1, 2, 3)


v_3 = v_2*5
v_3.give_info()

v_3 = v_2*v_1
print(v_3)

