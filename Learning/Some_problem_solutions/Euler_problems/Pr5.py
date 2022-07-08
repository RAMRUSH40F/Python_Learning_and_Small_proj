#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

#Какое самое маленькое число делится нацело на все числа от 1 до 20?	

from math import gcd # greatest common diviser -наибольшее общее кратное
from functools import reduce


def НОК(a, b):  # LeastCommonMultiple(x,y)
    return (a * b) // gcd(a, b)  # GreatestCommonDivisor(x,y)

numbers = range(1, 21) 
result = reduce(НОК, numbers)
print(result)  
 