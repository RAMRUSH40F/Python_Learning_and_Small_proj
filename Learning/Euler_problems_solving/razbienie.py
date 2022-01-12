def razbienie(a):
	spisok = []
	while a // 10 != 0 :
		b = a % 10
		a = a//10
		spisok.append(b)
	else:
		b = a % 10
		spisok.append(b)
	spisok.reverse()
	return spisok
