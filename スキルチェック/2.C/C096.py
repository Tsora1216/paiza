from collections import defaultdict
d = defaultdict(int)
n=int(input())
a,b=list(map(int,input().split()))
for i in range(a,b+1):
    d[i]=1

#print(d)

for i in range(1,n):
    a,b=list(map(int,input().split()))
    for j in range(a,b+1):
        d[j]+=1
#print(d)
flag=0
for i,j in d.items():
    #print(i,j)
    if d[i]==n:
        flag=1
        
print("OK") if flag==1 else print("NG")
