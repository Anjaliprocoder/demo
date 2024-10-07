#values are in the form key value pairs
#key instead of position,key not be same
#ordered,changeable,duplicate values are not allowed

d={"name":"Anjali","age":24,"place":"Thrissur"}
print(d)
print(len(d))
print(type(d))

print(d["name"])

print("gender" in d)
print("gender"not in d)

print(d.get("age"))

print(d.keys())#to access keys only

print(d.values())

print(d.items())

for i in d:
    print(i)

for i in d:
    print(d[i])

for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)

d["name"]="Anjana"
print(d)

d.update({"age":17})
print(d)

d["gender"]="f"
print(d)

d1=d.copy()
print(d1)

d1=dict(d)
print(d1)

d.pop("name")
print(d)

d.popitem()#remove last item
print(d)

del d["age"]
print(d)

d.clear()
print(d)

del d
#print(d)


#nested dictionary
family={"child1":{"name":"arjun","age":17,"gender":"m"},"child2":{"name":"anjali","age":24,"gender":"f"},"child3":{"name":"anjana","age":17,"gender":"f"}}
print(family)
print(family["child1"])

print(family["child1"]["name"])
