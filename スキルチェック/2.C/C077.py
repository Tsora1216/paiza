k,n=list(map(int,input().split()))
for i in range(k):
    d,a=list(map(int,input().split()))
    if d<=0:
        point=a*100//n
    elif d<10:
        point=int((a*100//n)*0.8)
    else:
        point=0
    if point>=80:
        print("A")
    elif point>=70:
        print("B")
    elif point>=60:
        print("C")
    else:
        print("D")
        
        
