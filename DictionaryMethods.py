data = {
    1 : 40,
    2 : 60,
    3 : 20,
    4 : 88
}

data2 = {
    5 : 67,
    6 : 88,
    7 : 45
}

data.update(data2)
print(data)

data2.clear()
print(data2)

data.pop(4)
data.popitem()
print(data)

del data[1]
print(data)

del data
#print(data)
