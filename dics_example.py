# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    #  "year": 2020, #  não aceita duplicidade
}
print(thisdict)

print(thisdict["year"])
print(len(thisdict))
print(type(thisdict))
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

##############################################################
# acessar o valor de um item

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

x = thisdict.get("model")
