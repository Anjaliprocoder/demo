x="she is very good girl"
print(x)
print(len(x))
print(type(x))

print("is" in x)
print("an" in x)
print("is" not in x)
print("an" not in x)

for i in x:
    print(i)

print(x[2:6])
print(x[5:])
print(x[:8])
print(x[-4:-1])
print(x[-4:])
print(x[:-2])    

print(x.upper())
print(x.lower())

y="  it was an amazing.place"
print(y)
print(y.strip())
print(y.split("."))


print(x.count("e"))
print(y.count("t"))

print(x.replace("good","calm"))

print(x+y)

#print(a+b)
a="{} nice place"
b=12
print(a.format(b))
