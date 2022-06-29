s=input()
Before_list=["A","E","G","I","O","S","Z"]
After_list=["4","3","6","1","0","5","2"]
for i in range(len(Before_list)):
    s=s.replace(Before_list[i],After_list[i])
print(s)
