h,w=list(map(int,input().split()))
dy,dx=list(map(int,input().split()))
print(abs(dx)*h+abs(dy)*w-abs(dx)*abs(dy))
