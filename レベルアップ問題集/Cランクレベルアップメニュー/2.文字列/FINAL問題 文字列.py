n=int(input())
a=[]
for i in range(n):
    b=list(map(str,input().split()))
    h=int(b[0][0:2])
    m=int(b[0][3:5])

    b[1]=int(b[1])
    b[2]=int(b[2])

    h=h+b[1]

    if m + b[2] >= 60:
        h = str(h + 1)
        m = str(m + b[2] - 60)
    else:
        h = str(h)
        m = str(m + b[2])

    if h==24:
        h=0

    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m

    a.append(h + ":" + m)

for i in range(len(a)):
    print(a[i])