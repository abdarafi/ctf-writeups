from Crypto.Cipher import AES
import sys

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

rahasia = open("rahasia").read()
key = open("key").read()

def pad(pesan):
    if len(pesan)%16:
        return pesan + (16-len(pesan)%16)* 'F'
    else:
        return pesan
    
def get_IV():
    return rahasia[:16]

def encrypt(pesan):
    pesan = pad(pesan)
    IV = get_IV()
    return AES.new(key,AES.MODE_OFB,IV=IV).encrypt(pesan)

def head():
    print "kamu: Hi Wi Bu, apa kabar?\nWi Bu: Genki desu!\nkamu: Wibu luh, bau bawang!!1!!\nWi Bu:"
    print encrypt(rahasia[16:])

head()
    
while 1:
    print "Balas Wi Bu??(Y/N)"
    cmd = raw_input()
    if cmd.lower() == 'y':
        pesan = raw_input()
        print "kamu:"
        print encrypt(pesan)
        print "Wi Bu:"
        print encrypt(rahasia[16:])
    else:
        sys.exit(0)
