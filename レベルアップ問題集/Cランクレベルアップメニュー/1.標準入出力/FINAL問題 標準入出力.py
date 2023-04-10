n=int(input())
a=[]
for i in range(n):
    a.append(list(map(str,input().split())))

for i in range(n):
    print(a[i][0],int(a[i][1])+1)