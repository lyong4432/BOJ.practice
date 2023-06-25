k = int(input())
n = '1'*k
n = int(n, 2)


hap = n * (n+1) //2

print(bin(hap)[2:])
