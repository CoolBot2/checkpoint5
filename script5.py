#this script  calculates the md5 of the checkpoint5.md file
import hashlib
f= open("checkpoint5.md","r")
content=f.read()
md5 = hashlib.md5().hexdigest()
print(md5)