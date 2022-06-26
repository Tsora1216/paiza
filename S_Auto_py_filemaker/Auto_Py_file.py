import pathlib
import os

os.mkdir(r'./D')
os.mkdir(r'./C')
os.mkdir(r'./B')
os.mkdir(r'./A')
os.mkdir(r'./S')

mydict={1:"D",2:"C",3:"B",4:"A",5:"S"}

for i in range(1,6):
    for j in range(1,501):
        mystr_a=format(j,'03')
        mystr_b=mydict[i]+mystr_a
        mypath=pathlib.Path(r".\\"+mydict[i]+"\\"+mystr_b+'.py')
        mypath.touch()
