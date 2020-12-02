from hashlib import md5

m = md5()
x = 0

while True:
    msg = f"ckczppom{x}"
    hash = md5(msg.encode()).hexdigest()
    if hash.startswith("0000000"):
        print("\n\n")
        print(f"{x} {msg} - {hash}")
        break

    x += 1