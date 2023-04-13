N = int(input())
A = [int(x) for x in input().split()]

ans_list=[]
for i in range(10):
    ans_list.append(A.count(i))

print(*ans_list)