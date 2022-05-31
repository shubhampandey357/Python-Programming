a={}
size=int(input("enter the size"))
for i in range(size):
  key=int(input("enter the key"))
  value=int(input("enter the value"))
  a[key]=value
print(a)
s=0
k=0
l=0
for j in a.keys():
  s=s+j
for m in a.values():
  k=k+m
l=s+k
print("the sum of all items of dictionary",l)
