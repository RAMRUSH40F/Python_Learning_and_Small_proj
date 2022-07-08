'''
https://mathworld.wolfram.com/Factorial.html
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
'''

import math

def zeros(n):
    if n == 0: return 0
    sum = 0
    k = math.log(n,5)
    # print(k)
    for i in [1,k]:
        sum = sum + n/(5**i)
        # print(sum)
    return math.floor(sum)

print(zeros(7))