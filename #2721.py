t = int(input())
w_list = []
for i in range(t):
    n = int(input())
    hap = 0
    for j in range(1,n+1):
        hap += (j * ((j+1)*(j+2)//2))
    w_list.append(hap)

for i in w_list:
    print(i)
