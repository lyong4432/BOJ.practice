a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a != b != c != d: 
    list_all = [a,b,c,d]
    sorted_li = sorted(list_all)
    sorted_li_re = sorted_li[::-1]
    if list_all == sorted_li:
        print('Fish Rising')
    elif list_all == sorted_li_re:
        print('Fish Diving')
    else: 
        print('No Fish')
elif a == b == c == d:
    print('Fish At Constant Depth')
else:
    print('No Fish')
