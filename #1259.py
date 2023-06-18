res = []
while True:
    s = input()
    if s == '0':
        break 
    else: 

        if s[:len(s)//2] == s[::-1][:len(s)//2]:
            res.append('yes')
        else: res.append('no')

for i in res: print(i)
