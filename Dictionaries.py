dic = {
    "Subhan" : "Fast Student",
    "Sarwar" : "UCP Student"
}

print(dic["Subhan"])

data = {
    "Roll Number" : "22P-9447",
    "Name" : "Subhan",
    "Age" : "20",
    "Discpline" : "CS"
}

print(data)
print(data["Roll Number"])
print(data.get("Section"))
print(data.keys())


for key in data.keys():
    print(f"The value for {key} is {data[key]}")
    
print(data.items())

for key,value in data.items():
        print(f"The value for {key} is {value}")
