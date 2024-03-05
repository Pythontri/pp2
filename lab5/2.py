import re

s = str(input())
pattern = r"ab{2,3}"

x = re.search(pattern, s)

if x:
    print("Match found:", x.group())
else:
    print("No match found")