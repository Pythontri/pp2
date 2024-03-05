import time
import math

def square_root(x):
    return math.sqrt(x)

n = float(input())    
ms = int(input())
time.sleep(ms / 1000.0) 

result = square_root(n)
print(f"Square root of {n} after {ms} miliseconds is {result}")