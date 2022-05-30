#program to find the number of lines in a file.
f=open("data.txt",'r')
x=f.readlines()
print(len(x))
f.close()