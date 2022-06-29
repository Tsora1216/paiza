n=int(input())
alist=list(map(int,input().split()))
t,q=list(map(int,input().split()))
for i in range(q):
    x,k=list(map(int,input().split()))
    if t>=alist[x-1]*k:
        t-=alist[x-1]*k
print(t)
