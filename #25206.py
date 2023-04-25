import sys
hak_hap = 0
score_hap = 0
for i in range(20):
    sub, hak, score = map(str, sys.stdin.readline().split())
    hak = float(hak)
    if score != 'P':
        hak_hap += hak
        if score == 'A+':
            score_hap += hak*4.5
        elif score == 'A0':
            score_hap += hak*4.0
        elif score == 'B+':
            score_hap += hak*3.5
        elif score == 'B0':
            score_hap += hak*3.0
        elif score == 'C+':
            score_hap += hak*2.5
        elif score == 'C0':
            score_hap += hak*2.0
        elif score == 'D+':
            score_hap += hak*1.5
        elif score == 'D0':
            score_hap += hak*1.0
        elif score == 'F':
            score_hap += hak*0.0

print(f"{score_hap/hak_hap:.6f}")
