#program to print last n words.
f=open("data.txt",'r')
x=f.read().split()
print(x[-5:])
f.close()