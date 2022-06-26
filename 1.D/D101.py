n,m=map(int,input().split())
print("YES") if n%2==0 and m%2==1 or m%2==0 and n%2==1 else print("NO")
