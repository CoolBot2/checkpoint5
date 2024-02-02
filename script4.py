from math import*

name = input("username: ")
passwd = input("password: ")
#generating the key to use as a shift for the ceasar cypher
key=round(abs(26*sin(len(name))))
#ceasar cypher on username with shift = key
encusr=""
s=name.upper()
for i in range(len(s)):
  if ord(s[i])+key<ord("Z"):
    encusr += chr(ord(s[i])+key)
  else:
    encusr+=chr((ord(s[i])+(key)-26))
# fills out the strings with "A" untill the length of the two strings match
def filler(a,b):
  while len(a)<len(b):
    a+="A"
  return a
#vigenere cypher on password using encuser(username after encryption) as the key
def vil(passwd,encusr):
  s=filler(passwd.upper(),encusr)
  key=filler(encusr,passwd.upper())
  res=""
  for i in range(len(s)):
    if ord(s[i])+(ord(key[i])-ord("A"))<ord("Z"):
      res += chr(ord(s[i])+(ord(key[i])-ord("A")))
    else:
      res+=chr((ord(s[i])+(ord(key[i])-ord("A")))-26)
  return res

print(f"encrypted credentials: {encusr}@{vil(passwd,encusr)}")