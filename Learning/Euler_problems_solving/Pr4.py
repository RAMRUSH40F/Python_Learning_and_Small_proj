#Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
#программа проверки полиндомов от 5 знаков до 6 знаков длиной

res =[]
dels = list(range(100,999))
dels.reverse()
end =[]

def polyndrom(x):
	return str(x) == str(x)[::-1]
print(polyndrom(6606))



for i in range(10000,999*999):
	if polyndrom(i):
		res.append(i)
res.reverse()
#функция проверки на делимость на трехзначные числа

for num in res:
	for z in dels:
		if num % z == 0 :
			s = num // z
			if z in range(100,999):
				if s in range(100,999):
					print('Трехзначные множители {0} и {1} дают полиндром {2}'.format(z,s,num))
					end.append(num)
print('Ответ:',max(end))










# сколько цифр в составе полиндрома из произвдения 3-значных цифр. Это точно либо 5, либо 6