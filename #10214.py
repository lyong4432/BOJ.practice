t = int(input())
array = []
for i in range(0,t):
    y_w, k_w = 0,0
    for j in range(0,9):
        y,k = map(int, input().split())
        y_w += y
        k_w += k
    if y_w == k_w:
        array.append('Draw')
    elif y_w > k_w:
        array.append('Yonsei')
    else:
        array.append('Korea')

for i in array:
    print(i)
