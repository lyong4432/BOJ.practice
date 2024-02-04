cnt = 0

for _ in range(int(input())):
    s = input()
    s = int(s[2:])
    if s <= 90: cnt += 1

print(cnt)
