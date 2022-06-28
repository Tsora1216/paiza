mydict={}
n,x,y=list(map(int,input().split()))
for i in range(n):
    mydict[i]=""
    if (i+1)%x==0:
        mydict[i]+="A"
    if (i+1)%y==0:
        mydict[i]+="B"
    if mydict[i] == "":
        mydict[i]+="N"

for i in range(len(mydict)):
    print(mydict[i])
