d={"college":"geci","year":2024,"place":"idukki"}
print(d)
print(len(d))
print(type(d))

print(d["college"])

print("course" in d)
print("course"not in d)

print(d.get("year"))

print(d.keys())

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

d["college"]="Sahrudaya"
print(d)

d.update({"year":2025})
print(d)

d[""]="course"
print(d)

d1=d.copy()
print(d1)

d1=dict(d)
print(d1)

d.pop("college")
print(d)

d.popitem()
print(d)

del d["year"]
print(d)

d.clear()
print(d)

del d

college={"dept1":{"course":"cse","year":2024},"dept2":{"course":"ece","year":2024},"dept3":{"course":"eee","year":2024}}
print(college)
print(college["dept1"])

print(college["dept1"]["course"])
print(college["dept2"]["year"])
