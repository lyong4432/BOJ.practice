cnt = []
for i in range(5):
    n = input()
    if 'FBI' in n:
        cnt.append(i+1)

if cnt==[]:
    print('HE GOT AWAY!')
else:
    for i in cnt:
        print(i, end= ' ')
