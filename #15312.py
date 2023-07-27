a = input()
b = input()
goong = []
alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(len(a)):
    goong.append(alpha[ord(a[i])-65])
    goong.append(alpha[ord(b[i])-65])


while True:
    new = []
    for i in range(len(goong)-1):
        a = (goong[i]+goong[i+1])%10
        new.append(a)
    if len(new) == 2: 
        print(new[0],new[1],sep='')
        break
    else: goong = new
