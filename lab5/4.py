import re 

s = str(input())
pattern = r"[A-Z][a-z]" 
x = re.findall(pattern, s)
y =  ''.join(x)

if x:
    print("Match found:", y)
else:
    print("No match found")