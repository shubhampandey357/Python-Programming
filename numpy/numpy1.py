#program to replace the max value of row to the right.
import numpy as np
s=[]
n=int(input())
m=int(input())
for i in range(n):
     l=list(map(int,input().split()))
     q=max(l)
     c=l.index(q)
     l[c],l[n-1]=l[n-1],q
     for i in l:
      s.append(i)
x=np.array(s)
x.shape=(n,m)
print(x)