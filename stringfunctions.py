data = "Hello world!"
print("length ", len(data))
print(data.index("o"))
print(data.index("o", 5))
print(data.index("o", 5, 8))
print(data.count("l"))
print(data.upper())
print(data.lower())
print(data.startswith("Hel"))
print(data.endswith("gg"))
words = data.split(" ")
print(words)
print(data.replace("Hell", "Heaven"))
print(data.find("o"))
print(data.find("o", 5, 7))


data2 = "this is a {0} from {2} {1}"
sub1 = "String"
lang = "Python"
print(data2.format(sub1, lang, "gg"))

tempdata = """Hello {fname} {lname} welcome 
                to {city}"""
datastring = tempdata.format(fname="boss", lname="bunny", city="hyderabad")
print(datastring)

ob = {
    "fname": "sachin",
    "lname": "tendulkar",
    "city": "Banglore"
}
objs = [
{
    "fname": "sachin",
    "lname": "tendulkar",
    "city": "Banglore"
},
{
    "fname": "sewag",
    "lname": "bhai",
    "city": "kolkata"
},
{
    "fname": "yuvraj",
    "lname": "singh",
    "city": "Pune"
}
]


def mysort(el):
    return el["fname"]


objs.sort(key=mysort, reverse=True)
print(objs)
dataob = tempdata.format(**ob)
print(dataob)

for obj in objs:
    print(tempdata.format(**obj))