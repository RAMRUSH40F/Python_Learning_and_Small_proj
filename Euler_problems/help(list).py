
f = 13195112
list = []
import math 
n = math.ceil(math.sqrt(f))

for i in range (2,n):
	if f % i == 0:
		list.append(i)

def simple():


	for i in list:
		for k in range(2,i-1):
			if not i % k :
				list.sort(reverse=True)
				del list[0]
simple()

list.sort()
print('Простые делители числа:',list)
print('Наибольший -',max(list))
print(n)




for div in range (2,f):
	while div <= f:


	if f % div == 0:
		list.append(div)
		f = f / div
		continue
if f == 1:
	status = False


list = []
f=13195
status = True
div=2
while (div <= f):
	while not f % div :
		f //=div
		list.append(div)
		div +=1





list.sort()
print('Простые делители числа:',list)
print('Наибольший -',max(list))
