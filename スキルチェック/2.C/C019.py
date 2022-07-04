q=int(input())
for i in range(q):
    n=int(input())
    temp_sum=0
    for i in range(1,n):
        if n%i==0:
            temp_sum+=i
    if n==temp_sum:
        print("perfect")
    elif n-1==temp_sum:
        print("nearly")
    else:
        print("neither")
        
