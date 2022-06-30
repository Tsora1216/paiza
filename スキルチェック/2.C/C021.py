xc,yc,r1,r2=list(map(int,input().split()))
n=int(input())
for i in range(n):
    x,y=list(map(int,input().split()))
    if r1**2 <= (x-xc)**2 + (y-yc)**2 <= r2**2:
        print("yes")
    else:
        print("no")
