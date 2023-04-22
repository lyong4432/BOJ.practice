import math
au, ad = map(int, input().split())
bu, bd = map(int, input().split())


u = au*bd + bu*ad
d = ad*bd

print(u//math.gcd(u,d), d//math.gcd(u,d))
