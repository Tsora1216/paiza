N,M=list(map(int,input().split()))
p=0
for i in range(M):
    money=int(input())
    if p>=money:
        p-=money
    else:
        N-=money
        p+=money//10
    print(N,p)
