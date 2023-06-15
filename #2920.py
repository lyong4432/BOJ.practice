a = list(map(int, input().split()))

sorted_a = sorted(a)

if a == sorted_a:
    print('ascending')
else:
    sorted_a.reverse()
    if a == sorted_a:
        print('descending')
    else: print('mixed')
