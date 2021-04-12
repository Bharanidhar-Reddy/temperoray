def hi():
    print("Hi Function")
hi()

def hi(name):
    print("Hi ! ", name)
hi(input("Enter Name : "))

def hi(name1, name2):
    print("Hi ! " + name1 + " " + name2)

hi(name2=input("Enter name1: "), name1=input("Enter name2: "))

print(type(hi))
print(hi)