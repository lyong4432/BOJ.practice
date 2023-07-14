s1 = input()
s2 = input()
arr = []
for i in range(len(s1)):
    arr.append(int(s1[i]))
    arr.append(int(s2[i]))

l = len(arr)
while l> 2:
    new = []
    for i in range(l-1):
        n = (arr[i] + arr[i+1])%10
        new.append(n)
    arr = new
    l = len(arr)

print(arr[0],arr[1],sep='')
