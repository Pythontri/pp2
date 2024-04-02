import re 

pattern = r"a.+b"

def test(pattern, Data, Number, Result):
    x = re.search(pattern, Data)
    if x:
        y = "Match found"
    else:
        y = "No match found" 
    if y == Result:
        print(Number + " is passed!")
    else: 
        print(Number + " is not passed!")

test(pattern, "annskdkdkb", "Test 1", "Match found")
test(pattern, "abob", "Test 2", "Match found")
test(pattern, "Alslddk", "Test 2", "No match found")
test(pattern, "CryMeARiver", "Test 4", "No match found")
