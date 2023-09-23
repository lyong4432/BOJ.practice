import sys
input = sys.stdin.readline

a = input().strip()
len_a = len(a)
if len(a) == 1:
    print(int(a))
else:
    a_0 = int(a[0])
    a_0x = int(a[1:])

    hap = 0
    for i in range(1,len(a)):
        hap += int('9'+'0'*(i-1))*i

        


    hap += (a_0x+1)*len_a + (a_0-1)* int(str(len(a))+'0'*(len(a)-1))

    print(hap)
