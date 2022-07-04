n=int(input())
clist = list(map(int,input().split()))
#print(n)
#print(clist)
def list_del(clist):
    for i in range(len(clist)-1):
        for j in range(i,len(clist)):
            #print(clist[i],clist[j])
            if clist[i]+1==clist[j] or clist[i]-1==clist[j]:
                if clist[i]<clist[j]:
                    del clist[i]
                else:
                    del clist[ij]
                return 0,clist
    return 1,clist

flag=0
while flag==0:
    #print(clist)
    flag,clist=list_del(clist)

print(sum(clist))
