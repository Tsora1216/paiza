x,y=list(map(str,input().split()))
xscore=str(int(x[0])+int(x[1]))[-1]
yscore=str(int(y[0])+int(y[1]))[-1]
print("Bob") if xscore>yscore else print("Draw") if xscore==yscore else print("Alice")
