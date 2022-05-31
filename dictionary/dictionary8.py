a={}
size=int(input("enter the size"))
for i in range(size):
  key=int(input("enter the key"))
  value=int(input("enter the value"))
  a[key]=value
print(a)
n=int(input("enter the key to be delet"))
del a[n]
print("dict after deleting",a)