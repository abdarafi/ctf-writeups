from Crypto.Util.number import getPrime as gp
from gmpy2 import next_prime as np

key = int(np(gp(0xff) % 10000))

flag = open('p.txt').read()
array = []

for f in flag:
	temp = ord(f) * key % 10000
	temp = str(temp).rjust(4, '0')
	array.append(temp)

cipher = ' '.join(array)
enc = open('c.txt','w')
enc.write(cipher)
enc.close()
