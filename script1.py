string = "HELLO"
s=string.upper()
res=""
for i in s:
  if ord(i)<ord("Z")-3:
    res+=chr(ord(i)+3)
  elif ord("Z")-3<ord(i)<=ord("Z"):
    res+=chr(ord(i)-23)
print(res)
#res = KHOOR