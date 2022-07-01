import itertools
list_num=list(map(int,input().split()))
tempA=sorted(list_num,reverse=True)
a=tempA.pop(0)
tempB=sorted(tempA,reverse=True)
b=tempB.pop(0)
print(a*10+b*10+sum(tempB))
