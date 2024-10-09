import sys

SECRET_KEY = "We lay, my love and I, beneath the weeping willow." # Change for your local copy
PORT_MAX = 2**16 - 1

simple_hasher = lambda s: sum([ord(c) for c in s])
easy_hasher = lambda s: eval('*'.join([str(ord(c)) for c in s]))
repeats = lambda n:True in [f"{n}".count(f'{d}') > 2 for d in range(0, 10)]

hash = simple_hasher(SECRET_KEY.join(sys.argv)) * easy_hasher(SECRET_KEY.join(sys.argv))

if "--nopattern" in sys.argv:
    allowed = [i for i in range(7700, PORT_MAX+1) if not repeats(i)]
    print(len(allowed))
    print(allowed[hash % len(allowed)])
    sys.exit(0)

print(hash % (PORT_MAX - 6600) + 6600)
