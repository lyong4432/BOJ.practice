n = int(input())
res = []
for i in range(n):
    s = input()
    res.append(s)
 
sorted_res = sorted(res)
revered_res = sorted(res, reverse=True)
if res == sorted_res:
    print('INCREASING')
elif res == revered_res:
    print('DECREASING')
else: print('NEITHER')
