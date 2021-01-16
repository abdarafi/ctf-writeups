#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random, string, base64

# flag = open("flag", "r").read()
def main():
    flag = "8Y5O8NaXBzcvMQqjfQZAlVcY3RN6a+E3EY5hGwZAmiaXFmxUBmBZMZdt4jZpHQdj4vqpFDZUMQd7U36Nxt4blrqVTwaZBvHXFrs1MQNyMich4jxRHmBiGDZK6SPYa5EQaRoPz+u83SL0SqqzSNaEEZHTrEXofV8+PzTj2e+g2OpuWV/KlApd0tdnrNhHmZdIGihdUtnh8t8Rx3TilYZoTvx+BrBjFQZgFwhuMvdp4mPAHDEwHioLG+qe6Raqa+HfzSsW35Nl3NcaSZxSEEBmrqZFfzftPeSvPOIs2V77Wzbklt7/03bJ6qu4mELUTDu/Umbp83fAxYSwxAILTrPtBQEvBwosFvu7MrLk4DqO4iaNHjHbGmsc6+x5aSBDz5Z2zRhx3+d6SEP3EqErENoBrV5VfO6ZPV4X2zX1WeRyWAXC0YR90RcMmqNGmwcCUDN98Y5O8A6Nxt4blrqVTwaZBvHXFrs1MQNyMich4jxRHmBiGDZK6SPYa5EQaRoPz+u83SL0SqqzSNaEEZHTrEXofV8+PzTj2e+g2OpuWV/KlApd0tdnrNhHmZdIGihdUIX="
    a = 'COMPFEST11{'
    d = Decoder()
    print(d.decode(flag))

def shuffle_string(s):
    s = list(s)
    random.shuffle(s)
    return "".join(s)


class Decoder(object):
    std = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def __init__(self):
        self.perm = shuffle_string(self.std)
        self.enc = str.maketrans(self.std, self.perm)

    def decode(self, s):
        return base64.b64decode(s).decode().translate(self.enc)

if __name__ == "__main__":
    main()
