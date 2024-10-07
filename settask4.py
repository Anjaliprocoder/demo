x={1,2,3,4,5}
print(len(x))
print(type(x))

for i in x:
    print(i)

print("2" in x)
print("2" not in x)
print("6" in x)
print("6" not in x)

x.add(8)
print(x)

x.remove(8)
print(x)

v={"of",4,"nice",9}
print(v)
x.update(v)
print(v)
 
x.discard(7)
print(x)

v.discard("nice")
print(v)

v.pop()
print(v)

t=x.union(v)
print(t)

w=x.intersection(v)
print(w)

y=x.difference(v)
print(y)

x.clear()
print(x)

#del v
print(v)