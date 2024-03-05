def f(start,stop):
    n = start
    while n <= stop:
        yield n * n
        n+=1
a = int(input("start"))
b = int(input("end"))

for x in f(a,b):
    print(x)