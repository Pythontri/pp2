def f(start,stop):
    curnum = start
    while curnum <= stop:
        yield curnum
        curnum +=1
for x in f(0,10):
    print(x*x, end = " ")
