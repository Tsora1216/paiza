H,W,r,c=map(int,input().split())
a=[input() for i in range(H)]
[print("No") if a[r-1][c-1] == "." else print("Yes")]