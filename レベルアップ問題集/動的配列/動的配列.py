N,Q=map(int,input().split())
A=list(map(str,input().split()))

for i in range(Q):
    query=list(map(str,input().split()))
    if query[0]=="0":
        A.append(query[1])
    elif query[0]=="1":
        A.pop(-1)
    else:
        print(*A)