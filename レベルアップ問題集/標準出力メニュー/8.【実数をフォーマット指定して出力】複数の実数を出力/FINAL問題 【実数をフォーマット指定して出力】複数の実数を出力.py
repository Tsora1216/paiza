for i in range(int(input())):
    N,M=list(map(str,input().split()))
    N=float(N)
    M=int(M)
    print("{0:.{1:}f}".format(N,M))