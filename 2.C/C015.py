sum_ans=0
n=int(input())
for i in range(n):
    d,p=list(map(int,input().split()))
    if "3" in str(d):
        sum_ans+=int(p*0.03)
    elif "5" in str(d):
        sum_ans+=int(p*0.05)
    else:
        sum_ans+=int(p*0.01)
print(sum_ans)
