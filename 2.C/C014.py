n,r=list(map(int,input().split()))
r=r*2
for i in range(n):
    h,w,d=list(map(int,input().split()))
    if h>=r and w>=r and d>=r:
        print(i+1)
