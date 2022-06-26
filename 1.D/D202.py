li=[list(map(int,input().split())) for _ in range(2)]
print(sum(li[0])) if sum(li[0])<sum(li[1]) else print(sum(li[1]))
