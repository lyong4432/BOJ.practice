while True:
    try: 
        s,t = map(str, input().split())
        idx = 0
        for i in t:
            if i == s[idx]:
                idx += 1
                if idx == len(s): break
                
        if idx == len(s): print('Yes')
        else: print('No')
    except EOFError: break   
