def f(stop):
    n = 0
    while n <= stop:
        if(n % 3 == 0 and n % 4 == 0):
            yield n
        n+=1
a = int(input())

for x in f(a):
    print(x)