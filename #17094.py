n = int(input())
s = input()

cnt_2 = s.count('2')
cnt_e = s.count('e')

if cnt_e == cnt_2:
    print('yee')
elif cnt_2 > cnt_e:
    print('2')
else: print('e')
