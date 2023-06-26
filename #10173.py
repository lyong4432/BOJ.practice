res = []

while True:
    s = input()
    if s == 'EOI':
        break
    else:
        s = s.lower()
        if 'nemo' in s:
            res.append('Found')
        else: res.append('Missing')

for i in res: print(i)
