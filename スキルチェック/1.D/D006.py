n,s=input().split()
print(int(n)*1000*100*10) if s=="km" else print(int(n)*100*10) if s=="m" else print(int(n)*10)
