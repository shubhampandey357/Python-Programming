#program to find the length of file.
f=open("data.txt",'r')
x=f.read()
print(len(x))
f.close()