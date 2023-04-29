a,b,c = map(int, input().split())

if a == b == c:
    print('*')
elif a == b:
    print('C')
elif b == c:
    print('A')
elif c == a:
    print('B')
