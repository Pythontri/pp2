def t(u):
    f = all(u)
    return f
    
x = input()
u = (bool(i) != False for i in x.split())

print(t(u))