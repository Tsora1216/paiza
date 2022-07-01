a,b,r=list(map(int,input().split()))
n=int(input())
ans_list=[]
for i in range(n):
    x,y=list(map(int,input().split()))
    if ((x-a)**2)+((y-b)**2)>=r**2:
        print("silent")
    else:
        print("noisy")
