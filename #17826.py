score = list(map(int, input().split()))
hong = int(input())

if 0 <= score.index(hong) <= 4:
    print('A+')
elif score.index(hong) <= 14:
    print('A0')
elif score.index(hong) <= 29:
    print('B+')
elif score.index(hong) <= 34:
    print('B0')
elif score.index(hong) <= 44:
    print('C+')
elif score.index(hong) <= 47:
    print('C0')
elif score.index(hong) <= 49:
    print('F')
