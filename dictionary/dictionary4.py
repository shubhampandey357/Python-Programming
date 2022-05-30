a={}
size=int(input("enter the size"))
for i in range(size):
  key=int(input("enter the key"))
  value=int(input("enter the value"))
  a[key]=value
print("maximum key =",max(a))
print("minimum key =",min(a))