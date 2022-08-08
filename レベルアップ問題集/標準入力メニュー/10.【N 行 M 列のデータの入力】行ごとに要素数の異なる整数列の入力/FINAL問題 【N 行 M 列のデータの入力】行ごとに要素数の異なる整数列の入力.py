N=int(input())
for i in range(N):
    s=input().split(" ")
    s.pop(0)
    print(*s)
