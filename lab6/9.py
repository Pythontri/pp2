a = input()
n = [int(x) for x in a.split()]

print(eval('*'.join(str(i) for i in n)))