x,p=list(map(int,input().split()))
i=0
sum_ans=x
while x!=0:
    #print(x)
    x=int(x*((100-p)/100))
    sum_ans+=x
print(sum_ans)
