N=int(input())
mydict={}
for i in range(N):
    mydict[i+1]=int(input())
M=int(input())
for i in range(M):
    a,b,x=list(map(int,input().split()))
    if mydict[a]-x<0:
        mydict[b]+=mydict[a]
        mydict[a]-=mydict[a]
    else:
        mydict[a]-=x
        mydict[b]+=x
for i in range(len(mydict)):
    print(mydict[i+1])
