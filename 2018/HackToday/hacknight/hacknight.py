#!/usr/bin/env python
import random, os, sys, time
import sys


level = 1
seed = os.urandom(32)
random.seed(seed)
damage = 0
exp = 0

health = random.randint(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
# print health
key = 26298068352792965782519228504287136151889532657078500100364707176111106349660684157555898878754695600709667361396999664032940210066117813897748927347719018997408801594001722211590014659304479256914455511907280683931446512121654782405142907079603284246898425904025749860749313017966773009577028655535612480029325812139720905832453624411869743327921410657379684455292052668008442689560590350637515661313340186668305001760358598603173849192742254219519144062843682893665280112273855452207249316245095485364633110571377320117080627658172724787161232267276496855812989243731756959307171737303004551572369029896793247670733

enemy = {'attack':0, 'health':0}


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


def init():
	print "|Dramaga Studios Present|"
	loading()
	print "|HacKnight V1.0|"

def stat():
	print "Level kamu : {}".format(level)
	print "Exp : {}".format(exp)

def kupon():
	print "Berikut kupon hadiah hari ini"
	lucky_point = health + level
	print pow(lucky_point, 3, key)

def taunting():
	taunt = "Itu saja kemampuanmu?"
	for i in taunt:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.1)

def recover():
	global health, damage, enemy, exp, level, key
	print "Pergi ke pub. Memulihkan HP mu"
	print "HP kamu pulih sebanyak {}".format(damage)
	health += damage
	damage = 0

def fight_command():
	
	print """
* Musuh menyerang. Mengurangi {} Hp mu
Musuh. HP : {}.
Instruction
|A| Attack
|T| Taunt
""".format(enemy['attack'], enemy['health'])

def fight():
	global health, damage, enemy, exp, level, key
	damage = 0
	enemy['attack'] = random.randint(0, 10)
	enemy['health'] = random.randint(0, 100)
	exp_get = enemy['health']
	while 1:
		health = health - enemy['attack']
		damage += enemy['attack']
		fight_command()
		hehe = raw_input()
		if(hehe == 'A'):
			enemy['health'] -= health
		elif(hehe == 'T'):
			taunting()
		if(enemy['health'] <= 0):
			break
	print "SFX : tet tenet tenet teneeeeet"
	print "Kamu menang"
	print "Kamu mendapatkan {} exp".format(exp_get)
	exp += exp_get
	if(exp > 100):
		exp -= 100
		level += 1
		print "Lv {} -> Lv {}".format(level-1, level)
		
hero = '''

  ,^.
  |||
  |||       _T_
  |||   .-.[:|:].-.
  ===_ /\\|  "\'"  |/
   E]_|\\/ \\--|-|\'\'\'\'|
   O  `\'  \'=[:]| H  |
          /""""|  T |
         /"""""`.__.\'
        []"/"""\\"[]
        | \\     / |
        | |     | |
      <\\\\\\)     (///>

'''
def header():
	print hero
	stat()
	print """
Perintah :
|F| Fight Enemy
|P| Go to pub
|T| Taunt
|K| Cek Kupon
|Y| Gacha Item
|X| Exit Game
"""

def loading():
	print "_Now Loading_"
	for i in range(5):
		sys.stdout.write(" . ")
		sys.stdout.flush()
		# time.sleep(1)
	print 

def gacha():
	print "Menangkan kesempatan berhadiah item langka berupa flag tanpa diundi"
	lucky_point = health + level
	random.seed(lucky_point)
	win_flag = random.randint(1, 1111111111111111111111111)
	print "pilih angka 1 - 1111111111111111111111111 : "
	angka = raw_input()

	loading()
	if(str(win_flag) == angka):
		print "SELAMAT ANDA MENDAPATKAN FLAG DARI KAMI"
		print open("flag").read()
	else:
		print "Maaf anda belum beruntung. Silahkan coba kembali ya:\"((("

init()

while 1:
	header()
	pil = raw_input()
	if(pil == "F"):
		fight()
	elif(pil == "T"):
		taunting()
	elif(pil == "P"):
		recover()
	elif(pil == "K"):
		kupon()
	elif(pil == "Y"):
		gacha()
	elif(pil == "X"):
		print "Terimakasih telah memainkan games ini. xoxo"
		sys.exit(0)