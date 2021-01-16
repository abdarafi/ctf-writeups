

import gmpy

p = 15100118367560938297
q = 18238194893394268367

#p,q didapat dari factordb.com dari nilai n
e = 5
n = p * q
c = 170841202002112185870598344402287193795
phi = (p-1) * (q-1)

d = gmpy.invert(e,phi)

#Cara dekripsi

m = hex(pow(c,d,n))[2:]

for i in range(len(m)/2):
	beuh = m[:2]
	print chr(int(beuh, 16))
	m = m[2:]
