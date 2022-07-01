count=0
for i in range(int(input())):
    t,e,m,s,j,g=list(map(str,input().split()))
    if int(e)+int(m)+int(s)+int(j)+int(g)>=350:
        #print(i,"350in")
        if t=="s":
            #print(int(m)+int(s))
            if int(m)+int(s)>=160:
                count+=1
                #print(i,"S160in")
        else:
            if int(j)+int(g)>=160:
                count+=1
                #print(i,"I160in")
print(count)
