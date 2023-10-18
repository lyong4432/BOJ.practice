for _ in range(int(input())):
    i,s = map(str, input().split())
    i = int(i)-1
    s = list(s)
    s.pop(i)
    print(*s,sep='')
