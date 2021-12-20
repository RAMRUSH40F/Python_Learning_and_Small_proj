def iscomplete(n,b): # является ли число n степенью числа b
  y = n # тоже ссылается на 162
  while y % b == False: 
  	y = y // b
  return y == True

print(iscomplete(25,5))



