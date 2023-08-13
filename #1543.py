import sys

input = sys.stdin.readline
s = input().strip()
search_s = input().strip()

cnt = s.count(search_s)
print(cnt)
