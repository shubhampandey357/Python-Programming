# To merge two dictionary.
a={}
size=int(input("enter the size dict 1"))
for i in range(size):
  key=int(input("enter the key"))
  value=int(input("enter the value"))
  a[key]=value
print("dict a=",a)
b={}
size=int(input("enter the size dict 2"))
for i in range(size):
  k=int(input("enter the key"))
  v=int(input("enter the value"))
  b[k]=v
print("dict b=",b)
a.update(b)
print("dict after merging",a)