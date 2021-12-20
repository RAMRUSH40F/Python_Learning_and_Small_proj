
def polyndrom(x):
	forbidden = (".", '?', '!', ':', ';', '-', '—', '( )', '[ ]', '. . .', '’', '“ ”', '/',',',' ')
	
	if type(x) == str:
		x = x.lower()
		print('Строка преобразована в нижний регистр >> {0}'.format(x))
		
		for i in forbidden:
			if i in x:
				x = x.replace(i,'')
		print('Строка преобразована в {0} >>'.format(x))
			
	return str(x) == str(x)[::-1]




test= 'А за работу дадут? - Оба раза'
print(polyndrom(test))
 