def f(s):
    cnt = 0
    Cnt = 0
    for i in s:
        if i.islower():
            cnt += 1
        else:
            Cnt += 1
    return cnt, Cnt

s = input()
print(f(s))