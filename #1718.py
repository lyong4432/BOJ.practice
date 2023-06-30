s = input()
code = input()
code = (code*len(s))[:len(s)]
word = ''
for i in range(len(s)):
    if s[i] == ' ':
        word += ' '
    else: 
        a = ord(s[i])-ord(code[i]) + 96
        
        if a < 97:
            a += 26
        word += chr(a)

print(word)
