n=int(input())
ans_list=[]
for i in range(n):
    s1,s2,s3=list(map(int,input().split()))
    ans_list.append(s1+s2+(24-s3))
print(min(ans_list))
print(max(ans_list))
