import os 

def dlt(path):
        if os.path.exists(path):
            if os.access(path, os.R_OK) and os.access(path, os.W_OK) and os.access(path, os.X_OK):
                os.remove(path)
        else:
            print("The file does not exist")

path = input()
dlt(path)