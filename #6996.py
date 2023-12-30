import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(str, input().split())

    print(f'{a} & {b} are ',end='')

    a = str.join('',sorted(a))
    b = str.join('',sorted(b))

    if a == b: print('anagrams.')
    else: print('NOT anagrams.')
