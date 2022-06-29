A,B=list(map(int,input().split()))
n=int(input())
for i in range(n):
    x,y=list(map(int,input().split()))
    if A>=x:
        if A==x:
            if B<y:
                print("High")
            else:
                print("Low")
        else:
            print("High")
    else:
        print("Low")
