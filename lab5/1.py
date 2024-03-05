import re

s = str(input())
pattern = r"ab*"

x = re.search(pattern, s)

if x:
    print("Match found:", x.group())
else:
    print("No match found")