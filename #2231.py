a = int(input())
result = 0
for i in range(a):
    isum = sum ( list(map(int, str(i))))

    if i+ isum == a:
        result = i 
        break

print(result)
