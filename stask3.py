x="welcome to, futura labs"
print(len(x))
print(type(x))

print("to" in x)
print("an" in x)

print("to" not in x)
print("an" not in x)


for i in x:
    print(i)

for i in x:
    print(i)
print(x[3])
print(x[1:6])
print(x[1:])
print(x[:6])
print(x[-3])
print(x[-6:-2])

print(x.upper())
print(x.lower())

y="  nice classes"
print(y)

print(y.strip())

print(x.split(","))

print(x.count("f"))

print(y.replace("nice","excellent"))

print(x+y)

a="nice class{}"
b=56

print(a.format(b))
