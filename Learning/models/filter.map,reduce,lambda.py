#Проверим на четность
from functools import reduce

print(reduce(lambda a,b:a*b, (50,57,89,12,100))) 


a = filter(lambda x: (x%2==0), (2,4,5,7,8,13,124))
print(list(a))

help = ('reduce','lambda','map','filter')