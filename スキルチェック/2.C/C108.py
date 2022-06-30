N=int(input())
xlist=[int(input()) for i in range(N)]
clist=[list(map(int,input().split())) for j in range(N)]
K=int(input())
ylist=[int(input()) for i in range(K)]

sum_ans=0
for i in range(len(ylist)):
    sum_ans+=xlist[ylist[i]-1]

for i in range(1,len(ylist)):
    sum_ans+=clist[ylist[i-1]-1][ylist[i]-1]

print(sum_ans)
