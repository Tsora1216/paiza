x1,y1,p1=list(map(int,input().split()))
x2,y2,p2=list(map(int,input().split()))
print(x1,y1,p1) if p1/(x1*y1) < p2/(x2*y2) else print("DRAW") if  p1/(x1*y1) == p2/(x2*y2) else print(x2,y2,p2)
