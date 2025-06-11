#!/usr/bin/python3
def uppercase(s):
    result = ""
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            result += chr(ord(s[i]) - 32)
        else:
            result += s[i]
    return result

print(uppercase("best"))
