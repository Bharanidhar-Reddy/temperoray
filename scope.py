data = 'Hello World'  # Global scope


def demo():
    data2 = 'hi'
    print(data)


#  print(data2)

#  test = demo()   return of demo is passed
test = demo  # Function demo is passed


def caller(a):
    print(type(a))
    print("Inside Function")
    a()


caller(demo)

print("Outer Inner")


def outer():
    print(data)
    print("This is outer")

    def inner():
        print("Inner Function")
    inner()


outer()