import re
n=int(input())
mydict={}
for i in range(n):
    s=input()
    temp=re.findall(r"\d+",s)
    mydict[int(temp[0])]=s
sort_dict_keys=sorted(mydict)
for i in range(len(mydict)):
    print(mydict[sort_dict_keys[i]])
