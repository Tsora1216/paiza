h,w=list(map(int,input().split()))
Slist=[]
Plist=[]
sum_ans=0
for i in range(h):
    Slist.append(input())
for i in range(h):
    Plist=list(map(int,input().split()))
    for j in range(w):
        if Slist[i][j]=="o":
            sum_ans+=Plist[j]
print(sum_ans)
