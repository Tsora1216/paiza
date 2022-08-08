N=input()
for i in range(len(N)):
    print(N[i],end="")
    if (i+1)%3==0 and (i+1)!=len(N):
        print(",",end="")
    