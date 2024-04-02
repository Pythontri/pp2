import re 

pattern = r"[ ,.]"

def test(pattern, Data, Number, Result):
    x = re.sub(pattern, ":", Data)
    print(x)
    if x == Result:
        print(Number + " is passed!")
    else: 
        print(Number + " is not passed!")

test(pattern, "My.Super,Test ", "Test 1", "My:Super:Test:")
test(pattern, "My.Super.Test   I,Am.Robot", "Test 2", "My:Super:Test:::I:Am:Robot")
test(pattern, "A   Ti Zhe.Delaesh,Laby,ImGhoul.", "Test 2", "A:::Ti:Zhe:Delaesh:Laby:ImGhoul:")
test(pattern, "Cry,Me A..River   ", "Test 4", "Cry:Me:A::River:::")
