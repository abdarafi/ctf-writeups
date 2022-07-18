with open('out', encoding='utf-8') as f:
    enc = f.read()

k = ord(enc[0]) - ord('f')

flag = ''
for c in enc:
    flag += chr(ord(c) - k)

print(flag)