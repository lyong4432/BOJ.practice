fir = []
sec = []
for i in range(10):
    a = int(input())
    fir.append(a)
for i in range(10):
    b =  int(input())
    sec.append(b)

fir.sort(reverse=True)
sec.sort(reverse=True)
print(sum(fir[:3]),sum(sec[:3]))
