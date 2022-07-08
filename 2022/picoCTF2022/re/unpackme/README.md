# Unpackme - 300
Can you get the flag? Reverse engineer this binary.

unpack the binary with `upx` since it was packed with UPX.
```bash
upx -d <file>
```

disassemble with Ghidra and look at the comparison function
```
if (local_44 == 754635) {
	local_40 = (char *)rotate_encrypt(0,&local_38);
	fputs(local_40,(FILE *)stdout);
	putchar(10);
	free(local_40);
}
```

it compares a variable with value 754635, simply input it and we get the flag:
picoCTF{up><_m3_f7w_77ad107e}