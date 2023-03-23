# 사분면 고르기 

x = int(input())
y = int(input())
quadrant = 0

if x > 0 :
    if y > 0 :
        quadrant = 1
    elif y < 0:
        quadrant = 4
elif x < 0:
    if y > 0 :
        quadrant = 2
    elif y < 0:
        quadrant = 3

print(quadrant)
