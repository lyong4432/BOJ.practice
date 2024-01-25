import sys 
input = sys.stdin.readline  

EP = ['Never gonna give you up', \
      'Never gonna let you down',\
        'Never gonna run around and desert you',\
            'Never gonna make you cry',\
                'Never gonna say goodbye',\
                    'Never gonna tell a lie and hurt you',\
                        'Never gonna stop']

n = int(input())

flag = 1
for i in range(n):
    s = input().strip()
    if s not in EP: 
        flag = 0

if flag == 0: print('Yes')
else: print('No')
