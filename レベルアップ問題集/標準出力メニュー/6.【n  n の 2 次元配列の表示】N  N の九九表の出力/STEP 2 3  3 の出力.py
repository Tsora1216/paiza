N=list(map(int,input().split(" ")))
for i in range(len(N)):
    print(N[i],end="")
    if((i+1)%3==0):
        print()
    else:
        print(end=" ")