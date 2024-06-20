tup = (1, 5, 6, "blue")
print(type(tup), tup)
''' immutable'''

print(tup[3])
print(len(tup))
print(tup[-2])

tup2 = tup[1:4]
print(tup2)

if 5 in tup:
    print("Present")
    
cities = ("Lahore", "Islamabad", "Karachi")
temp = list(cities)
temp.append("Peshawar")
cities = tuple(temp)
print(cities)

t1 = (1, 2, 3, 4, 5, 5)
t2 = (5, 6, 7, 8)
t3 = t1 + t2
print(t3)
print(t3.count(5))

print(t1.index(3))
print(len(t1))


