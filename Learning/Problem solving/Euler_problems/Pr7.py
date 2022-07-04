#Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. 
#Очевидно, что 6-е простое число - 13.
#Какое число является 10001-м простым числом?

simple = []
numbers =list(range(2,10**6)) 
import simplenum
	
for i in numbers:		
	if simplenum.issimple(i) and len(simple) < 10001 :
		simple.append(i)
		print('Добавлено',i)
	
print('Длина',len(simple))
print(simple[-1])
