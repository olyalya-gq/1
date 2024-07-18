import sys
##from functools import *
##@lru_cache(maxsize = None)

k=0
def f(n):
    if n == 0:
        return 0
    return f(n // 10) + f(n % 10)
       

for n in range(237567892, 1134567010):
    if f(n) > f(n+1):
        k += 1
        
sys.setrecursionlimit(10100) 
print(k)
