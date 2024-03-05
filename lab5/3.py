import re

s = str(input())
pattern = r"[a-z]_[a-z]_[a-z]*"

x = re.search(pattern, s)
#y =  ''.join(x)
if x:
    print("Match found:", x.group())
else:
    print("No match found")