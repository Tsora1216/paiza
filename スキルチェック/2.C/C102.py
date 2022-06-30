mydict={}
for i in range(31):
    mydict[i+1]="x"
    
n=int(input())
nlist=[]
for i in range(n):
    mydict[int(input())]+="A"
m=int(input())
mlist=[]
for i in range(m):
    mydict[int(input())]+="B"

flag=0
for i in range(len(mydict)):
    if mydict[i+1]=="xAB" and flag==0:
        print("A")
        flag=1
    elif mydict[i+1]=="xAB" and flag==1:
        print("B")
        flag=0
    elif mydict[i+1]=="xA":
        print("A")
    elif mydict[i+1]=="xB":
        print("B")
    else:
        print(mydict[i+1])
