N,M=list(map(int,input().split()))
sum_ans=0
for i in range(N-1):
    num=int(input())
    if M>=num:
        sum_ans+=num
print(sum_ans)