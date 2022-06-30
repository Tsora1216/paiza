H=int(input())
Slist=list(map(str,input().split()))
if Slist.count("G") < Slist.count("P"):
    print("G")
elif Slist.count("G") == Slist.count("P"):
    print("Draw")
else:
    print("P")
