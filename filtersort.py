objs = [
{
    "team": "india",
    "fname": "sachin",
    "lname": "tendulkar",
    "city": "Banglore"
},
{
    "team": "india",
    "fname": "sewag",
    "lname": "bhai",
    "city": "kolkata"
},
{
    "team": "india",
    "fname": "yuvraj",
    "lname": "singh",
    "city": "Pune"
},
{
    "team": "aus",
    "fname": "se",
    "lname": "bb",
    "city": "Pune"
},
    {
    "team": "aus",
    "fname": "ss",
    "lname": "bb",
    "city": "Pune"
},
    {
    "team": "aus",
    "fname": "gg",
    "lname": "gg",
    "city": "Pune"
}
]


def myfilter(ele):
    return ele["fname"][0] == "y" and ele["team"] == "india"


# newobj = filter(lambda ele: ele["fname"][0]=="s" and ele["team"]=="india",objs)
newobj = filter(myfilter, objs)

for i in newobj:
    print("{fname} {lname}".format(**i))
