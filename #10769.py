sen = input()
s , h = 0, 0

h = sen.count(':-)')
s = sen.count(':-(')

if h == 0 and s == 0:
    print('none')
elif h > s:
    print('happy')
elif h < s:
    print('sad')
else: print('unsure')
