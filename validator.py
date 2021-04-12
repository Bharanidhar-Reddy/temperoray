def allstrings(a):

    def inner(*args, **kwargs):
        for i in args:
            if type(i) != str:
                print("Invalid Arguments")
                break
        else:
            for k in kwargs.values():
                if type(k) != str:
                    print("Invalid Arguments")
                    break
            else:
                a(*args, **kwargs)
    return inner


@allstrings
def hello(name):
    print("Hello " + name)


@allstrings
def sayhi(name1, name2):
    print("Hi " + name1 + " and " + name2)


# demo1 = outer(hello)
# demo1()
# demo2 = outer(sayhi)
# demo2()

# hello = outer(hello) # same as @outer
# sayhi = outer(sayhi)


hello("sachin")
sayhi(name2="warner", name1="smith")

hello(22)
sayhi(name2=True, name1="smith")
