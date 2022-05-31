#program to transpose a matrix
import numpy as np  
n=int(input())
m=int(input())
a=[]
for i in range(n):
    l1=list(map(int,input().split()))
    a.append(l1)
x=np.array(a)
x.shape=(n,m)
c=np.transpose(x)
print(c)