at,de,ag=list(map(int,input().split()))
n=int(input())
count=0
for i in range(n):
    s,min_at,max_at,min_de,max_de,min_ag,max_ag=list(map(str,input().split()))
    if int(min_at) <= at <= int(max_at) and int(min_de) <= de <= int(max_de) and int(min_ag) <= ag <= int(max_ag):
        print(s)
        count+=1
if count==0:
    print("no evolution")
