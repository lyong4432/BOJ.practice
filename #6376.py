import sys
import math
input = sys.stdin.readline

hap = 0
print("n e")
print("- -----------")
print("0 1")
print("1 2")
print("2 2.5")
for i in range(10):
    hap += 1/math.factorial(i)
    if i>2:
        print("%d %.9lf"%(i,hap))

    

