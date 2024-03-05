import os 

def existence(path):
    s = {
        "e": os.access(path, os.F_OK),
        "r": os.access(path, os.R_OK),
        "w": os.access(path, os.W_OK),
        "ex": os.access(path, os.X_OK)
    }
    return s

path = input()
info = existence(path)
print(f"existence: {info['e']}")
print(f"readability: {info['r']}")
print(f"writability: {info['w']}")
print(f"executability: {info['ex']}")