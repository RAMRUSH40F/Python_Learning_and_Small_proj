x=50
def func(x):
	print('x равен',x)   #локальные функции
	x=2
	print('Замена локального х на',x)
func(x)
print('x по-прежнему',x) 

n=100
def func1():
	global n

	print('n equels to',n)
	n=2
	print('заменяем глобальнок значение n на',n)

func1()
print('Значение n состовляет',n)
