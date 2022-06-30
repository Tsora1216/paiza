n,m=list(map(int,input().split()))
for i in range(n):
    a,b=list(map(int,input().split()))
    point=a-b*5
    if point<0:
        point=0
    if m <= point:
        print(i+1)
