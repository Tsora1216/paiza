import numpy as np
N=int(input())
for i in range(N):
    nlist=np.arange(1,i+2)
    print(*nlist)