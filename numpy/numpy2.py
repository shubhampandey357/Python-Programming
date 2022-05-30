# Program to create a matrix.
import numpy as np 
n=int(input()) #no. of rows
m=int(input()) #no. of columns
s=[]
for i in range(n):
    l=list(map(int,input().split()))
    for i in l:
        s.append(i)
a=np.array(s)
a.shape=(n,m)
print(a)