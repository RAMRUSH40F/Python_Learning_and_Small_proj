import time
from functools import cache, lru_cache

@lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    for i in range(400):

        print(i)
        print('%s seconds' % round((time.time() - start_time),10))



if __name__ == '__main__':
    start_time = time.time()
    main()
