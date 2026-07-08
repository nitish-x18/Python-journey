# List Comprehension--->

"""" list cpmprehinsion is a shortcut of create a new list 
     insted of writing 4-5 lines od code, we can write it in just one line."""

l = []
for i in range(1,6):
    l.append(i)

print(l)

# SYNTEX-->
# VARIABLE_NAME = [EXPRESSION FOR ITEM  IN ITERABLE]

numbers = [i for i in range(1,6)]
print(numbers)

li = []
for i in range(1,6):
    li.append(i*i)

print(li)

number = [i*i for i in range(1,6)]
print(number)

name = ["karan", "ritika", "sanya"]
c = [i.upper() for i in name]
print(c)

# INTERSECTION---> CREATE A NEW SET FOR INTERSECTION ELEMENTS
set1 = {"a","b","c"}
set2 = {"a","e","c"}

set3 = set1.intersection(set2)
# set1 & set2
print(set3)

# INTERSECTION_UPDATE---> WITHOUT CREATING NEW SET 
set1.intersection_update(set2)
print(set1)

# DIFFERENCE--->
set3 = set1.difference(set2)
print(set3)

# SYMMETRIC DIFFERENCE--->
set3 = set1.symmetric_difference(set2)
print(set3)


""" DICTIONARIES--->>>"""
# VALUES STORES IN THE KEY-VALUE PAIRS

disc = {
    "name": "riya",
    "age": 20,
    "student": True
}

print(disc)
print(disc["name"])
disc.get("name")
print(len(disc))

details = {
    "name": "nitish",
    "age": 20,
    "list": [1,2,3],
    "tupple": ("a","b","c")
}

element = (details.get("list"))
for e in element:
    print(e)

print(details.keys())
print(details.values())
print(details.items())

details["age"] = 21
print(details)

details["new_key"] = "kuch bhi"
print(details)

details.update({"name": "n"})
print(details)

# DEL()
# POP()
# POPITEMS()

# NESTED DICTIONARY--->
details = {
    "name": "nitish",
    "age": 20,
    "isstudent": True,
    "student": {
        "boy": True,
        "marks": [90,32,12]
    }
}

print(details["student"])

# MERG MANY DIFFERENT DICTIONARIES IN ONE DICTIONARY--->
member1 = {
    "name": "nitish"
}
member2 = {
    "name": "saks"
}
member3 = {
    "name": "abcc"
}

teamone = {
    "member1": member1,
    "member2": member2,
    "member3": member3,
}
print(teamone)