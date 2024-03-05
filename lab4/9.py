def f(start):
    n = start
    while n >=0:
        yield n
        n-=1
a = int(input())
for x in f(a):
    print(x)

