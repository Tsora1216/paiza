N,D=list(map(int,input().split()))
x=N*D
for i in range(N-1):
    x=x-int(input())
print(x*D)
