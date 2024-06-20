l = [1, 4, 3, 2, 1]
print(l)
l.append(7)
print(l)
l.sort()
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))
m = l
m[0] = 0
print(l)
k = l.copy()
k[0] = 3
print(l)
print(k)
l.insert(1,899)
print(l)
j = [900, 1000, 1100]
j.extend(m)
print(j)
f = m + k
print(f)
