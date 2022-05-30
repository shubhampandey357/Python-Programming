#program to subtract two matrices.
import numpy as np  
n=int(input())
m=int(input())
a=[]
b=[]
for i in range(n):
    l1=list(map(int,input().split()))
    a.append(l1)
for i in range(n):
    l2=list(map(int,input().split()))
    b.append(l2)
x=np.array(a)
y=np.array(b)
x.shape=(n,m)
y.shape=(n,m)
c=np.subtract(x,y)
print(c)