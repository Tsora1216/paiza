m,d=list(map(str,input().split()))
day=m+d
print("Yes") if day.count(day[0])==len(day) else print("No")
