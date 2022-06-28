S=input()
htime=int(S[:S.find(":")])-8
mtime=S[S.find(":")+1:]
if htime<0:
    htime+=24
print(str(htime)+":"+str(mtime))
