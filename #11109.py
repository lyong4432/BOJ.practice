for i in range(int(input())):
    d,n,s,p = map(int, input().split())
    if d+n*p < n*s: print('parallelize')
    elif d+n*p > n*s: print('do not parallelize')
    else: print('does not matter')
