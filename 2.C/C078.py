sum_ans=0
kabu=0
n,c1,c2=list(map(int,input().split()))
for i in range(n):
    p=int(input())
    if c2<=p or i+1==n:
        sum_ans+=p*kabu
        kabu=0
    elif c1>=p:
        sum_ans-=p
        kabu+=1
    else:
        None
print(sum_ans)
