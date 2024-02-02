s="OPENAI"
key="CRYPTO"
res=""
for i in range(len(s)):
  if ord(s[i])+(ord(key[i])-ord("A"))<ord("Z"):
    res += chr(ord(s[i])+(ord(key[i])-ord("A")))
  else:
    res+=chr((ord(s[i])+(ord(key[i])-ord("A")))-26)
print(res)
#res = QGCCTW
