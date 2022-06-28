S=input()
S=S.replace("-","")
sum_ans=0

for i in range(len(S)):
    if S[i]=="0":
        sum_ans+=12
    else:
        sum_ans+=(int(S[i])+2)
print(sum_ans*2)
