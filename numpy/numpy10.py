#program to print element in reverse order.
import numpy as np  
n=int(input())
m=int(input())
a=[]
for i in range(n):
    l1=list(map(int,input().split()))
    a.append(l1[::-1])
x=np.array(a)
x.shape=(n,m)
c=np.array(x)
print(c)