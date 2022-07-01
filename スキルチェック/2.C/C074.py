h,w,x=list(map(int,input().split()))
ans_list=""
for i in range(h):
    ans_list+=input()
for j in range(len(ans_list)):
    print(ans_list[j],end="")
    if (j+1)%x==0:
        print("")
