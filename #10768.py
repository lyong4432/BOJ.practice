# 2/18 -> Special, ~2/17 -> Before, 2/19~ -> After

m = int(input())
d = int(input())

if m == 2 :
    if d == 18:
        print('Special')
    elif d > 19:
        print('After')
    else:
        print('Before')
elif m > 2:
    print('After')
else: 
    print('Before')
