def outer(a):

    def inner(*args, **kwargs):
        print("This is inner")
        a(*args, **kwargs)
    return inner



def hello(name):
    print("Hello " + name)



def sayhi(name1, name2):
    print("Hi " + name1 + " and " + name2)


# demo1 = outer(hello)
# demo1()
# demo2 = outer(sayhi)
# demo2()

hello = outer(hello) # same as @outer
sayhi = outer(sayhi)


hello("sachin")
sayhi(name2="warner", name1="smith")
