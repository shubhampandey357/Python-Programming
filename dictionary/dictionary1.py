a={}
size=int(input("enter the size"))
for i in range(size):
  key=int(input("enter the size"))
  value=int(input("enter the value"))
  a[key]=value
for i in a.keys():
  print(i,":",a[i})