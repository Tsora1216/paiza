N,M=list(map(int,input().split()))
Alist=list(map(int,input().split()))
Blist=list(map(int,input().split()))
count=0
for i in range(len(Blist)):
    for j in range(Blist[i]):
        print(Alist[count],end="")
        if Blist[i]-1!=j:
            print("",end=" ")
        count+=1
    print()