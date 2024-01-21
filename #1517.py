result = 0

def merge(s, e):
    global result 
    if e - s < 1 : return
    m = int(s + (e - s)/2)
    merge(s,m)
    merge(m+1,e)
    for i in range(s, e+1):
        tmp[i] = A[i]

    k = s
    idx1 = s
    idx2 = m + 1
    while idx1 <= m and idx2 <= e: 
        if tmp[idx1] > tmp[idx2]:
            A[k] = tmp[idx2]
            result = result + idx2 - k
            k += 1
            idx2 += 1
        else: 
            A[k] = tmp[idx1]
            k += 1
            idx1 += 1
    while idx1 <= m: 
        A[k] = tmp[idx1]
        k += 1
        idx1 += 1

    while idx2 <= e: 
        A[k] = tmp[idx2]
        k += 1
        idx2 += 1

N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
tmp = [0] * (N+1)
merge(1,N)
print(result)
