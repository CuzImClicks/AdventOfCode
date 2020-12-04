from hashlib import md5

m = md5()
x = 0

while True:
    msg = f"ckczppom{x}"
    hash = md5(msg.encode()).hexdigest()
    print(f"{x} {msg} - {hash}")
    if hash.startswith("000000"):
        print("\n\n")

        break

    x += 1