n=list(input())
sum_ans=0
for i in range(len(n)):
    sum_ans+=int(n[4-i])*(2**i)
print(sum_ans)
