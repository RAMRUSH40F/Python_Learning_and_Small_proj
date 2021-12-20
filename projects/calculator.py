
lang = 'EN'
prodolzhit = 'y'
x = input("The current language is EN. If you want to switch a language to RU, enter 'y'")
if x == 'y':
	lang = 'RU'

if lang == 'RU':
	f = 'Введите первое число>>' 
	o = 'Введите операцию для чисел>>'
	s = 'Введите второе число>>'
	e = 'Ошибка'
	Cont = "Введите 'y', чтобы продолжить, или любую другую букву, чтобы завершить>>"
	r ='Результат: '

	
else: 
	f = 'Enter the first number>>'
	o = 'Enter the operation(+,-,/,*)>>'
	s = 'Enter the second number>>'
	e = 'Error'
	Cont = 'Enter "y" to continue or other letter to exit>>'
	r = 'The result is'


while prodolzhit == 'y':

	f_num = float(input(f))
	oper = input(o)
	s_num = float(input(s))

	if oper == '+':
		print(r,f_num + s_num)
	elif oper == '*':
		print(r,f_num * s_num)
	elif oper == '-':
		print(r,f_num - s_num)
	elif oper == '/':
		print(r,f_num / s_num)
	else:
		print(e)
	prodolzhit = input(Cont)

