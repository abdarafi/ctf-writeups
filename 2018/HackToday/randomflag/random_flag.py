from random import *
import sys, os, base64, string
import time

def yeah(string):
  temp = 0
  for i in string:
    temp += ord(i)
  return temp

strset = open('plaintext.txt').read().split('\n')
N = 50 + (yeah(os.urandom(3)) % 10)

for c in range(N):
  secure_seed = yeah(os.urandom(3))
  seed(secure_seed)
  password = strset[secure_seed % len(strset)]
  
  cipher = ''
  for p in password:
    cipher += chr(ord(p) ^ randint(0x00, 0xff))
  print 'Decrypt me: %s' % format(base64.b64encode(cipher))

  t1 = time.time()
  aw = raw_input('Your password: ')
  t2 = time.time()

  if t2 - t1 > 0.5:
    print '\n [-] Out of time!\n'
    sys.exit(0)
  elif aw == password:
    print '\n [+] Correct!\n'
  else:
    print '\n [-] Wrong!\n'
    sys.exit(0)

flag = open('flag').read()
print '+++ Congrats! +++'
print flag
