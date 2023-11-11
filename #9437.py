while True:
    s = input()
    if s == '0': break
    n,p = s.split()
    n,p = int(n),int(p)
    if p%2==0:
        N = [p-1,n-p+1,n-p+2]
    else: 
        N = [p+1,n-p,n-p+1]
    N.sort()
    print(*N)
