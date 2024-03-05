import os 

def existence(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            filename = os.path.basename(path)
            directory = os.path.dirname(path)
            print(f"Path exists. \nFilename - {filename}\nDirectory: {directory}")
        elif os.path.isdir(path):
            directory = os.path.dirname(path)
            print(f"Path exists. Directory: {directory}")
    else:
        print("Path does not exist")

path = input()

existence(path)