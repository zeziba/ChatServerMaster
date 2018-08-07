import base64
import zlib


def encode(data):
    return zlib.compress(base64.b64encode(str(data).encode("utf-8")), 9)


def decode(data):
    return base64.b64decode(zlib.decompress(data))


def utf8len(s):
    return len(str(s).encode('utf-8'))


if __name__ == "__main__":
    msg = "help! THERE ARE ZOMBIES" * 100

    compressed = encode(msg)

    print(utf8len(msg), utf8len(compressed))

    uncompressed = decode(compressed)

    print(compressed, uncompressed)

    with open("cmp.txt", "w+") as file:
        file.write(str(compressed))

    with open("ncmp.txt", "w+") as file:
        file.write(msg)
