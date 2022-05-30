a={}
size=int(input("enter the size"))
for i in range(size):
  key=input("enter the key")
  value=input("enter the value")
  a[key]=value
print(a)
if(len(a)==0):
  print("it is empty ")
 else:
    print("it is not empty ")