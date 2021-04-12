# anonymous
# Inline Functions
# lambda Functions

data = (lambda n1, n2: "Hi " + n1 + " " + n2)("Boss", "Bunny")
print(data)
li=[1,2,3]
data2 = lambda *n1 : n1
print(data2(li))

add = lambda a, b: "Sum is {0}".format(a+b)
print(add(5,6))
if 5 > 2: print("Yes")

