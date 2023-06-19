s = input()

if s[:len(s)//2] == s[::-1][:len(s)//2]:
    print('true')
else: print('false')
