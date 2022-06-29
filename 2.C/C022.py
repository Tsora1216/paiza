n=int(input())
start_num=[]
end_num=[]
max_num=[]
min_num=[]
for i in range(n):
    a,b,c,d=list(map(int,input().split()))
    start_num.append(a)
    end_num.append(b)
    max_num.append(c)
    min_num.append(d)
print(start_num[0],end_num[-1],max(max_num),min(min_num))
