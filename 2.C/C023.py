Alist=list(map(int,input().split()))
n=int(input())
for i in range(n):
    temp_list=list(map(int,input().split()))
    temp_ans=0
    for j in range(len(Alist)):
        if Alist[j] in temp_list:
            temp_ans+=1
    print(temp_ans)
