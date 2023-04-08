#n複数行のみの読み込み
N,M=list(map(int,input().split()))
v = []
for i in range(N):
    v.append(int(input()))

for i in range(N):
    print("{:>{}}".format(v[i],M))
