def ff(l):
    f = open("text.txt", "a")
    f.write(str(l) + '\n')
    f.close()


s = input()
l = list(item for item in s.split())
ff(l)