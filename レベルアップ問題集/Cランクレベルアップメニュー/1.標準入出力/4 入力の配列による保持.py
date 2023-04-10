n=int(input())

#配列Aを用意
a=[]
for i in range(n):
    #ひとつずつ格納
    a.append(int(input()))

#最大を出力
print(max(a))
