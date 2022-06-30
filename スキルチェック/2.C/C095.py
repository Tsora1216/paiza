import itertools

x=input()


xlist = itertools.permutations(x)
temp_list=[]
for temp in xlist:
    temp_list.append("".join(temp))

y=input()
if y in temp_list:
    if x==y:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
