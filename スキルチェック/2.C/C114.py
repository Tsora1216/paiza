N=int(input())-1
s=input()[-1]
flag=0
for i in range(N):
    temp=input()
    nexts=temp[0]
    if s!=nexts:
        flag=1
        print(s,nexts)
        break
    s=temp[-1]
print("Yes") if flag==0 else None