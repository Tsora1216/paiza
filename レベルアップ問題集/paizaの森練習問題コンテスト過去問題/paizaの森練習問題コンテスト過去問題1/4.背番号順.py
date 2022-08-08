n=int(input())
dict={}
for i in range(n):
    b,p=list(map(str,input().split()))
    dict[int(b)]=p

sorted_dict=sorted(dict.keys())

for i in sorted_dict:
    print(i,dict[i])