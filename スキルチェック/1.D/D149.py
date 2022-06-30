a=input()
b=int(input())-1
for i in range(len(a)):
    if i==b:
        continue
    else:
        print(a[i],end="")
