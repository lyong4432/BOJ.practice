n, m = map(int, input().split())

hap = 1
a = list(map(int, input().split()))
for i in a:
    hap *= i

print(hap%m)
