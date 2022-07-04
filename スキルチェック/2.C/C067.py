n,x=list(map(int,input().split()))
temp_list=""
while x!=0:
    temp_list+=str(x%2)
    x=x//2

#re_temp_list="".join(list(reversed(temp_list)))
#print(re_temp_list)

for i in range(n):
    k=int(input())-1
    print(temp_list[k])
