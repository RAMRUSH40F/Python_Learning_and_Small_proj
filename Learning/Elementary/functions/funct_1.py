def sayhello ():
	print('Привет, мир!')
sayhello()
#Аналогично мы передаём значения, когда вызываем функцию. Обратите внимание на
#Терминологию: имена, указанные в объявлении функции, называются параметрами, то-
#гда как значения, которые вы передаёте в функцию при её вызове, – аргументами.

def printmax(a,b): # a,b - параметры функции
	if a>b:
		print(a, "Максимально.")
	elif a==b:
		print(a,'равно',b)
	else:
		print(b,'Максимально.')
printmax(3,4)   #3,4 - аргументы функции

x=5;y=8
printmax(x,y)
