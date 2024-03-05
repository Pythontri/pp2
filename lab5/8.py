import re 

def repl(obj):
    return obj.group(1) + ' ' + obj.group(2) 


pattern = r"([a-zA-z])([A-Z])"

def test(pattern, Data, Number, Result):
    x = re.sub(pattern, repl, Data)
    print(x)
    if x == Result:
        print(Number + " is passed!")
    else: 
        print(Number + " is not passed!")

test(pattern, "MySuperTest", "Test 1", "My Super Test")
test(pattern, " MySuperTest IAmRobot", "Test 2", " My Super Test I Am Robot")