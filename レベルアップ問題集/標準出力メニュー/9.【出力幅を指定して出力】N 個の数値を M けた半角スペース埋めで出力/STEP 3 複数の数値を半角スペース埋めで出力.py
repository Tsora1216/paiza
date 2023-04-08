#n複数行のみの読み込み
n=int(input())
v = []
for i in range(n):
    v.append(int(input()))

for i in range(n):
    print("{:3d}".format(v[i]))