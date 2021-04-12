count = 0


def hello():
    out = 0
    global count
    count += 1

    def helloinner():
        nonlocal out
        out += 1
        return out

    return helloinner


hi = hello()
print("First", hi())
print("second", hi())
print("Third", hi())

#  This type of accessing is called closures
