def ct():
    with open('text.txt', 'r') as file:
        linecnt = sum(1 for line in file)
    return linecnt

print(ct())