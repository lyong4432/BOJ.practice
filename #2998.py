a = input()
a = a[::-1]

ind = 0
for i in range(len(a)):
    ind += int(a[i])*2**i



print(oct(ind)[2:])
