def total(initial=5,*numbers,extra_num=3):
	count = initial
	for number in numbers:
		count += extra_num
		print(count)
total(10,1,2,3,extra_num=50)
total(10,1,2,3)