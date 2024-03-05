def f(stop):
    curnum = 0
    while curnum <= stop:
        if curnum % 2 == 0:
            yield curnum
        curnum +=1
a = int(input())
for x in f(a):
    print(x, end = ", ")

