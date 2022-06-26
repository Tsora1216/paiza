m,n=map(int,input().split())
[print("{} ".format(m+i*n),end="") for i in range(9)]
print(m+9*n)
