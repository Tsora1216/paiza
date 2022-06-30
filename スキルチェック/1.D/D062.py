S= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
s_1,s_2,s_3=list(map(int,input().split()))
print("".join(S[:s_1]))
print("".join(S[s_1:s_2+s_1]))
print("".join(S[s_2+s_1:]))
