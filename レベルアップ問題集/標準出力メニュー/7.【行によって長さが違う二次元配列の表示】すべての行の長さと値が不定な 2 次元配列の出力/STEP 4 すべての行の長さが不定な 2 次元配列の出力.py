import numpy as np
N=int(input())
Mlist=list(map(int,input().split(" ")))
for i in Mlist:
    nlist=np.arange(1,i+1)
    print(*nlist)