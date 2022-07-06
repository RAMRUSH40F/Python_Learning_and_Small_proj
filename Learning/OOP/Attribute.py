class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан Human: {0})'.format(self.name))

    def tell(self):
        # Вывести информацию
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

    @staticmethod
    def say_hi():
        print(f'Привет, я человек.')

class Student(Human):
    # Представляет студента
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        print('({0} добавлен к Student)'.format(self.name))

    def tell(self):
        Human.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


    def give_full_info(self):

        print(f'{self.name} \n'\
              f'Возраст {self.age} \n'\
              f'Средняя успеваемость{self.marks}')


if __name__ == '__main__':
    st = Student('Elena', 25, 4.4)
    st.give_full_info()
    print(st.__dict__)

    st.__delattr__('name')
    print(st.__dict__)

