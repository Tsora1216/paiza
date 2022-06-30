n=int(input())
sum_ans=0
now=1
for i in range(n):
    f=int(input())
    sum_ans+=abs(now-f)
    now=f
print(sum_ans)
