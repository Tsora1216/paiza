n=int(input())

#配列Aを用意
a=[]
for i in range(n):
    #ひとつずつ格納
    a.append("paiza")

#空白を交えながら出力
print(*a)
