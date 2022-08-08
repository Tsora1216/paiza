import numpy as np
list=np.arange(1,int(input())+1)
re_list=list.reshape(2,4)
for i in range(len(re_list)):
    print(*re_list[i])