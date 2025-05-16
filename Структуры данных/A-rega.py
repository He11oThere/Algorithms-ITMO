import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    names = data[1:1+n]

    return names

def rega(names):
    db = {}

    for name in names:

        if name not in db:
            db[name] = 1
            print("OK")

        else:
            suf = db[name]
            while True:
                new_name = name + str(suf)

                if new_name not in db:
                    db[new_name] = 1
                    db[name] = suf + 1
                    print(new_name)
                    break

                suf += 1


def start():
    names = read_data()
    rega(names)


start()
