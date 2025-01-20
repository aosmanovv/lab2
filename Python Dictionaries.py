thisdict = {  #thisdict = dict(name = "John", age = 36, country = "Norway")
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(thisdict["brand"]) #x = thisdict.get("brand")

print(len(thisdict))
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
thisdict["year"] = 2018 #thisdict.update({"year": 2020})
print(type(thisdict))

x = thisdict.keys() #return all keys
x = thisdict.values() #return all values
x = x = thisdict.items() #return all keys and values
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red" #thisdict.update({"color": "red"})
thisdict.pop("model") #to delete. del thisdict["element"]
thisdict.popitem() #remove the last inserted item
print(thisdict)
thisdict.clear() #clear totaly

for x in thisdict:  #print only keys
    print(x)

for x in thisdict: #print all values  for x in thisdict.values():
    print(thisdict[x])

for x, y in thisdict.items(): #print all items
    print(x, y)

mydict = thisdict.copy()


myfamily = {  #nested dictionaries
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}

child1 = { #second variant
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items(): #print all items
    print(x)

    for y in obj:
        print(y + ':', obj[y])