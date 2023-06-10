plate = input()
height = 10
pre = plate[0]
for i in plate[1:]:
    if pre == i:
        height += 5
    else: height += 10

    pre = i

print(height)
