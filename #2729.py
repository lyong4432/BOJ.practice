n = int(input())
for i in range(n):
  a, b = map(str, input().split())
  a = int(a, 2)
  b = int(b, 2)
  c = a + b 
  print(bin(c)[2:])
