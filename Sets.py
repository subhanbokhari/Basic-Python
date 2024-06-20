s = {2, 2, 4, 6, 7, 3, 5}
print(s)

info = set()


s2 = {3, 4, 6, 7, 3, 7, 2, 8}

print(s.union(s2))

print(s.intersection(s2))

s.update(s2)
print(s)

n3 = s.symmetric_difference(s2)
print(n3)

print(s.isdisjoint(s2))
print(s.issuperset(s2))
print(s.issubset(s2))

s2.add(9)
print(s2)

s2.remove(9)
print(s2)

s2.discard(3)
print(s2)

print(s2.pop())

del s
s2.clear()