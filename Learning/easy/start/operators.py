#Операторы – это некий функционал, производящий какие-либо действия, который мо-
#жет быть представлен в виде символов, как например +, или специальных зарезервиро-
#ванных слов. Операторы могут производить некоторые действия над данными, и эти дан-
#ные называются операндами. В нашем случае 2 и 3 – это операнды.
m = 'sa' # 
sh = 'sha'
res = m + sh
print(res)
print(res*5)

l = -110
k = 25
print(l+k)

i=11
print(i**2)
i = i + 1
print(i**2)
i = i + 1

print(2 << 2) #Сдвиг битов влево 2 << 2 даст 8. В двоичном виде 2представляет собой 10. Сдвиг влево на 2бита даёт 1000, что в десятичном видеозначает 8.

print(5 > 3) # true/false
print(63 >= 63)

a=2;a=a*3  #одинковая запись
b=2;b *=3 #Обратите внимание, что выражения вида «переменная = переменная операция выражение» принимает вид «переменная операция = выражение».
print(a,b)