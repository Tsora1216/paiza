N,Q=map(int,input().split())
keys=[input() for i in range(N)]
values=[i+1 for i in range(N)]

d = dict(zip(keys,values))

#print(d)

inputlist = [input() for j in range(Q)]
for j in range(Q):
    try:
        print(d[inputlist[j]])
    except:
        print("-1")
