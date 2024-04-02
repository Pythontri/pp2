def al():
    for i in range(ord('A'), ord('Z') + 1):
        filename = f"{chr(i)}.txt" 
        with open(filename, "x"):
            pass

al()