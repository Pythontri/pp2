def copyfile():
    with open('text.txt', 'r') as t:
            with open('textcopy.txt', 'w') as c:
                c.write(t.read())

copyfile()