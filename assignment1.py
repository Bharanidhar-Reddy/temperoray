data = [
    {"id": "111", "name": "laptop", "cost": 50000, "rating": 2, "discount": 40, "category": "Electronics", "brand": "Asus"},
    {"id": "222", "name": "laptop", "cost": 69999, "rating": 4, "discount": 30, "category": "Electronics", "brand": "Acer"},
    {"id": "333", "name": "laptop", "cost": 79999, "rating": 5, "discount": 10, "category": "Electronics", "brand": "Acer"},
    {"id": "444", "name": "phone", "cost": 32999, "rating": 2, "discount": 60, "category": "Electronics", "brand": "Asus"},
    {"id": "555", "name": "phone", "cost": 35999, "rating": 4, "discount": 20, "category": "Electronics", "brand": "Acer"},
    {"id": "666", "name": "shirt", "cost": 1999, "rating": 3.4, "discount": 30, "category": "Lifestyle", "brand": "Polo"},
    {"id": "777", "name": "shirt", "cost": 1599, "rating": 4, "discount": 20, "category": "Lifestyle", "brand": "Raymond"},
    {"id": "888", "name": "pant", "cost": 2999, "rating": 4, "discount": 20, "category": "Lifestyle", "brand": "Polo"},
    {"id": "999", "name": "pant", "cost": 2599, "rating": 3, "discount": 30, "category": "Lifestyle", "brand": "Raymond"}
]

i = -1
while i != 0:
    print("Press 1. to sort by cost Low to High")
    print("Press 2. to sort by cost High to Low")
    print("Press 3. to sort Rating")
    print("Press 4. to sort by Discount Low to High")
    print("Press 5. to sort by Discount High to Low")
    print("Press 0 to exit")
    i = int(input("Enter your option : "))
    if i == 1:
        data.sort(key=lambda ele: ele["cost"])
        for d in data:
            print(d)
    elif i == 2:
        data.sort(key=lambda ele: ele["cost"], reverse=True)
        for d in data:
            print(d)
    elif i == 3:
        data.sort(key=lambda ele: ele["rating"], reverse=True)
        for d in data:
            print(d)
    elif i == 4:
        data.sort(key=lambda ele: ele["discount"])
        for d in data:
            print(d)
    elif i == 5:
        data.sort(key=lambda ele: ele["discount"], reverse=True)
        for d in data:
            print(d)
    else:
        break

fields = {1: ["cost", False], 2: ["cost", True], 1: ["rating", True], 1: ["discount", False], 1: ["discount", True]}
while inp != 0:
    print("Press 1. to sort by cost Low to High")
    print("Press 2. to sort by cost High to Low")
    print("Press 3. to sort Rating")
    print("Press 4. to sort by Discount Low to High")
    print("Press 5. to sort by Discount High to Low")
    print("Press 0 to exit")
    inp = int(input("Enter your option "))
    data.sort(key=lambda ele: ele[fields[inp][0]], reverse=fields[inp][1])
    for d in data:
        print(d)