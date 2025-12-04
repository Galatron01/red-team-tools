hash = input("Enter hash: ")

if len(hash) == 32:
    print("Possible MD5")
elif len(hash) == 40:
    print("Possible SHA1")
elif len(hash) == 64:
    print("Possible SHA256")
else:
    print("Hash length not recognised")
