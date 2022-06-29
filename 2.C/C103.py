n,m=list(map(int,input().split()))
alist=[]
blist=[]
for i in range(m):
    a,b=list(map(str,input().split()))
    alist.append(int(a))
    blist.append(b)
for i in range(n):
    ans_list=[]
    for j in range(len(alist)):
        if (i+1)%alist[j]==0:
            ans_list.append(blist[j])
    if len(ans_list)==0:
        print(i+1)
    else:
        print(" ".join(ans_list))
