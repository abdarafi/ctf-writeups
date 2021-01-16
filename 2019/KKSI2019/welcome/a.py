from string import printable
a = "1663323d00434ad7#ca8ecca2b#22844"

b = "1fee4be0b38ae6b8722b49e4db037bbd"

for x in a:
    if x == "#":
        print("karakter ke: ",a[x])
    else:
        continue
