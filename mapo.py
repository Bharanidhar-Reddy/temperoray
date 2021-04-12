obj = [22, 25, 19, 18, 30]


def mymap(el):
    return 32+el * 9/5


newobj = map(mymap, obj)

for i in newobj:
    print(i)

