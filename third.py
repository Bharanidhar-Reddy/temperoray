def sayhi(n1, n2, n3):
    print("Hi " + n1 + " " + n2 + " " + n3)


li = ["a", "b", "c"]
sayhi(*li)

s = {"a", "b", "c", "c"}
sayhi(*s)

d = {"n1": "aa",  "n3": "cb", "n2": "cc"}
sayhi(**d)