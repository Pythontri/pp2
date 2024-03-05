def pldrm(s):
    rs = ''.join(reversed(s))
    if s == rs:
        print("Yes, the given string is palindrome!")
        return True
    else:
        print("This string is not palindrome")
    return False

s = input()
pldrm(s)