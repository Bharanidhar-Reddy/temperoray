def add(*args):
    sum = 0
    for a in args:
        sum += a
    return args, sum

print(lambda *a:)
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4))
print("Hello world")

# var length keyword args


def sayhi(*args, **kwargs): # Generic function supports both keyword and positional arguments
    if args:
        print(type(args), args)
    else:
        print(type(kwargs), kwargs,"kwargs")


sayhi("Hello")
sayhi(name1="a")
sayhi(name1="a", name2="b")
sayhi(name1="a", name2="b", name3="c")
sayhi("hi", name1="a", name2="b", name3="c")
