myDict = {
    "priyanshu": "a very good boy",
    "time": "running of a clock",
    "Age": [76, 34, 45],
    "Dynasty": {"Rajput": "clan"},
    1: 2
}

# print(type(myDict.keys()))  # prints the keys of the dictionary

# print(myDict.values())  # prints the values of the dictionary

# print(myDict.items())  # prints all keys and values , contents of the dictionary

print(myDict)
updateDict = {
    "ritesh": "freind",
    "kullu": "manali"
}
# updates the values by adding key-value pairs from updateDict
myDict.update(updateDict)
print(myDict)

# .get and [] syntax is the difference
print(myDict.get("kullu2"))  # returns none and runs successfully
# print(myDict["kullu2"]) throws error as kullu2 is not in the dictionarys
