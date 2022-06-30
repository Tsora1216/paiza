n=int(input())
g=input()
count=0
for i in range(n):
    temp=input()
    if g in temp:
        print(temp)
        count+=1
if count==0:
    print("None")
