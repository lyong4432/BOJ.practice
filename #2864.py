import sys


input = sys.stdin.readline
a,b= map(str, input().split())

big_a = a.replace('5','6')
small_a = a.replace('6','5')

big_b = b.replace('5','6')
small_b = b.replace('6','5')

print(int(small_a)+int(small_b), int(big_a)+int(big_b))
