dis_v = int(input())
v = int(input())


if v <= dis_v:
    print('Congratulations, you are within the speed limit!')
else:
    if  v - dis_v <= 20:
        n = 100
    elif v - dis_v <= 30:
        n = 270
    else: n = 500
    print('You are speeding and your fine is $%d.'%n)
