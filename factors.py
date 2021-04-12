i = int(input("Enter number : "))
print(list(filter(lambda j: i % j == 0, range(1, i+1))))
