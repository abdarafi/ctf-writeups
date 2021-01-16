Diberikan 4 file terenkripsi dan sebuah file public key. Lalu kami lakukan pengecekan dari file public tersebut.

```openssl rsa -noout -text -inform PEM -in public_key.pem -pubin```

Dengan asumsi public key yang disertakan mempunyai nilai modulus yang dapat ditemukan di situs factordb, langsung hajar dengan rsatool.

``` python rsatool.py -p 261405546274977273223526430686751806507 -q 282951240817731535316382617983090875677 -o private.key ```

Terakhir dekripsi file tadi.

``` openssl rsautl -in flag0.enc -out /dev/tty -inkey private.key -decrypt ```
Flag: GEMASTIK{Gem4571kITS}