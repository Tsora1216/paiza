S=input()
rep_list= ("a", "e", "i", "o", "u" , "A", "E", "I", "O", "U" )
for i in range(len(rep_list)):
    S=S.replace(rep_list[i],'')
print(S)
