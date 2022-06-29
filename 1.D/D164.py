x=int(input())
i=0
flag=0
while 2**i <= x:
    if 2**i==x:
        flag=1
        break
    i+=1
if flag==0:
    print("NG")
else:
    print("OK")
