#!/usr/bin/python3
import base64

with open("flag.txt") as f:
	c = f.read()

while True:
	a = c = base64.b64decode(c).decode('utf-8')
	if "{" in a:
		break

print(a)