string = "VWDQGD"
s=string.upper()
res=""
for i in s:
    res+=chr(ord(i)-3)

print(res)