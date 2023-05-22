#!/usr/bin/python3

from hashlib import sha256

HASH="4fd180f1b8c54208be120bd51b91f629952e6c989d7a78e6fb8133b10f3e110c"

def main():
    with open("./src/rockyou.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if sha256(line.strip().encode()).hexdigest() == HASH:
            print(line.strip())
            break

if __name__ == "__main__":
    main()

