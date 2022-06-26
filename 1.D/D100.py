S=input()
print(S.replace("_","-")) if S.count("-") > S.count("_") else print(S.replace("-","_"))
