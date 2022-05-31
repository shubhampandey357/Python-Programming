#program to write a statement in the file at end.
f=open("data.txt",'w')
f.write("hello world")
print(f)
f.close()