n=int(input())
print("Hello ",end="")
for i in range(n):
    print(input(),end="")
    print(".",end="") if n-1==i else print(",",end="")
