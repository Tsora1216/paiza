n=input()
[print(n[i]) if (i+1)%10==0 else print(n[i],end="") for i in range(len(n))]
